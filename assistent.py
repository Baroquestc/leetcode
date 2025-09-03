import re
import json
from typing import Optional, Dict, Any, List

try:
    import requests
except ImportError:
    requests = None
    import urllib.request
    import urllib.error

LEETCODE_GRAPHQL = "https://leetcode.cn/graphql"
USER_AGENT = "Mozilla/5.0 (compatible; LeetCodeFetcher/1.3; +https://leetcode.cn)"

def extract_slug(url: str) -> Optional[str]:
    if not url or not isinstance(url, str):
        return None
    m = re.search(r"/problems/([^/?#]+)/?", url)
    return m.group(1) if m else None

def http_post_json(url: str, body: Dict[str, Any], headers: Dict[str, str], timeout: int = 10) -> Optional[Dict[str, Any]]:
    try:
        if requests:
            resp = requests.post(url, headers=headers, json=body, timeout=timeout)
            if resp.status_code != 200:
                return None
            return resp.json()
        else:
            req = urllib.request.Request(
                url,
                data=json.dumps(body).encode("utf-8"),
                headers=headers,
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
    except Exception:
        return None

def http_get_text(url: str, headers: Dict[str, str], timeout: int = 10) -> Optional[str]:
    try:
        if requests:
            resp = requests.get(url, headers=headers, timeout=timeout)
            if resp.status_code != 200:
                return None
            return resp.text
        else:
            req = urllib.request.Request(url, headers=headers, method="GET")
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

# =============== GraphQL 查询 ===============

# QUERY_QUESTION = """
# query questionData($titleSlug: String!) {
#   question(titleSlug: $titleSlug) {
#     questionFrontendId
#     title
#     translatedTitle
#     titleSlug
#     difficulty
#     categoryTitle

#     topicTags { name translatedName slug }

#     content
#     translatedContent
#     similarQuestions
#   }
# }
# """

def fetch_via_graphql(slug: str) -> Optional[Dict[str, Any]]:
    body = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": """query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            translatedTitle
            titleSlug
            title
            difficulty
            topicTags { name translatedName slug }
            similarQuestions   # JSON string; may include frontendQuestionId
          }
        }""",
    }
    headers = {
        "content-type": "application/json",
        "user-agent": USER_AGENT,
    }
    data = http_post_json(LEETCODE_GRAPHQL, body, headers)
    q = (data or {}).get("data", {}).get("question")
    if not q:
        return None

    # 标签
    tags_raw: List[Dict[str, Any]] = q.get("topicTags") or []
    tags_cn = [t.get("translatedName") or t.get("name") or t.get("slug") for t in tags_raw]
    tags_cn = [t for t in tags_cn if t]

    # 相似题解析
    similar_raw = q.get("similarQuestions")
    similar_list: List[Dict[str, Any]] = []
    if isinstance(similar_raw, str) and similar_raw.strip():
        try:
            parsed = json.loads(similar_raw)
            candidates = []
            if isinstance(parsed, list):
                candidates = parsed
            elif isinstance(parsed, dict) and isinstance(parsed.get("questions"), list):
                candidates = parsed["questions"]

            for it in candidates:
                slug = it.get("titleSlug")
                # 题号字段在不同返回中可能叫 frontendQuestionId 或 questionFrontendId
                qid = it.get("frontendQuestionId") or it.get("questionFrontendId") or ""
                link = f"https://leetcode.cn/problems/{slug}/" if slug else ""
                similar_list.append({
                    "id": qid,
                    "title": it.get("title"),
                    "translatedTitle": it.get("translatedTitle"),
                    "titleSlug": slug,
                    "difficulty": it.get("difficulty"),
                    "isPaidOnly": it.get("paidOnly") or it.get("isPaidOnly"),
                    "url": link,
                })
        except Exception:
            pass

    qid = q.get("questionFrontendId")
    title_cn = q.get("translatedTitle") or q.get("title")
    title_slug = q.get("titleSlug")

    return {
        "id_title": f"{qid}.{title_cn}" if qid and title_cn else "",
        "id_title_slug": f"{qid}.{title_slug}" if qid and title_slug else "",
        "id": qid or "",
        "title_cn": title_cn or "",
        "title_slug": title_slug or "",
        "difficulty": q.get("difficulty") or "",
        "tags": tags_cn,
        "tags_detail": tags_raw,

        # 相似题（含题号与链接）
        "similarQuestionsRaw": similar_raw or "",
        "similarQuestions": similar_list,
    }

def scrape_fallback(url: str) -> Optional[Dict[str, Any]]:
    headers = {"user-agent": USER_AGENT}
    html = http_get_text(url, headers)
    if not html:
        return None

    m = re.search(r'"questionFrontendId":"(\d+)"[^}]*"translatedTitle":"([^"]+)"', html)
    qid, title_cn, id_title = "", "", ""
    if m:
        qid, title_cn = m.group(1), m.group(2)
        id_title = f"{qid}.{title_cn}"
    else:
        m2 = re.search(r'"questionFrontendId":"(\d+)"[^}]*"title":"([^"]+)"', html)
        if m2:
            qid, title_cn = m2.group(1), m2.group(2)
            id_title = f"{qid}.{title_cn}"

    md = re.search(r'"difficulty":"(Easy|Medium|Hard)"', html)
    difficulty = md.group(1) if md else ""

    tags = []
    tags_detail = []
    for tm in re.finditer(r'{"name":"([^"]*)","translatedName":"([^"]*)","slug":"([^"]*)"}', html):
        name, tcn, slug = tm.group(1), tm.group(2), tm.group(3)
        tags.append(tcn or name or slug)
        tags_detail.append({"name": name, "translatedName": tcn, "slug": slug})

    return {
        "id_title": id_title or "",
        "id": qid or "",
        "title_cn": title_cn or "",
        "difficulty": difficulty,
        "tags": tags,
        "tags_detail": tags_detail,
        "similarQuestionsRaw": "",
        "similarQuestions": [],
    }

def core(url: str) -> Dict[str, Any]:
    slug = extract_slug(url)
    if not slug:
        return {"id_title": "", "id_title_slug": "", "id": "", "title_cn": "", "title_slug": "", "difficulty": "", "tags": [], "tags_detail": [], "similarQuestionsRaw": "", "similarQuestions": []}

    data = fetch_via_graphql(slug)
    if data:
        return data

    fb = scrape_fallback(url)
    if fb:
        return fb

    if not url.rstrip("/").endswith("/description"):
        url_desc = re.sub(r"(/problems/[^/?#]+)(/)?(?:\?.*|#.*)?$", r"\1/description/", url)
        fb2 = scrape_fallback(url_desc)
        if fb2:
            return fb2

    return {"id_title": "", "id_title_slug": "", "id": "", "title_cn": "", "title_slug": "", "difficulty": "", "tags": [], "tags_detail": [], "similarQuestionsRaw": "", "similarQuestions": []}

def main(params: dict):
    print("读取到参数：", params)
    url = None
    for key in ("url", "URL", "link", "Link", "leetcode", "LeetCode"):
        if isinstance(params.get(key), str) and params[key].strip():
            url = params[key].strip()
            break
    if not url and isinstance(params.get("text"), str):
        m = re.search(r"https?://leetcode\.cn/[^\s\"']+", params["text"])
        url = m.group(0) if m else None

    if not url:
        return json.dumps({
            "id_title": "", "id_title_slug": "", "id": "", "title_cn": "", "title_slug": "", "difficulty": "",
            "tags": [], "tags_detail": [], "similarQuestionsRaw": "", "similarQuestions": []
        }, ensure_ascii=False)

    result = core(url)
    return json.dumps(result, ensure_ascii=False)

if __name__ == "__main__":
    test_params = {
        "url": "https://leetcode.cn/problems/rotate-list/"
    }
    print(main(test_params))
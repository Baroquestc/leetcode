#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1.迭代法
        # def merge_two(l1, l2):
        #     if not l1:
        #         return l2
        #     if not l2:
        #         return l1
            
        #     dummy = ListNode(-1)
        #     cur = dummy

        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             cur.next = l1
        #             l1 = l1.next
        #         else:
        #             cur.next = l2
        #             l2 = l2.next
        #         cur = cur.next
        #     cur.next = l1 if l1 else l2

        #     return dummy.next
        
        # if not lists:
        #     return None

        # while len(lists) > 1:
        #     merged_lists = []
        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i + 1] if i + 1 < len(lists) else None
        #         merged_lists.append(merge_two(l1, l2))
        #     lists = merged_lists

        # return lists[0]

        # 2.递归法
        def merge_two(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val <= l2.val:
                l1.next = merge_two(l1.next, l2)
                return l1
            else:
                l2.next = merge_two(l1, l2.next)
                return l2
        
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge_two(l1, l2))
            lists = merged_lists
        return lists[0]
# @lc code=end


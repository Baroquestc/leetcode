#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.cn/problems/lru-cache/description/
#
# algorithms
# Medium (54.38%)
# Likes:    3441
# Dislikes: 0
# Total Accepted:    809.4K
# Total Submissions: 1.5M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# 
# Example 1:
# 
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
# 
# 
#

# @lc code=start
class Node:  
    """双向链表节点"""  
    def __init__(self, key: int, value: int):  
        self.key = key  
        self.value = value  
        self.prev = None  # 前驱节点  
        self.next = None  # 后继节点  


class LRUCache:  
    """LRU 缓存实现"""  
    def __init__(self, capacity: int):  
        self.capacity = capacity  # 缓存容量  
        self.cache = {}  # 哈希表存储键值对  
        # 创建伪头部和伪尾部节点  
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail  
        self.tail.prev = self.head  

    def _remove(self, node: Node) -> None:  
        """移除双向链表中的一个节点"""  
        prev_node = node.prev  
        next_node = node.next  
        prev_node.next = next_node  
        next_node.prev = prev_node  

    def _add_to_head(self, node: Node) -> None:  
        """将节点添加到双向链表的头部"""  
        node.prev = self.head  
        node.next = self.head.next  
        self.head.next.prev = node  
        self.head.next = node  

    def get(self, key: int) -> int:  
        """获取键对应的值，如果不存在返回 -1"""  
        if key in self.cache:  
            node = self.cache[key]  
            # 移动到头部（表示最近使用过）  
            self._remove(node)  
            self._add_to_head(node)  
            return node.value  
        return -1  

    def put(self, key: int, value: int) -> None:  
        """插入或更新键值对"""  
        if key in self.cache:  
            # 如果键已存在，更新值并移动到头部  
            node = self.cache[key]  
            node.value = value  
            self._remove(node)  
            self._add_to_head(node)  
        else:  
            # 如果键不存在，创建新节点  
            if len(self.cache) >= self.capacity:  
                # 如果超出容量，移除链表尾部节点（最久未使用）  
                tail_node = self.tail.prev  
                del self.cache[tail_node.key]  
                self._remove(tail_node)  
            # 插入新节点到头部  
            new_node = Node(key, value)  
            self.cache[key] = new_node  
            self._add_to_head(new_node)    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


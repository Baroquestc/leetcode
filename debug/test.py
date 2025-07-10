class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 输入一个数组，转换为一条单链表
def createLinkedList(arr: 'List[int]') -> 'ListNode':
    if arr is None or len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head

# 单链表的遍历/查找/修改
def printLinkedList(head: 'ListNode'):
    cur = head
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print()

def findNode(head: 'ListNode', val: 'int') -> 'ListNode':
    cur = head
    while cur is not None:
        if cur.val == val:
            return cur
        cur = cur.next
    return None

def modifyNode(head: 'ListNode', val: 'int', newVal: 'int') -> 'ListNode':
    cur = head
    while cur is not None:
        if cur.val == val:
            cur.val = newVal
            return cur
        cur = cur.next
    return None

# 输入一个单链表，转换为数组
def createArray(head: 'ListNode') -> 'List[int]':
    arr = []
    cur = head
    while cur is not None:
        arr.append(cur.val)
        cur = cur.next
    return

    
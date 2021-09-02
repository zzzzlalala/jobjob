class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class solution:
    # 链表长度
    def removeNth(self, head, n):
        def getLenth(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLenth(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    # 栈
    def removeNth(self, head, n):
        dummy = ListNode(0, head)
        stack = []
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

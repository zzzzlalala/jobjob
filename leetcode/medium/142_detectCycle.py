class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class solution:
    # 快慢指针
    # slow=a+b fast=a+n(b+c)+b  fast=2*slow -> a = (n-1)(b+c)+c
    # 当slow==fast时，令fast=head,每次走一步再相遇时，在入环处相遇
    def detectCycle(self, head):
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next
class solution:
    def reverseList(self,head):
        # 迭代
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        # 递归
    def reverseList2(self,head):
        # 终止条件就是当前为空或者下一个节点为空
        if not head or not head.next:
            return head
        cur =  self.reverseList2(head)
        # 反转
        head.next.next = head
        head.next = None
        return cur



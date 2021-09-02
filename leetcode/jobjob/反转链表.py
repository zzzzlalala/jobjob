"""
1.双指针迭代
2.递归
"""
class soluton:
    def reveseList1(self,head):
        cur,pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    def reverseList2(self,head):
        def helper(cur,pre):
            if not cur:
                return pre
            res = helper(cur.next,cur)
            cur.next = pre
            return res
        return helper(head,None)

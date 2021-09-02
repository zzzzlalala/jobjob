class solution:
    def isHuiwen(self,head):
        head_val = []
        cur = head
        while cur is not  None:
            head_val.append(cur.val)
            cur = cur.next
        return head_val ==head_val[::-1]
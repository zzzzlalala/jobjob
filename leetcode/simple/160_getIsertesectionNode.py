class solution:
    def xiangjiaoNode(self,headA,headB):
        # 双指针
        A= headA
        B = headB
        while A!=B:
            # 不相交 走完A走B
            A = A.next if A else headB
            B = B.next if B else headA
        return A
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class solution:
    # 归并递归
    def sortList1(self,head):
        if not head or not head.next:
            return head
        slow, fast = head,head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        left = self.sortList1(head)
        right = self.sortList1(mid)
        l1=left
        l2=right
        dummyhead = ListNode(0)
        ans  = dummyhead
        while l1 and l2:
            if l1.val< l2.val:
                dummyhead.next = l1
                l1.next = l1
            else:
                dummyhead.next = l2
                l2.next = l2
            dummyhead = dummyhead.next
        if l1 ==None:
            dummyhead.next=l2
        elif l2== None:
            dummyhead.next=l1
        return ans.next







    def sortList3(self, head):
        # 递归超时
        def sortFunc(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return mergeTwoLists(sortFunc(head, tail), sortFunc(mid, tail))

        # def mergeTwoLists(self, l1, l2):
        #     if l1 == None:
        #         return l2
        #     elif l2 == None:
        #         return l1
        #     elif l1.val < l2.val:
        #         l1.next = self.mergeTwoLists(l1.next, l2)
        #         return l1
        #     else:
        #         l2.next = self.mergeTwoLists(l1, l2.next)
        #         return l2

        def mergeTwoLists(l1, l2):
            prehead = ListNode(0)
            prev = prehead
            while l1 and l2:
                if l1.val < l2.val:
                    prev.next = l1
                    l1.next = l1
                else:
                    prev.next = l2
                    l2.next = l2

            if l1 == None:
                prev.next = l2
            elif l2 == None:
                prev.next = l1
            return prehead.next

        return sortFunc(head, None)

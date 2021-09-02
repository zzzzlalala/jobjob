class solution:
    def hasCycle(self, head):
        # 是否再次到达
        again = set()  # 不重复元素集
        while head:
            if head in again:
                return True
            again.add(head)
            head = head.next
        return False

    # O(1)
    def hasCycle2(self, head):
        # 快慢指针
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            # 快的走两步慢的走一步
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

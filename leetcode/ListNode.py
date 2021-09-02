class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkNode:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add_head(self, val):
        new_headnode = ListNode(val)
        new_headnode.next = self.head
        self.head = new_headnode

    def add_last(self, val):
        new_lastnode = ListNode(val)
        if self.is_empty():
            self.head = new_lastnode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_lastnode

    def insert_node(self, index, val):
        new_node = ListNode(val)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.add_head()
        elif index == self.length():
            self.add_last()
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            new_node.next = cur.next
            cur.next = new_node

    # 删除指定节点
    def remove_node(self, val):
        cur = self.head
        pre = None  # pre指向cur前一个节点
        #
        if self.head == val:
            self.head.next = self.head
        else:
            while cur.val is not val:
                pre = cur
                cur = cur.next
            pre.next = cur.next

    def search_node_in_exist(self, val):
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    def traversal(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
    def list2node(self,List):
        head = ListNode(List[0])
        cur =head
        for i in range(1,len(List)):
            cur.next = ListNode(List[i])
            cur = cur.next
        return head

from leetcode.ListNode import *


class solution:
    def addTwoNums(self, l1, l2):
        head = ListNode(l1.val + l2.val)
        cur = head
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            cur.next = ListNode(l1.val + l2.val + cur.val // 10)
            cur.val = cur.val % 10
            cur = cur.next
        if cur.val >= 10:
            cur.next = ListNode(cur.val // 10)
            cur.val = cur.val % 10
        return head


if __name__ == '__main__':
    # list = SingleLinkNode()
    # list.add_head(2)
    # list.add_head(1)
    # list.add_last(4)
    # list.insert_node(2, 3)
    # list.traversal()
    # print(list.is_empty())
    # print(list.length())
    # list.remove_node(4)
    # print(list.search_node_in_exist(3))
    # print(list.search_node_in_exist(4))
    # list.traversal()
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    l1 = node1
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    l2 = node1
    node4.next = node5
    node5.next = node6

    test = solution()
    test.addTwoNums(l1, l2)
    test = SingleLinkNode()
    test.traversal()

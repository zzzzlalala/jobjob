class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        node.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print('\nnode:', node, 'value:', node.val, 'next:', node.next)
            node = node.next

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next()
        result = ListNode()
        handle = ListNode_handle()
        for i in list:
            result = handle.add(i)
        return result


class solution:
    # 递归
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists(self,l1,l2):
        prehead = ListNode()
        prev = prehead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1.next = l1
            else:
                prev.next = l2
                l2.next = l2
            prev = prev.next
        if l1==None:
            prev.next = l2
        elif l2==None:
            prev.next = l1

        return prehead.next

ListNode_1 = ListNode_handle()

l1 = ListNode()
l1_list = [1, 8, 3]
for i in l1_list:
    l1 = ListNode_1.add(i)
ListNode_1.print_ListNode(l1)

l2 = ListNode()
l2_list = [3, 4, 5]
for i in l2_list:
    l2 = ListNode_1.add(i)
ListNode_1.print_ListNode(l2)

S = solution()
l3 = S.mergeTwoLists(l1, l2)
ListNode_1.print_ListNode(l3)

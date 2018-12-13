class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = LinkedNode(None)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        count = 0
        curr = self.head.next

        while curr and count != index:
            count += 1
            curr = curr.next

        return curr.val if curr else -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head.next
        new_node = LinkedNode(val)
        self.head.next = new_node
        new_node.next = curr


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new_node = LinkedNode(val)
        curr = self.head.next
        if curr is None:
            self.head.next = new_node
        else:
            while curr and curr.next:
                curr = curr.next
            curr.next = new_node


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        new_node = LinkedNode(val)

        prev = self.head
        curr = self.head.next
        count = 0

        while curr and count != index:
            count += 1
            prev = curr
            curr = curr.next

        if curr is None:
            if count == index:
                prev.next = new_node
            elif count < index:
                return
        else:
            prev.next = new_node
            new_node.next = curr


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        prev = self.head
        curr = self.head.next
        count = 0
        while curr and count != index:
            count += 1
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next

    def printlist(self):
        curr = self.head.next
        while curr:
            print(curr.val, end=' ')
            curr = curr.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
result = obj.get(0)
print(result)
obj.addAtHead(0)
obj.printlist()
print('\n')
obj.addAtTail(1)
obj.printlist()
print('\n')
obj.addAtIndex(3,2)
obj.printlist()
print('\n')
obj.deleteAtIndex(1)
obj.printlist()
print('\n')
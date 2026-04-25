class ListNode:
    """
    This class represents a linked list node.

    Args:
        value: Value of this node.

    Attributes:
        value: Value of this node.
        next: Link to the next node.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    This class represents a linked list.

    Args:
        args: Items can be specifiend as an arbitrary
            number of positional arguments.

    Attributes:
        head: The first node in the list.
        tail: The last node in the list.
    """

    def __init__(self, *args):
        if args:
            self.head = ListNode(args[0])

            prev = self.head
            for element in args[1:]:
                node = ListNode(element)
                prev.next = node
                prev = node

            self.tail = prev
        else:
            self.head = None
            self.tail = None

    def append(self, value):
        """
        Appends an item to the end of the list.

        Args:
            value: The item to append.
        """
        node = ListNode(value)

        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

    def prepend(self, value):
        """
        Prepends an item to the start of the list.

        Args:
            value: The item to prepend.
        """
        node = ListNode(value)

        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def insert(self, after, value):
        """
        Inserts an item after the specified node.

        Args:
            after: Node, after which the item should be inserted.
            value: The item to insert.
        """
        node = ListNode(value)

        node.next = after.next
        after.next = node

        if after == self.tail:
            self.tail = node

    def remove(self, node):
        """
        Removes a node from the list.

        Args:
            node: The node to remove.
        """
        if node == self.head:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next == node:
                    current.next = node.next

                    if node == self.tail:
                        self.tail = current

                    break

                current = current.next

    def __len__(self):
        count = 0

        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    def __str__(self):
        representation = "{"

        current = self.head
        while current:
            representation += str(current.value)

            if current.next:
                representation += " -> "

            current = current.next

        representation += "}"

        return representation


if __name__ == "__main__":
    lst = LinkedList(1, 4, 6, 7)
    print("First:", lst.head.value)
    print("Last:", lst.tail.value)

    print(lst)
    print("Len:", len(lst))

    print("Append 4")
    lst.append(4)
    print(lst)

    print("Prepend 66")
    lst.prepend(66)
    print(lst)

    el = lst.head.next.next
    print("Insert 99 after", el.value)
    lst.insert(el, 99)
    print(lst)

    el = lst.tail
    print("Insert 67 after", el.value)
    lst.insert(el, 67)
    print("Tail:", lst.tail.value)
    print(lst)

    print("Remove head")
    lst.remove(lst.head)
    print(lst)

    print("Remove tail")
    lst.remove(lst.tail)
    print(lst)

    el = lst.head.next.next
    print("Remove", el.value)
    lst.remove(el)
    print(lst)

    print("First:", lst.head.value)
    print("Last:", lst.tail.value)

    l_empty = LinkedList()
    print(l_empty)
    print(len(l_empty))

    print("Append 4")
    l_empty.append(4)
    print(l_empty)

    print("Prepend 66")
    l_empty.prepend(66)
    print(l_empty)

    el = l_empty.head.next
    print("Insert 99 after", el.value)
    l_empty.insert(el, 99)
    print(l_empty)

    el = l_empty.tail
    print("Insert 67 after", el.value)
    l_empty.insert(el, 67)
    print("Tail:", l_empty.tail.value)
    print(l_empty)

    print("Remove head")
    l_empty.remove(l_empty.head)
    print(l_empty)

    print("Remove tail")
    l_empty.remove(l_empty.tail)
    print(l_empty)

    print("First:", l_empty.head.value)
    print("Last:", l_empty.tail.value)

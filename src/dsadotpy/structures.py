class ListNode[T]:
    """
    This class represents a linked list node.

    Args:
        value: Value of this node.

    Attributes:
        value: Value of this node.
        next: Link to the next node.
    """

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: ListNode[T] | None = None


class LinkedList[T]:
    """
    This class represents a linked list.

    Args:
        args: Items can be specifiend as an arbitrary
            number of positional arguments.

    Attributes:
        head: The first node in the list.
        tail: The last node in the list.
    """

    def __init__(self, *args: T) -> None:
        self.head: ListNode[T] | None = None
        self.tail: ListNode[T] | None = None

        if args:
            self.head = ListNode(args[0])

            prev = self.head
            for element in args[1:]:
                node = ListNode(element)
                prev.next = node
                prev = node

            self.tail = prev

    def append(self, value: T) -> None:
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

    def prepend(self, value: T) -> None:
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

    def insert(self, after: ListNode[T], value: T) -> None:
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

    def remove(self, node: ListNode[T]) -> None:
        """
        Removes a node from the list.

        Args:
            node: The node to remove.
        """
        if node == self.head:
            self.head = self.head.next
            return

        current = self.head
        while current and current.next:
            if current.next == node:
                current.next = node.next

                if node == self.tail:
                    self.tail = current

                break

            current = current.next

    def __len__(self) -> int:
        count = 0

        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    def __str__(self) -> str:
        representation = "{"

        current = self.head
        while current:
            representation += str(current.value)

            if current.next:
                representation += " -> "

            current = current.next

        representation += "}"

        return representation


class HashNode[K, V]:
    """
    This class represents a key-value pair inside a hash table.

    This construction helps to solve collisions using chaining by
    making each bucket a linked list.

    Args:
        key: A hast table key.
        value: Value associated with this key.

    Attributes:
        key: A hast table key.
        value: Value associated with this key.
        next: The next key-value pair in this bucket.
    """

    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value
        self.next: HashNode[K, V] | None = None


class HashTable[K, V]:
    """
    This class represents a hash table.

    Internally, its values are stored as an array of linked lists.
    """

    def __init__(self) -> None:
        self.__state: list[None | HashNode[K, V]] = [None for _ in range(5)]
        self.__total: int = 0

    def __resize(self) -> None:
        old = self.__state.copy()
        self.__state = [None for _ in range(len(self.__state) * 2)]
        self.__total = 0

        for bucket in old:
            if bucket:
                current: HashNode[K, V] | None = bucket
                while current:
                    self.set(current.key, current.value)

                    current = current.next

    def __load_factor(self) -> float:
        return self.__total / len(self.__state)

    def __index(self, key: K) -> int:
        return hash(key) % len(self.__state)

    def get(self, key: K) -> V | None:
        """
        Retrieve a value associated with a given key.

        Args:
            key: A hash table key.

        Returns:
            Value associated with this key, or None if not exists.
        """
        index = self.__index(key)

        current = self.__state[index]
        while current:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def set(self, key: K, value: V) -> None:
        """
        Inserts a key-value pair into the hash table, or
        updates the value if the key already exists.

        Args:
            key: A hast table key.
            value: Value associated with this key.
        """
        index = self.__index(key)

        if not self.__state[index]:
            self.__state[index] = HashNode(key, value)
            self.__total += 1

            if self.__load_factor() >= 0.7:
                self.__resize()

            return

        current = self.__state[index]

        while current and current.next:
            if current.key == key:
                current.value = value
                return

            current = current.next

        if current:
            if current.key == key:
                current.value = value
            else:
                current.next = HashNode(key, value)
                self.__total += 1

                if self.__load_factor() >= 0.7:
                    self.__resize()

    def delete(self, key: K) -> None:
        """
        Deletes a key-value pair from the hast table.

        Args:
            key: A hash table key.
        """
        index = self.__index(key)

        current = self.__state[index]
        if current:
            if current.key == key:
                self.__state[index] = current.next
                self.__total -= 1
                return

            while current.next:
                if current.next.key == key:
                    current.next = current.next.next
                    self.__total -= 1
                    return

                current = current.next

    def __len__(self) -> int:
        return self.__total

    def __str__(self) -> str:
        buckets: list[str] = []

        for bucket in self.__state:
            if bucket:
                current: HashNode[K, V] | None = bucket
                while current:
                    buckets.append(f"{current.key}: {current.value}")

                    current = current.next

        return "{" + ", ".join(buckets) + "}"


if __name__ == "__main__":
    htable: HashTable[str, str] = HashTable()
    print(htable)

    htable.set("name", "Some User")
    htable.set("age", "20")
    print(htable)
    print("Length:", len(htable))

    age = htable.get("age")
    print(age)

    nonexistent = htable.get("nonexistent")
    print(nonexistent)

    htable.delete("name")
    print(htable)
    print("Length:", len(htable))

    htable.set("k1", "val1")
    print(htable)
    htable.set("k2", "val2")
    print(htable)
    htable.set("k3", "val3")
    print(htable)
    htable.set("k4", "val4")
    print(htable)
    htable.set("k5", "val5")
    print(htable)
    htable.set("k6", "val6")
    print(htable)

    lst = LinkedList(1, 4, 6, 7)

    assert lst.head
    assert lst.tail
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

    assert lst.head.next
    el = lst.head.next
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

    el = lst.head.next
    print("Remove", el.value)
    lst.remove(el)
    print(lst)

    print("First:", lst.head.value)
    print("Last:", lst.tail.value)

    l_empty: LinkedList[int] = LinkedList()
    print(l_empty)
    print(len(l_empty))

    print("Append 4")
    l_empty.append(4)
    print(l_empty)

    print("Prepend 66")
    l_empty.prepend(66)
    print(l_empty)

    assert l_empty.head
    assert l_empty.tail
    print("First:", l_empty.head.value)
    print("Last:", l_empty.tail.value)

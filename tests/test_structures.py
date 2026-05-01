from dsadotpy import structures


class TestLinkedList:
    def test_create_empty_list(self):
        test_list = structures.LinkedList()

        assert len(test_list) == 0
        assert test_list.head is None
        assert test_list.head is None

    def test_empty_list_append(self):
        test_list = structures.LinkedList()

        item = 32
        test_list.append(item)

        assert len(test_list) == 1
        assert test_list.tail == test_list.head
        assert test_list.head.value == item

    def test_empty_list_prepend(self):
        test_list = structures.LinkedList()

        item = 32
        test_list.prepend(item)

        assert len(test_list) == 1
        assert test_list.tail == test_list.head
        assert test_list.head.value == item

    def test_create_single_element_list(self):
        test_list = structures.LinkedList(5)

        assert len(test_list) == 1
        assert test_list.head == test_list.tail

    def test_create_list(self):
        test_list = structures.LinkedList(3, 5, 7, 12, 55)

        assert len(test_list) == 5
        assert test_list.head.value == 3
        assert test_list.tail.value == 55

    def test_list_append(self):
        test_list = structures.LinkedList(3, 5, 7, 12, 55)

        item = 32
        test_list.append(item)

        assert len(test_list) == 6
        assert test_list.tail.value == item

    def test_list_prepend(self):
        test_list = structures.LinkedList(3, 5, 7, 12, 55)

        item = 32
        test_list.prepend(item)

        assert len(test_list) == 6
        assert test_list.head.value == item

    def test_list_insert(self):
        test_list = structures.LinkedList(3, 5, 7, 12, 55)

        after = test_list.head.next
        item = 32
        test_list.insert(after, item)

        assert len(test_list) == 6
        assert test_list.head.next.next.value == item

    def test_list_remove(self):
        test_list = structures.LinkedList(3, 5, 7, 12, 55)

        node = test_list.head.next
        test_list.remove(node)

        assert len(test_list) == 4
        assert test_list.head.next != node


class TestHashTable:
    def test_empty_hash_table(self):
        htable = structures.HashTable()

        assert len(htable) == 0

    def test_hash_table_crud(self):
        htable = structures.HashTable()

        htable.set("k1", "val1")
        htable.set("k2", "val2")
        htable.set("k3", "val3")

        assert len(htable) == 3

        value = htable.get("k2")

        assert value == "val2"

        nonexistent = htable.get("nonexistent")

        assert nonexistent is None

        htable.delete("k2")

        assert len(htable) == 2

    def test_hash_table_resize(self):
        htable = structures.HashTable()

        htable.set("k1", "val1")
        htable.set("k2", "val2")
        htable.set("k3", "val3")

        assert len(htable) == 3
        assert len(htable._HashTable__state) == 5

        htable.set("k4", "val4")

        assert len(htable) == 4
        assert len(htable._HashTable__state) == 10

import unittest


class DoubleNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, node):

        if self.head is None:
            self.head = node
            self.tail = self.head
            return

        if self.head == self.tail:
            self.head = node
            self.head.next = self.tail
            self.tail.previous = self.head
            return

        self.head.previous = node
        self.head.previous.next = self.head
        self.head = node

    def remove_node(self, node):

        if not node:
            return

        if node == self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
            return

        if node == self.head:
            return

        node.next.previous = node.previous
        node.previous.next = node.next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_map = {}
        self.double_linked_list = DoublyLinkedList()
        self.capacity = capacity
        self.current_size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hash_map:
            node = self.hash_map[key]
            self.double_linked_list.remove_node(node)
            self.double_linked_list.prepend(node)
            return node.value[1]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.hash_map:
            if self.current_size >= self.capacity:
                self.hash_map.pop(self.double_linked_list.tail.value[0], None)
                self.double_linked_list.remove_node(self.double_linked_list.tail)
            else:
                self.current_size += 1
        else:
            self.double_linked_list.remove_node(self.hash_map.pop(key, None))

        self.double_linked_list.prepend(DoubleNode((key, value)))
        self.hash_map[key] = self.double_linked_list.head


# My unit tests
class LRUCachTest(unittest.TestCase):

    def test_empty_cache(self):

        my_cache = LRU_Cache(2)

        self.assertEqual(my_cache.get(1), -1)

    def test_non_existent_value(self):

        my_cache = LRU_Cache(2)
        my_cache.set(2, 4)

        self.assertEqual(my_cache.get(10), -1)

    def test_change_priority_set_fct_head_value(self):

        my_cache = LRU_Cache(5)
        my_cache.set(2, 4)
        my_cache.set(4, 16)
        my_cache.set(6, 36)

        self.assertEqual(my_cache.double_linked_list.head.value,
                         my_cache.hash_map[6].value)
        self.assertNotEqual(my_cache.double_linked_list.tail.value,
                            my_cache.hash_map[4].value)

    def test_change_priority_set_fct_tail_value(self):

        my_cache = LRU_Cache(5)
        my_cache.set(2, 4)
        my_cache.set(4, 16)
        my_cache.set(6, 36)

        self.assertNotEqual(my_cache.double_linked_list.tail.value,
                            my_cache.hash_map[4].value)

    def test_change_priority_get_fct(self):

        expected_order_list = [(4, 16), (6, 36), (2, 4), (8, 64), (10, 100)]

        my_cache = LRU_Cache(5)
        my_cache.set(2, 4)
        my_cache.set(4, 16)
        my_cache.set(6, 36)
        my_cache.set(8, 64)
        my_cache.set(10, 100)

        my_cache.get(10)
        my_cache.get(6)
        my_cache.get(8)
        my_cache.get(2)
        my_cache.get(6)
        my_cache.get(4)

        node = my_cache.double_linked_list.head
        order_list = []
        while node:
            order_list.append(node.value)
            node = node.next

        self.assertEqual(order_list, expected_order_list)

    def test_full_capacity_linked_list_value(self):

        expected_list = [(10, 100), (8, 64), (6, 36)]

        my_cache = LRU_Cache(5)
        my_cache.set(2, 4)
        my_cache.set(4, 16)
        my_cache.set(6, 36)
        my_cache.set(8, 64)
        my_cache.set(10, 100)

        node = my_cache.double_linked_list.head
        first_list = []
        while node:
            first_list.append(node.value)
            node = node.next

        my_cache.set(12, 144)
        my_cache.set(14, 196)

        node = my_cache.double_linked_list.head
        second_list = []
        while node:
            second_list.append(node.value)
            node = node.next

        intersection_list = [item for item in first_list
                             if item in second_list]

        self.assertEqual(intersection_list, expected_list)

    def test_full_capacity_hash_table_value(self):

        my_cache = LRU_Cache(5)
        my_cache.set(2, 4)
        my_cache.set(4, 16)
        my_cache.set(6, 36)

        my_cache.get(2)

        my_cache.set(8, 64)
        my_cache.set(10, 100)

        my_cache.get(6)

        my_cache.set(12, 144)
        my_cache.set(14, 196)

        self.assertEqual(my_cache.get(4), -1)

    def test_with_string(self):

        expected_list = ["camera", "outlook", "kindle", "youtube", "linkedin", "map",
                         "whatsapp", "viber", "hangouts"]

        my_cache = LRU_Cache(9)
        my_cache.set("gmail", "gmail")
        my_cache.set("hangouts", "hangouts")
        my_cache.set("kindle", "kindle")
        my_cache.set("viber", "viber")
        my_cache.set("whatsapp", "whatsapp")
        my_cache.set("map", "map")
        my_cache.set("linkedin", "linkedin")
        my_cache.set("youtube", "youtube")
        my_cache.set("outlook", "outlook")

        my_cache.get("kindle")
        my_cache.get("outlook")

        my_cache.set("camera", "camera")

        node = my_cache.double_linked_list.head
        result_list = []
        while node:
            result_list.append(node.value[1])
            node = node.next

        self.assertEqual(result_list, expected_list)

    def test_provided_project(self):

        expected_list = [1, 2, -1, -1]

        my_cache = LRU_Cache(5)
        my_cache.set(1, 1)
        my_cache.set(2, 2)
        my_cache.set(3, 3)
        my_cache.set(4, 4)

        result_list = []

        result_list.append(my_cache.get(1))
        result_list.append(my_cache.get(2))
        result_list.append(my_cache.get(9))

        my_cache.set(5, 5)
        my_cache.set(6, 6)

        result_list.append(my_cache.get(3))

        self.assertEqual(result_list, expected_list)


suite_loader = unittest.TestLoader()
suite = suite_loader.loadTestsFromTestCase(LRUCachTest)
unittest.TextTestRunner(verbosity=2).run(suite)


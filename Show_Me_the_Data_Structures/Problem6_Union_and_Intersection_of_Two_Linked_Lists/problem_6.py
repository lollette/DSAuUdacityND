import unittest
import time


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        if out_string:
            return out_string
        return "empty set"

    def append(self, value):

        if self.head is None:
            self.head = self.tail = Node(value)
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

    def get_size(self):
        return self.size


def union(llist_1, llist_2):
    # Your Solution Here
    linked_list_union = LinkedList()
    set_union = set()
    node = llist_1.head
    while node:
        set_union.add(node.value)
        node = node.next
    node = llist_2.head
    while node:
        set_union.add(node.value)
        node = node.next

    for value in set_union:
        linked_list_union.append(value)
    return linked_list_union


def intersection(llist_1, llist_2):
    # Your Solution Here
    linked_list_intersection = LinkedList()
    if llist_1.get_size() == 0 or llist_2.get_size() == 0:
        return linked_list_intersection

    set_intersection = dict()

    if llist_1.get_size() < llist_2.get_size():
        node1 = llist_1.head
        node2 = llist_2.head
    else:
        node1 = llist_2.head
        node2 = llist_1.head
    while node1:
        if node1.value not in set_intersection:
            set_intersection[node1.value] = 0
        node1 = node1.next
    while node2:
        if node2.value in set_intersection and set_intersection[node2.value] == 0:
            linked_list_intersection.append(node2.value)
            set_intersection[node2.value] = 1
        node2 = node2.next
    return linked_list_intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


# My tests

# For a clear display
print('\n\n\n\n\n')
time.sleep(0.1)


def get_values(llist):
    values_set = set()
    node = llist.head
    while node:
        values_set.add(node.value)
        node = node.next
    return values_set


class UnionIntersectionTest(unittest.TestCase):

    def test_random_example(self):
        element_1 = [47,  7,  3, 19, 74, 56, 28,  7,  8, 32, 99, 37, 48, 38,
                     23, 87, 8, 51, 95, 75]
        element_2 = [38, 54, 77, 88, 18, 17, 65, 15, 40, 12, 56, 28]

        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        union_set = get_values(union(linked_list_1, linked_list_2))
        intersection_set = get_values(intersection(linked_list_1, linked_list_2))

        union_set_expected = set(element_1).union(element_2)
        intersection_set_expected = set(element_1).intersection(element_2)

        self.assertTrue(union_set == union_set_expected and
                        intersection_set == intersection_set_expected)

    def test_random_example_with_negative_values(self):
        element_1 = [-18, 34, -36,-4, 16, 42, -16, -23, 24, 7, 19, 10]
        element_2 = [34, -10, 13, 47, -15, -35, -33, -37, -38, 4, -7, 14, -26,
                     24, 37, 10, -19, -21, 34, -36, -18, -4]

        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        union_set = get_values(union(linked_list_1, linked_list_2))
        intersection_set = get_values(intersection(linked_list_1, linked_list_2))

        union_set_expected = set(element_1).union(element_2)
        intersection_set_expected = set(element_1).intersection(element_2)

        self.assertTrue(union_set == union_set_expected and
                        intersection_set == intersection_set_expected)

    def test_both_empty_set(self):
        element_1 = []
        element_2 = []

        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        union_set = get_values(union(linked_list_1, linked_list_2))
        intersection_set = get_values(intersection(linked_list_1, linked_list_2))

        union_set_expected = set(element_1).union(element_2)
        intersection_set_expected = set(element_1).intersection(element_2)

        self.assertTrue(union_set == union_set_expected and
                        intersection_set == intersection_set_expected)

    def test_one_empty_set(self):
        element_1 = [-18, 34, -36,-4, 16, 42, -16, -23, 24, 7, 19, 10]
        element_2 = []

        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        union_set = get_values(union(linked_list_1, linked_list_2))
        intersection_set = get_values(intersection(linked_list_1, linked_list_2))

        union_set_expected = set(element_1).union(element_2)
        intersection_set_expected = set(element_1).intersection(element_2)

        self.assertTrue(union_set == union_set_expected and
                        intersection_set == intersection_set_expected)

    def test_no_intersection(self):
        element_1 = [-18, 34, -36, -4, 16, 42, -16, -23, 24, 7, 19, 10]
        element_2 = [38, 54, 77, 88, 18, 17, 65, 15, 40, 12, 56, 28]

        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        intersection_set = get_values(
            intersection(linked_list_1, linked_list_2))

        intersection_set_expected = set(element_1).intersection(element_2)

        self.assertTrue(intersection_set == intersection_set_expected)


suite_loader = unittest.TestLoader()
suite = suite_loader.loadTestsFromTestCase(UnionIntersectionTest)
unittest.TextTestRunner(verbosity=2).run(suite)



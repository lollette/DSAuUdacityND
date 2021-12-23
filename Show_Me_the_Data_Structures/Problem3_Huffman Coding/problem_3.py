import sys
import unittest
import time


class Node:
    def __init__(self, frequency=None, key=None, left_child=None,
                 right_child=None):

        self.frequency = frequency
        self.key = key
        self.left_child = left_child
        self.right_child = right_child

    def join_node(self, node):

        return Node(self.frequency + node.frequency, '', self, node)


class BinaryMinHeap:
    def __init__(self):
        self.nodes = []

    def insert(self, node):

        self.nodes.append(node)
        self.heapify_up()

    def delete(self):

        if self.is_empty():
            return None

        return_value = self.nodes[0]
        self.nodes[0] = self.nodes[-1]

        self.nodes.pop()

        self.heapify_down(0, self.get_left_child_index(0),
                          self.get_right_child_index(0))

        return return_value

    def heapify_up(self):

        child = len(self.nodes) - 1

        parent = self.get_parent_child_index(child)

        while self.nodes[child].frequency < self.nodes[parent].frequency:
            temp = self.nodes[child]
            self.nodes[child] = self.nodes[parent]
            self.nodes[parent] = temp
            child = parent

            parent = self.get_parent_child_index(child)

    def heapify_down(self, parent, left_child, right_child):

        if not self.valid_child(left_child) and \
                not self.valid_child(right_child):
            return

        if not self.valid_child(right_child) or \
                self.nodes[left_child].frequency < \
                self.nodes[right_child].frequency:

            if self.nodes[left_child].frequency < self.nodes[parent].frequency:
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[left_child]
                self.nodes[left_child] = temp

                parent = self.get_left_child_index(parent)

            else:
                return

        else:
            if self.nodes[right_child].frequency < self.nodes[parent].frequency:
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[right_child]
                self.nodes[right_child] = temp

                parent = self.get_right_child_index(parent)

            else:
                return

        self.heapify_down(parent, self.get_left_child_index(parent),
                          self.get_right_child_index(parent))

    def valid_child(self, index):
        return True if index < len(self.nodes) else False

    def get_left_child_index(self, index):
        return (2 * index) + 1

    def get_right_child_index(self, index):
        return (2 * index) + 2

    def get_parent_child_index(self, index):
        return int((index - 1) / 2)

    def is_empty(self):
        return len(self.nodes) == 0


class PriorityQueue:
    def __init__(self):
        self.pr_queue = BinaryMinHeap()

    def enqueue(self, node):
        self.pr_queue.insert(node)

    def dequeue(self):
        return self.pr_queue.delete()


def frequencies_count(data):
    nodes_set = {}

    for char in data:

        if char in nodes_set:
            nodes_set[char].frequency += 1
        else:
            nodes_set[char] = Node(1, char)

    dummy_char = chr(92) + chr(48)
    nodes_set[dummy_char] = Node(1, dummy_char)

    return nodes_set


def huffman_tree_building(nodes_set):

    pr_queue = PriorityQueue()

    for node in nodes_set.values():
        pr_queue.enqueue(node)

    min_freq_1 = pr_queue.dequeue()
    min_freq_2 = pr_queue.dequeue()

    while min_freq_2:
        pr_queue.enqueue(min_freq_1.join_node(min_freq_2))
        min_freq_1 = pr_queue.dequeue()
        min_freq_2 = pr_queue.dequeue()

    return min_freq_1


def assign_binary_code(node, code, char_code):

    if node.key:
        char_code[node.key] = code
        return

    if node.left_child:
        assign_binary_code(node.left_child, code + '0', char_code)

    if node.right_child:
        assign_binary_code(node.right_child, code + '1', char_code)


def huffman_encoding(data):
    assert len(data) != 0, "Data is empty."

    huffman_tree = huffman_tree_building(frequencies_count(data))

    char_code = dict()
    assign_binary_code(huffman_tree, '', char_code)

    data_code = ''
    for char in data:
        if char in char_code:
            data_code += char_code[char]
        else:
            print('Char object not found!')

    return data_code, huffman_tree


def huffman_decoding(data, tree):
    original_data = ''
    node = tree
    for char in data:
        if char == '0':
            node = node.left_child
        else:
            node = node.right_child
        if node.key:
            original_data += node.key
            node = tree

    return original_data


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: \n{}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: \n{}\n".format(decoded_data))


# My unit tests

# For a clear display
print('\n\n\n\n\n')
time.sleep(0.1)


class HuffmanCodingTest(unittest.TestCase):

    def test_symbol_char(self):
        string = '--*+***---+++///@@233%%3333& *)()*&&%%$^%^*$'
        encoded_data, tree = huffman_encoding(string)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) <
                        sys.getsizeof(string)
                        and decoded_data == string)

    def test_really_long_sentence(self):
        string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                 'Nullam et lacus a sem convallis vehicula vel non magna. Sed ' \
                 'a mattis risus, vel venenatis arcu. Cras odio mi, posuere ac ' \
                 'cursus at, cursus ac mauris. Integer tempor, tellus a consectetur ' \
                 'molestie, leo urna sodales risus, id accumsan nunc metus ' \
                 'efficitur eros. Maecenas quis ipsum elit. Proin euismod risus ' \
                 'dolor, eget mattis eros hendrerit non. Nullam euismod tincidunt ' \
                 'luctus. Cras blandit enim felis. Curabitur ante est, ' \
                 'sollicitudin eu sodales vitae, consectetur ac libero. Vivamus ' \
                 'dignissim tempus vehicula. Suspendisse a imperdiet felis. ' \
                 'Phasellus vestibulum vestibulum ornare. Proin facilisis pretium ' \
                 'ex, ac interdum quam placerat sit amet. Duis gravida mi in risus ' \
                 'volutpat varius. \n' \
                 'Mauris luctus gravida metus eget euismod. Vestibulum quis ' \
                 'dolor eget nulla sagittis facilisis sit amet vel libero. Sed ' \
                 'condimentum arcu eu leo tristique porta non vel sem. Maecenas ' \
                 'sit amet feugiat odio. Phasellus faucibus ultrices leo, sit ' \
                 'amet imperdiet neque ullamcorper nec. Lorem ipsum dolor sit ' \
                 'amet, consectetur adipiscing elit. Curabitur consequat lectus ' \
                 'a faucibus fermentum. '

        encoded_data, tree = huffman_encoding(string)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) <
                        sys.getsizeof(string)
                        and decoded_data == string)

    def test_one_char(self):
        string = 'b'
        encoded_data, tree = huffman_encoding(string)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) <
                        sys.getsizeof(string)
                        and decoded_data == string)

    def test_one_char_repeated(self):
        string = 'bbbbbbbbbbb'
        encoded_data, tree = huffman_encoding(string)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) <
                        sys.getsizeof(string)
                        and decoded_data == string)


suite_loader = unittest.TestLoader()
suite = suite_loader.loadTestsFromTestCase(HuffmanCodingTest)
unittest.TextTestRunner(verbosity=2).run(suite)


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node



class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffix_list = set()
        
        if self.is_word:
            suffix_list.add(suffix)
        
        if not self.children:
            return suffix_list

        for (char, child) in self.children.items():
            if child.suffixes(suffix + char):
                suffix_list = child.suffixes(suffix + char) | suffix_list
        
        return suffix_list


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# My tests
prefixNode = MyTrie.find('a')
assert(prefixNode.is_word is False)
assert({'ntonym', 'ntagonist', 'nt', 'nthology'} == prefixNode.suffixes())

prefixNode = MyTrie.find('ant')
assert(prefixNode.is_word is True)
assert({'', 'onym', 'agonist', 'hology'} == prefixNode.suffixes())

prefixNode = MyTrie.find('antagonis')
assert not (prefixNode.is_word is True)
assert({'t'} == prefixNode.suffixes())

prefixNode = MyTrie.find('ohhh')
assert (not prefixNode)

prefixNode = MyTrie.find('triumph')
assert (not prefixNode)

prefixNode = MyTrie.find('trigonometry')
assert (prefixNode.is_word is True)
assert({''} == prefixNode.suffixes())

prefixNode = MyTrie.find('')
assert (prefixNode.is_word is False)
assert({'fun', 'trigger', 'anthology',
        'antonym', 'ant', 'factory',
        'trigonometry', 'antagonist', 'tripod',
        'function', 'trie'} == prefixNode.suffixes())





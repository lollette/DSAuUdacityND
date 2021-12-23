# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, default_handler):
        # Initialize the trie with an root node and a handler, this is the root
        # path or home page node
        self.root = RouteTrieNode()
        self.root.handler = default_handler

    def insert(self, parts_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of
        # this path

        current_node = self.root

        for part in parts_list:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, parts_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root

        for part in parts_list:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one
# additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, part):
        # Insert the node as before
        self.children[part] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, default_handler, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(default_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts_list = self.split_path(path)
        self.trie.insert(parts_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        parts_list = self.split_path(path)
        handler = self.trie.find(parts_list)
        if handler:
            return handler
        return self.not_found_handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        parts = path.split('/')

        if parts[0] != "" or not path:
            return self.not_found_handler

        parts_list = []

        for part in parts:
            if part != "":
                parts_list.append(part)

        return parts_list


# Here are some test cases and expected outputs you can use to test your
# implementation

# create the router and add a route

router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'


# My tests

router.add_handler("//classroom.udacity.com/nanodegrees/nd256/parts/"
                   "da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/"
                   "bd252a0b-e9e7-473b-bcc1-bc7e3153568b/lessons/"
                   "8ec390d0-e99d-44c0-88f9-f8f9faf467fc/concepts/"
                   "8a8492a5-f76d-4dcc-a07c-3e2a2ca9b3c6",
                   "HTTPRouter using a Trie handler")  # add a route

router.add_handler("/home/about/me/cv", "cv handler")
print(router.lookup("/home/about/me"))  # should print 'not found handler'
print(router.lookup("/home/about/me/cv/"))  # should print 'cv handler'
print(router.lookup(""))  # should print 'not found handler'
print(router.lookup("home/about"))  # should print 'not found handler'
print(router.lookup("//classroom.udacity.com/nanodegrees/nd256/parts/"
                   "da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/"
                   "bd252a0b-e9e7-473b-bcc1-bc7e3153568b/lessons/"
                   "8ec390d0-e99d-44c0-88f9-f8f9faf467fc/concepts/"
                   "8a8492a5-f76d-4dcc-a07c-3e2a2ca9b3c6"))  # should print 'HTTPRouter using a Trie handler'










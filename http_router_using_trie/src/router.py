"""
Implements trie node
"""
class RouteTrieNode:
    def __init__(self, value, handler):
        self.value = value
        self.handler = handler
        self.children = []

    def insert(self, value):
        for c in self.children:
            if c.value == value:
                return c
        child = RouteTrieNode(value)
        self.children.append(child)
        return child

"""
Implements the trie data structure
"""
class RouteTrie:
    def __init__(self, handler, not_found_handler):
        self.not_found_handler = not_found_handler
        self.root = RouteTrieNode("/", handler)

    def insert(self, start_node, handler, path):
        if len(path) == 0:
            return
        found = False
        element = path.pop(0)
        for c in start_node.children:
            if c.value == element:
                found = True
                break
        if not found:
            # Assign the holder when all elements present in list: path is exhausted
            c = RouteTrieNode(element, handler if len(path) == 0 else self.not_found_handler)
            start_node.children.append(c)
        return self.insert(c, handler, path)

    def find(self, start_node, path):
        if len(path) == 0:
            if len(start_node.children) == 0:
                return start_node.handler
            else:
                return start_node.handler
        else:
            found = False
            element = path.pop(0)
            if len(path) == 1 and path[0] == '':
                path.pop(0)
            for c in start_node.children:
                if c.value == element:
                    found = True
                    break
            if not found:
                return start_node.handler
            else:
                return self.find(c, path)


"""
The Router class will wrap the Trie and handle
"""
class Router:
    def __init__(self, root_handler, not_found_handler):
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        self.route_trie = None

    def add_handler(self, path, handler):
        if self.route_trie is None:
            self.route_trie = RouteTrie(self.root_handler, self.not_found_handler)
        self.route_trie.insert(self.route_trie.root, handler, self.split_path(path))

    def lookup(self, path):
        if not path.startswith('/'):
            raise Exception('URL is invalid as it does not start with /')
        if path == "/":
            return self.root_handler
        else:
            return self.route_trie.find(self.route_trie.root, self.split_path(path))

    def split_path(self, path):
        return path[1:].split('/')

if __name__ == '__main__':
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")  # add a route
    print(router.lookup("/"))
    print(router.lookup("/home"))
    print(router.lookup("/home/about/"))
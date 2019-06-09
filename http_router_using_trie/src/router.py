import unittest
"""
Implements trie node
"""
class RouteTrieNode:
    def __init__(self, value, handler):
        self.value = value
        self.handler = handler
        self.children = []

    def insert(self, value, handler):
        for c in self.children:
            if c.value == value:
                return c
        child = RouteTrieNode(value, handler)
        self.children.append(child)
        return child

"""
Implements the trie data structure
"""
class RouteTrie:
    """
    Parameters:
        handler: Reference to handler for root node
        not_found_handler: Reference to handler that gets invoked when page is not found
    """
    def __init__(self, handler, not_found_handler):
        self.not_found_handler = not_found_handler
        self.root = RouteTrieNode("/", handler)

    """
    Parameters:
        start_node: Reference to node in trie from where path matching starts
        handler: Handler to be added to leaf node
        path: Path to be added to existing trie structure. This is a 
    """
    def insert(self, start_node, handler, path):
        if len(path) == 0:
            return
        found = False
        # Select leading element in path
        element = path.pop(0)
        # Check whether there is a match with one of the children
        for c in start_node.children:
            if c.value == element:
                found = True
                break
        if not found:
            # Assign the handler when all elements present in list: path is exhausted
            c = start_node.insert(element, handler if len(path) == 0 else self.not_found_handler)
        # Make recursive call
        return self.insert(c, handler, path)

    """
    Parameters:
        start_node: Reference to node in trie from where path matching starts
        path: Individual components of path in a list of string.
            For example /a/b/c will be [a,b,c]
    """
    def find(self, start_node, path):
        if len(path) == 0:
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

    """
    Method to add handler to a path. Path gets added to trie if it doesn't exist
    Parameters:
        path: URL string of the form /a/b/c
    """
    def add_handler(self, path, handler):
        self._validate_path(path)
        if self.route_trie is None:
            self.route_trie = RouteTrie(self.root_handler, self.not_found_handler)
        self.route_trie.insert(self.route_trie.root, handler, self.split_path(path))

    """
    Parameters:
        path: URL string of the form /a/b/c or /a/b/c/
    Returns:
        Handler attached to path
    """
    def lookup(self, path):
        self._validate_path(path)
        if path == "/":
            return self.root_handler
        else:
            return self.route_trie.find(self.route_trie.root, self.split_path(path))

    """
    Method to split the path into individual components. Leading slash is ignored
    Parameters:
        path: URL string of the form /a/b/c or /a/b/c/
    """
    def split_path(self, path):
        return path[1:].split('/')

    def _validate_path(self, path):
        if not path.startswith('/'):
            raise Exception('URL is invalid as it does not start with /')

# unit test class
class TestRouter(unittest.TestCase):
    def test_router_with_invalid_path(self):
        router = Router("root handler", "not found handler")
        with self.assertRaises(Exception) as context:
            router.add_handler("home/about", "about handler")  # URL doesn't have a leading /
            self.assertTrue('URL is invalid as it does not start with /' in context.exception)

    def test_router_with_url_having_trailing_slash(self):
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about/me", "me handler")
        router.add_handler("/home/cooking/recipe", "recipe handler")
        router.add_handler("/home/contact/email", "email handler")
        router.add_handler("/home/contact/facebook", "facebook handler")
        self.assertEqual(router.lookup("/home/cooking/recipe/"), "recipe handler")

    def test_router_with_url_not_having_trailing_slash(self):
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about/me", "me handler")
        router.add_handler("/home/cooking/recipe", "recipe handler")
        router.add_handler("/home/contact/email", "email handler")
        router.add_handler("/home/contact/facebook", "facebook handler")
        self.assertEqual(router.lookup("/home/cooking/recipe"), "recipe handler")

    def test_router_with_url_not_found(self):
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about/me", "me handler")
        router.add_handler("/home/cooking/recipe", "recipe handler")
        router.add_handler("/home/contact/email", "email handler")
        router.add_handler("/home/contact/facebook", "facebook handler")
        self.assertEqual(router.lookup("/home/cooking"), "not found handler")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRouter)
    unittest.TextTestRunner(verbosity=2).run(suite)

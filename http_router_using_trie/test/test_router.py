import unittest
from router import Router

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
        self.assertEqual(router.lookup("/home/cooking/recipe/"), router.lookup("/home/cooking/recipe"))

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
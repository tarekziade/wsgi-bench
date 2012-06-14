from funkload.FunkLoadTestCase import FunkLoadTestCase
import time


class Bench(FunkLoadTestCase):
    def setUp(self):
        self.root = self.conf_get('main', 'url')

    def test_simple(self):
        # just runs indefinitely on the root
        res = self.get(self.root)
        self.assertEquals(res.code, 200)

if __name__ == '__main__':
    import unittest
    unittest.main()

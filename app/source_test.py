from models import Source
import unittest

class TestSource(unittest.TestCase):
    def setUp(self):
        self.new_source=Source('abc','BBC','reliable ready news','www.bbc.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__=='__main__':
    unittest.main()
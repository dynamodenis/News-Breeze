import unittest
from models import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.new_article=Article('cnn','CNN','skjsdjfkd.jpg','killer cat','killer','www.cnn.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__=='__main__':
    unittest.main()
import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the class
    '''
    
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_article = Articles("abc-news","Abc","associated","a 5o year old","https:\/\/abcnews.go.com\/US\/wireStory\/louisiana-man-charged-100-counts-degree-rape-62425650","https:\/\/s.abcnews.com\/images\/US\/mississippi-storm-damage-ap-mo-20190414_hpMain_16x9_992.jpg","2019-04-16T09:36:47Z","The number of tornadoes confirmed over the weekend ha")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        
        
    def test_init(self):
        self.assertEqual(self.new_article.id,"abc-news")
        self.assertEqual(self.new_article.name,"ABC")
        self.assertEqual(self.new_article.author,"associated")
        self.assertEqual(self.new_article.title,"a 5o year old")
        self.assertEqual(self.new_article.description,"abc-news")
        self.assertEqual(self.new_article.url,"https:\/\/abcnews.go.com\/US\/wireStory\/louisiana-man-charged-100-counts-degree-rape-62425650")
        self.assertEqual(self.new_article.urlToImage,"https:\/\/s.abcnews.com\/images\/US\/mississippi-storm-damage-ap-mo-20190414_hpMain_16x9_992.jpg")
        self.assertEqual(self.new_article.publishedAt,"2019-04-16T09:36:47Z")
        self.assertEqual(self.new_article.content,"The number of tornadoes confirmed over the weekend ha")
if __name__ == '__main__':
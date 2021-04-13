import unittest

from twitter import Twitter

if __name__ == '__main__':
    unittest.main()


class TwitterTest(unittest.TestCase):
    def setUp(self):
        self.twitter = Twitter()

    def test_initialization(self):
        self.assertTrue(self.twitter)

    def test_tweet_single_passing(self):
        # When
        self.twitter.tweet('Test message')
        # Then
        self.assertEqual(self.twitter.tweets, ['Test message'])

    def test_tweet_single_failing(self):
        # When
        self.twitter.tweet('Test message')
        # Then
        self.assertEqual(self.twitter.tweets, ['Test messag'])

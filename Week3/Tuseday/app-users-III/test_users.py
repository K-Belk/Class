import unittest
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.User import User


class TestUserClasses(unittest.TestCase):

    def setUp(self):
        self.cheap = FreeUser('Kevin', 'kevin@email.com', '2/29/1904', 'K-Belk')
        self.money = PremiumUser('Rich', 'rich@rich.com', '12/30/2000', 'Money_Money_Money')
        self.basic = User('Zella', 'Zella@email.com', '2/2/2222', 'Zel')

    def test_user_post(self):
        self.basic.new_post()
        self.assertEqual(len(self.basic.post), 1)

    def test_free_user_post_restriction(self):
        self.cheap.new_post()
        self.cheap.new_post()
        self.cheap.new_post()
        self.assertEqual(len(self.cheap.post), 2)

    def test_premium_four_post(self):
        self.money.new_post()
        self.money.new_post()
        self.money.new_post()
        self.money.new_post()
        self.assertEqual(len(self.money.post), 4)

    
if __name__ == '__main__':
    unittest.main()
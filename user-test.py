import unittest
from user import  User
import pyperclip

class TestUser(unnitest.TestCase):
    '''
        Test class that defines the cases for user and credential class behaviours

        Args:
            unittest.TestCase: TestCase Class that helps in creating test cases
    
    '''

    def setUp(self):
        '''
        Setuo method to run before each test case
        '''
        self.new_user = User("Kevin","Munge","kmunge","mashaup")

    def test_init(self):
        '''
        test_init test case if object is properly initialized
        '''
        self.assertEqual(self.new_user.first_name,"Kevin")
        self.assertEqual(self.new_user.last_name,"Munge")
        self.assertEqual(self.new_user.user_name,"kmunge")
        self.assertEqual(self.new_user.password,"mashup")

    def tearDown(self):
        '''
        testDown cleans up after each test case
        '''
        User.user_list = []

    def test_save_user(self):
        '''
        test_save_user test case if new user is saved into the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to test if multiple userscan be saved into our list
        '''
        self.new_user.save_user()
        test_user = User |("Asha","Kibet", "sheraton")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_find_user_by_user_name(self):
        '''
        test if we can search by their username and display their details
        '''
        self.new_user.save_user()
        test_user = User("Kamau","Voke","Brayo")
        test_user.save_user()

        find_user = User.ftest_find_user_by_user_name("Kamau")

        self.assertEqual(find_user.password, test_user.password)

    def test_user_exists(self):
        '''
        test if boolean is returned if user daent exist
        '''
        self.new_user.save_user()
        test_user = User("Noella","Ann","shiko","Kevin")
        test_user.save_user()

        user_exists = User.user_exists("Kevin")

        self.assertTrue(user_exists)



if __name__ == '__main__':
    unittest.main()










































































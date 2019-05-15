import pyperclip
import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    defines test cases for credentials class behaviour

    Args:
        unittest.TestCase: helps in creating  test cases
    '''

    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_credentials = Credentials("Twitter","kmunge","Kumewaka")

    def test_init(self):
        '''
        test if objects are initialized properly
        '''
        self.assertEqual(self.new_credentials.platform,"Twitter")
        self.assertEqual(self.new_credentials.account_user_name,"kmunge")
        self.assertEqual(self.new_credentials.account_password,"Kumewaka")

    def tearDown(self):
        '''
        method that does clean up after each test case
        '''
        Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
        test to check if user credentials are being saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        check if we can save multiple credentials into our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","Kmunge","faceke")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test if user credentials can be removed
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram","kmunge","instapass")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_platform(self):
        '''
        check if user credentials can be found  using platform and displayed
        '''
        self.nnew_credentials.save_credentials()
        test_credentials = Credentials("LinkedIn","kmunge","linkinke")
        test_credentials.save_credentials()

        find_credentials = Credentials.find_by_platform("LinkedIn")

        self.assertEqual(find_credentials.account_user_name,test_credentials.account_user_name)

    def test_credentials_exist(self):
        '''
        check if boolean is returned if searched credentials dont exist
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("youtube","kmunge","youtke")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist("youtube")

        self.assertTrue(credentials_exist)

    def test_display_saved_credentials(self):
        '''
        displays all saved credentials
        '''
        self.assertEqual(Credentials.display_saved_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()

























































































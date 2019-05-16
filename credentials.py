import random
import pyperclip

class Credentials:
    '''
    Class that generates instances of user credentials.

    '''
    credentials_list = []

    def __init__(self,platform,account_user_name,account_password):
        '''
        init__ helps in creating our credentials

        Args:
            platform: New users's platform
            account_user_name : New user account for the platform
            account_password : New user account password for platform
        '''

        self.platform = platform
        self.account_user_name = account_user_name
        self.account_password = account_password

    def save_credentials(self):
        '''
        save_credentials saves credentials into the credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials deletes users credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_platform(cls,platform):
        '''
        Method that displays users platform credentials

        Args:
            platform:platform to search for
        returns:
            credentials that the user saved
        '''

        for credentials in cls.credentials_list:
            if credentials.platform == platform:
                return credentials

    @classmethod
    def credentials_exist(cls, platform):
        '''
        checks if credentials exists form the credentials_list

        Args:
            platform:platform to search if it exists
        Returns:
            Boolean: True or false dependent on existance
        '''
        for credentials in cls.credentials_list:
            if credentials.platform == platform:
                return True
        return False

    @classmethod
    def display_saved_credentials(cls):
        '''
        method to display users saved credentials
        '''
        return cls.credentials_list




























































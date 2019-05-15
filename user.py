import pyperclip

class User:
    '''
    Class that generates new instances of the user
    '''
    user_list = []

    def __init__(self,first_name,last_name,user_name,password):
        '''
        init__helps to define our user's properties

        Args:
            first_name:New contact first name
            last_name:New contact last_name
            user_name:New user's login username
            password:New user's login password
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        Method saves user objects into the user_list
        '''
        User.user_list.append(self)

    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        Method that takes in a user_name and returns the user details that match that user_name

        Args:
            user_name: User_name to search 
        Returns:
            User details that match the search

        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exists(cls, user_name):
        '''
        Method to check if user exists in the user_list

        Args:
            user_name: User_name to search from the user_list
        returns:
            boolean: true or false depending on existance of user
        '''
        for user in cls.user_list:
            if user in cls.user_name == user_name:
                return True
            return False



















































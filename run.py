#!/usr/bin/env python3.6

from user import User
from credentials import Credentials
import random

#user functions
def create_new_user(first_name,last_name,user_name,password):
    '''
    creates new users
    '''
    new_user = User(first_name,last_name,user_name,password)
    return new_user

def save_user(user):
    '''
    saves new user
    '''
    user.save_user

def verify_user(user_name):
    '''
    checks if user exists in user_list ,returns boolean

    '''
    return User.user_exists(user_name)
#credentials Functions
def create_credentials(platform,account_user_name,account_password):
    '''
    allows to create new credentials
    '''
    new_credentials = Credentials(platform,account_user_name,account_password)
    return new_credentials

def save_credentials(credentials):
    '''
    allows to save credentials
    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    allows to delete saved credentials
    '''
    credentials.delete_credentials()

def find_credentials(platform):
    '''
    finding credentials using platform
    '''
    return Credentials.find_by_platform(platform)

def check_existing_credentials(platform):
    '''
    checks if user credentials exists
    '''
    return Credentials.credentials_exist(platform)

def display_credentials():
    '''
    returns all saved credentials
    '''
    return Credentials.display_saved_credentials()


def main():
    print("Yeey! This is your trustes password locker.Enter your name?")
    user_name = input()

    print(f"Hello {user_name}.What is your task ?")
    print('\n')

    while True:
        print("Please Use these short codes to navigates :\n na - Create an account, ex = exit locker app ")

        short_code = input().lower()

        if short_code == 'na':
            print("New Account")
            print("-"*10)

            print("First Name.....")
            first_name = input()

            print("Last Name......")
            last_name = input()

            print("User Name......")
            user_name = input()

            print("Password.......")
            password = input()

            save_user (create_new_user(first_name,last_name,user_name,password))
            print('\n')
            print(f"New Account for {first_name} {last_name } created")
            print(f'hello {first_name }, you successfully logged in!')
            print('\n')
            while True:
                print('use this shortcodes in your progress :\n cc - create new credentials ,dc - delete credentials ,fd - find credentials, ds-dispaly saved credentials,ex - exit')
                short_code = input().lower()
                if short_code == 'ex':
                    print('\n')
                    print(f'Goodbye your credentials are safe  {user_nmae}.')
                    break
                elif short_code == 'fd':
                    print('\n')
                    print('Enter platform to be sought for')
                    search_platform = input()
                    if check_existing_credentials(searchsearch_platform):
                        search_credentials = find_credentials(search_platform)
                        print('\n')
                        print(f"Platform:{search_credentials.platform}")
                        print(f"User Name:{search_credentials.account_user_name}")
                        print(f"Account password :{search_credentials.account_password}")
                        print('\n')
                    else:
                        print('\n')
                        print("That credential does not exist!")
                        print('\n')
                elif short_code == 'ds':
                    if display_credentials():
                        print('\n')
                        print('Here is your saved credentials')
                        print('\n')


                        for credentials in display_credentials():
                            print(f'Platform: {credentials.platform}')
                            print(f'Account user Name:{credentials.account_user_name}')
                            print(f'Account Password:{credentials.account_password}')
                            print('\n')
                        else:
                            print('/n')
                            print('Looks like the details dont exist yet!')
                            print('/n')


                elif short_code == 'dc':

                        print('Please enter the Platform of the credentials you would like to delete')
                        delete_cred = input()
                        if check_existing_credentials(delete_cred):
                            search_credentials = find_credentials(delete_cred)
                            print (f'Are you sure you want to delete the credentials for {search_credentials.platform}')
                            print('\n')
                            print (f'press y for yes and n to cancel')
                            print ('\n')
                            proceed =input().lower()
                            if proceed == 'y':
                                delete_credential(search_credentials)
                                print ('\n')
                                print(f'Credentials have been deleted')
                                print ('\n')
                            elif proceed == 'n':
                                print ('\n')
                                print(f'We have not deleted any credential')
                                print ('\n')
                            else:
                                print ('\n')
                                print ('We cannot understand that shortcode, please use y or n.')
                                print ('\n')
                        else: 
                            print ('\n')
                            print(f'Looks like you do not have that kind of a credential')
                            print ('\n')

                elif short_code == 'cc':

                        print ('\n')
                        print ("New Credentials")
                        print ("-"*10)

                        print("Platform:")
                        platform = input()

                        print("Account user name:")
                        account_user_name = input()

                        while True:
                            print('Please choose an option for entering your password by choosing a short-code! \n mp -enter my password, gp - generate a password for me!')
                            short_code = input().lower()
                            if short_code == 'mp':
                                print("Account Password:")
                                account_password = input()
                                break
                            elif short_code =='gp':
                                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                                account_password = "".join(random.choice(chars) for _ in range(10))
                                break
                            else: 
                                print('Ooops!I did not get that. Please try again!')
                            

                        save_credentials(create_credentials(platform, account_user_name, account_password))
                        print('\n')
                        print(f'New Credentials: {platform } {account_user_name } {account_password}')
                        print('\n')
     

                elif short_code =='ex':

                         print("Have a lovely day!")
                         break

                else:
                     print('\n')
                     print("I really didn't get that. Please use the short codes")
                     print('\n')

if __name__ == '__main__':
     main()




































































































































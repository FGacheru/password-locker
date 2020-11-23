from users import User
from credentials import Credentials

def create_users(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_users(user):
    '''
    Function to save contact
    '''
    users.save_users()
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)
def check_existing_users(username):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.users_exist(number)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()






def create_credentials(account,username1,password1):
    '''
    Function to create a new user
    '''
    new_credentials = Credentials(account,username1,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save contact
    '''
    credentials.save_credentials()
    
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()
    
def find_credentials(username1):
    '''
    Function that finds a user by username and returns the credential
    '''
    return Credentials.find_by_username(username1)
def check_existing_credentials(username1):
    '''
    Function that check if a user exists with that username1 and return a Boolean
    '''
    return Credentials.credentials_exist(username)

def display_credentials():
    '''
    Function that returns all the saved users
    '''
    return Credentials.display_credentials()



from users import User
from credentials import Credentials
def create_user(account,username,password):
    '''
    creating new user
    '''
    new_users = User(username,password)
    return new_users
def  save_users(users):
    users.save_users()
def create_credentials (account,username1,password1):
    new_credentials = Credentials(account,username1,password1)
    return new_credentials
def save_credentials(credentials):
    credentials.save_credentials()
def delete_credentials(Credentials):
  Credentials.delete_credentials()
def find_credentials(account):
    return  Credentials.find_by_account(account)
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
def check_existing_credentials(account):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(account)
def main():
    print("Hello! Welcome to an application that help you manage your credentials")
    print('Use the these commands to proceed: CA = create account,' )
    short_code = input().lower()
    if short_code == 'ca':
        print('Enter new account details')
        print('*' * 100)
        account = input('Enter account: ')
        username = input('Enter Username: ')
        while True:
            print('use :  MP = to Enter your password manually')
            password_choice = input().lower()
            if password_choice == 'mp':
                password = input('Enter Password:')
                break
            else:
                print('Invalid short code.Please try again')
            save_user(create_user(username, password))
        print('*' * 100)
        print(f'Welcome {username} to your new account your password is <--- {password} --->')
        print('*' * 100)
    while True:
        print('Use these short codes to manage credentials: \n NC = new credential, \n VC = display credentials,\n SC =     find credential  \n Dc = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credential Details')
            print('*' * 100)
            account = input('Account Name : ')
            username1 = input('Username : ')
            while True:
                print('Use: MP = manually enter password?')
                password_choice = input().lower()
                if password_choice == 'mp':
                    password = input('Enter password : ')
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_credentials(create_credentials(account, username1,password))
            print('*' * 100)
            print(f'Your {account} account has been saved')
            print('*' * 100)
        elif short_code == 'vc':
            if display_credentials():
                print('Your saved credentials are:')
                for account in display_credentials():
                    print('*' * 100)
                    print(f' Username: {username1} \n Password: {password}')
                    print('*' * 100)
            else:
                print('*' * 100)
                print('You have No Credentials. Please Create One')
                print('*' * 100)
        elif short_code == 'dc':
            print('Enter Account name to delete...')
            # name = input('Acount Name : ')
            print('*' * 100)
            if find_credentials(name):
                name_result = find_credentials(name)
                name_result.delete_credentials()
                print(f'Account {name} has been successfully deleted ')
                print('*' * 100)
            else:
                print('Incorrect account name')
                print('*' * 100)
        elif short_code == 'sc':
            print('Enter Account Name To Search...')
            search = input('Account Name : ')
            print('*' * 100)
            if find_credentials(search):
                search = find_credentials(search)
                print(f'Account Name: {search} ')
                print('*' * 100)
            else:
                print('Credentials does not exist')
                print('*' * 100)
        elif short_code == 'ex':
            print('Goodbye')
            print('*' * 100)
            break
        else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
if __name__ == '__main__':
    main()
    
    
from users import User
from credentials import Credentials
def create_user(account,username,password):
    '''
    creating new user
    '''
    new_user = User(account,username,password)
    return new_users
def  save_users(users):
    user.save_users()
def create_credentials (account,username1,password1):
    new_credential = Credentials(account,username1,password1)
    return new_credentials
def save_credentials(credentials):
    credentials.save_credentials()
def delete_credentials(Credentials):
  Credentials.delete_credentials()
def find_credentials(account):
    return  Credentials.find_by_account(account)
def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()
def check_existing_credentials(account):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(account)
def main():
    print("Hi! welcome to an application that help you manage your credentials")
    print('Welcome to Password Locker. Use the these commands to proceed: CA = create account,' )
    short_code = input().lower()
    if short_code == 'ca':
        print('Enter new account details')
        print('*' * 100)
        username = input('Enter Username: ')
        while True:
            print('use :  MP = to manually enter your own password')
            password_choice = input().lower()
            if password_choice == 'mp':
                password = input('Enter Password: ')
                break
            else:
                print('Invalid short code. Please try again')
            save_users(create_user(account,username, password))
        print('*' * 100)
        print(f'Welcome {username} your password is <--- {password} --->')
        print('*' * 100)
    while True:
        print('Use these short codes to manage credentials: \n NC = new credential, \n VC = display credentials,\n SC =     find credential  \n Dc = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credentials Details')
            print('*' * 100)
            account = input('Account Name : ')
            username1 = input('Username : ')
            while True:
                print('Use: MP = manually enter password?')
                password_choice = input().lower()
                if password_choice == 'mp':
                    password = input('Enter password : ')
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_credentials(create_credentials(account, username1,password1))
            print('*' * 100)
            print(f'Your {account} account has been saved')
            print('*' * 100)
        elif short_code == 'vc':
            if display_credentials():
                print('Your saved credentials are:')
                for account in display_credentials():
                    print('*' * 100)
                    print(f' Name: {account} \n Username: {username1} \n Password: {password}')
                    print('*' * 100)
            else:
                print('*' * 100)
                print('You have No Credentials. Please Create One')
                print('*' * 100)
        elif short_code == 'dc':
            print('Enter Account name to delete...')
            name = input('Acount Name : ')
            print('*' * 100)
            if find_credentials(name):
                name_result = find_credentials(name)
                name_result.delete_credentials()
                print(f'Account {name} has been successfully deleted ')
                print('*' * 100)
            else:
                print('Incorrect account name')
                print('*' * 100)
        elif short_code == 'sc':
            print('Enter Account Name To Search...')
            search = input('Account Name : ')
            print('*' * 100)
            if find_credentials(search):
                search = find_credentials(search)
                print(f'Account Name: {search} ')
                print('*' * 100)
            else:
                print('Credentials does not exist')
                print('*' * 100)
        elif short_code == 'ex':
            print('Goodbye')
            print('*' * 100)
            break
        else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
if __name__ == '__main__':
    main()



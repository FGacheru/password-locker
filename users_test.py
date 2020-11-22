import unittest 
from users import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestUser: TestUser class that helps in creating test cases
    '''

    # Items up here .......
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_users = User("Frank","23456789") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_users.username,"Frank")
        self.assertEqual(self.new_users.password,"23456789")


    
    def test_save_users(self):
        '''
        test_save_user test case to test if the users object is saved into
         the user list
        '''
        self.new_users.save_users() # saving the new contact
        self.assertEqual(len(User.user_list),1)
        
        # Items up here...

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_users.save_users()
        test_users = User("Test","users",23456789) # new contact
        test_users.save_users()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
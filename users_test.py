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


if __name__ == '__main__':
    unittest.main()
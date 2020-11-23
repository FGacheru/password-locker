import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCredentials: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Franck","9751","instagram") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.username1,"Franck")
        self.assertEqual(self.new_credentials.password1,"9751")
        self.assertEqual(self.new_credentials.account,"instagram")
        
    def test_save_credentials(self):
        '''
        test_save_credentialstest case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)
       
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
       
        
    def test_save_multiple_credentials(self):
         '''
         test_save_multiple_credentials to check if we can save multiple credentials
         objects to our credentials_list
         '''
         self.new_credentials.save_credentials()
         test_credentials = Credentials("Peter","66820","instagram") # new credentials
         test_credentials.save_credentials()
         self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a contact from our contact list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Peter","66820","instagram") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting credentials object
            self.assertEqual(len(Credentials.credentials_list),1)
            
    def test_find_credentials_by_username1(self):
            '''
            test to check if we can find a contact by phone number and display information
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials("Peter","66820","instagram") # new contact
            test_credentials.save_credentials()

            found_credentials = Credentials.find_by_username1("Peter")

            self.assertEqual(found_credentials,test_credentials)
            
    def test_credentials_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the contact.
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials("Peter","66820","instagram") # new contact
            test_credentials.save_credentials()

            credentials_exists = Credentials.credentials_exist("Peter")

            self.assertTrue(credentials_exists)    
            
    def test_display_all_credentials(self):
           '''
           method that returns a list of all contacts saved
           '''

           self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list) 
if __name__ == '__main__':
    unittest.main()   
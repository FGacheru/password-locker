class Credentials:
    """
    Class that generates new instances of credentials
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,username1,password1,account):

      
         self.username1 = username1
         self.password1 = password1
         self.account = account

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_by_username1(cls,username1):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credentials in cls.credentials_list:
            if credentials.username1 == username1:
                return credentials
        
    @classmethod
    def credentials_exist(cls,username1):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credentials in cls.credentials_list:
            if credentials.username1 == username1:
                    return True

        return False 
    
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
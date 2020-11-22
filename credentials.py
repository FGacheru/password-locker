class Credentials:
    
    """
    Class that generates new instances of the user
    """

    credentials_list = []
    
     # Init method up here
    def save_credentials(self):

        '''
        save_credentials method saves credential objects into credentials_list
        '''

        Credentials.crediantials_list.append(self)
 

class User:

    """
    Class that generates new instances of the user
    """

    user_list = []
    
    def __init__(self,username,password):
        
        self.username = username
        self.password = password

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New users username.
            password : New users password.
        '''



class User:

    """
    Class that generates new instances of the user
    """

    user_list = []
    
     # Init method up here
    def save_users(self):

        '''
        save_user method saves users objects into user_list
        '''

        User.user_list.append(self)

    
    def __init__(self,username,password):
        
        self.username = username
        self.password = password

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New users username.
            password : New users password.
        '''

    def delete_users(self):

        '''
        delete_users method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)    

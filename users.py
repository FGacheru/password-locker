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
        
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in the username and returns a user that matches that username.

        Args:
            username: username to search for
        Returns :
            User of person that matches the username.
        '''

        for users in cls.user_list:
            if users.username == username:
                return users  
            
    @classmethod
    def users_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for users in cls.user_list:
            if users.username == username:
                    return True

        return False             

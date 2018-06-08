from social_django.middleware import SocialAuthExceptionMiddleware

class UserStateDoesNotExistMiddleware(SocialAuthExceptionMiddleware):
    '''
        No need to override get_message() as the UserStateDoesNotExistException
        already includes a useful message to the user.
    '''
    def raise_exception(self, request, exception):
        '''
            By default, the SocialAuthExceptionMiddleware checks if this function
            returns True to check whether it should raise the exception or not.
            It also checks if the current strategy == None, but that's never been
            the case in my testing.
            If the raise_exception() function returns True, the exception is raised.
            This doesn't happen with DEBUG=False, however it's not very useful when I
            need to test if this middleware is working.
        '''
        return False

from social_core.exceptions import AuthException

class UserStateNotPresentException(AuthException):
    def __str__(self):
        return "You must be an administrator, staff member or a student to sign in."

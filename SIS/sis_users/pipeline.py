from sis_users.models import UserState
from sis_users.exceptions import UserStateNotPresentException

def user_state_exists(backend, details, response, *args, **kwargs):
    email = details['email']
    try:
        UserState.objects.get(
            email=email
        )
    except UserState.DoesNotExist:
        raise UserStateNotPresentException(backend)

from social_core.exceptions import AuthForbidden
from sis_users.models import UserState

def user_state_exists(backend, details, response, *args, **kwargs):
    email = details['email']
    try:
        UserState.objects.get(
            email=email
        )
    except UserState.DoesNotExist:
        raise AuthForbidden(backend)

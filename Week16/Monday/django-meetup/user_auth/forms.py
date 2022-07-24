from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class UserAuthenticationForm(AuthenticationForm):
    pass

class UserSignupForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'test']
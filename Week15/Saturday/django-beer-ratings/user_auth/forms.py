from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserAuthenticationForm(AuthenticationForm):
    pass

class UserSignupForm(UserCreationForm):
    pass
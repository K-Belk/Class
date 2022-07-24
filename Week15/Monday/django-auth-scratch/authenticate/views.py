from django.shortcuts import render, redirect, reverse
from .forms import SignUpUserForm

def signup_user(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_posts'))
    else:
        form = SignUpUserForm()
        return render(request, 'authenticate/sign-up.html', {'form': form})
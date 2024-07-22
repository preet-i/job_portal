from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout
from .forms import UserRegistrationForm, EmployeeLoginForm 

def signup(request):
    next_url = request.GET.get('next', '/')
    form = UserRegistrationForm(request.POST or None)
    
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        if new_user is not None:
            auth_login(request, new_user)
            return redirect(next_url)
    
    context = {'form': form}
    return render(request, "accounts/signup.html", context)


def employee_login(request):
    form = EmployeeLoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                 
            else:
                print("Invalid login credentials")
        return redirect('jobs:job-listing')
    
    else:
        form = EmployeeLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')

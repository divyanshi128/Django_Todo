from django.shortcuts import render, redirect
from user_side.models import Todo
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# ====================================== LOGIN =====================================

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                
                if user.is_staff:
                    auth.login(request, user)
                    return redirect('admin_dashboard')
                
                auth.login(request, user)
                return redirect('dashboard')
                
            else:                
                messages.error(request, "Invalid Password")
                return redirect("login")
            
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")

    return render(request, 'accounts/login.html')

# ====================================== LOGOUT ====================================

@login_required(login_url="login")
def logout(request):
     auth.logout(request)
     return redirect("login")

# ====================================== REGISTER ==================================

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        messages.success(request, "Account created successfully")
        return redirect("login")
    
    return render(request, 'accounts/register.html')
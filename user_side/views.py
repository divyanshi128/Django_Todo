from django.shortcuts import render, redirect
from user_side.models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# ====================================== HOME ====================================

def home(request):
    return render(request, 'user_side/home.html')

# ====================================== DASHBOARD ====================================

@login_required(login_url="login")
def dashboard(request):
    
    todos = Todo.objects.filter(user=request.user)
    
    parameters = {
        "todos": todos
    }
        
    return render(request, "user_side/dashboard.html", parameters)

# ====================================== ADD TODO ====================================

@login_required(login_url="login")
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        
        if not title or not description:
            messages.error(request, "Please fill all the fields")
            return redirect("add_todo")
        
        Todo.objects.create(
            title=title,
            description=description,
            priority=priority,
            user=request.user
        )
        
        messages.success(request, "Todo added successfully")
        
        return redirect("dashboard")
    
    return render(request, "user_side/add_todo.html")

# ====================================== DELETE TODO ====================================

@login_required(login_url="login")
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    
    if todo.user == request.user:
        todo.delete()
        
        messages.success(request, "Todo deleted successfully")
        
        return redirect("dashboard")
    
    return redirect("dashboard")

# ====================================== EDIT TODO ====================================

@login_required(login_url="login")
def edit_todo(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        
        if not title or not description:
            messages.error(request, "Please fill all the fields")
            return redirect("edit_todo", id)
        
        todo.title = title
        todo.description = description
        todo.priority = priority
        todo.save()
        
        messages.success(request, "Todo updated successfully")
        
        return redirect("dashboard")
    
    parameters = {
        "todo": todo
    }
    
    return render(request, "user_side/edit_todo.html", parameters)

# ====================================== MY PROFILE ====================================

@login_required(login_url="login")
def my_profile(request):
    user = User.objects.get(id=request.user.id)
    
    parameters = {
        "user": user
    }
    
    return render(request, "user_side/my_profile.html", parameters)

# ====================================== CHANGE PASSWORD ====================================

@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not old_password or not new_password or not confirm_password:
            messages.error(request, "Please fill all the fields")
            return redirect("change_password")
        
        if not request.user.check_password(old_password):
            messages.error(request, "Old password is incorrect")
            return redirect("change_password")
        
        if new_password != confirm_password:
            messages.error(request, "New password and confirm password do not match")
            return redirect("change_password")
        
        request.user.set_password(new_password)
        request.user.save()
        
        messages.success(request, "Password changed successfully")
        return redirect("logout")
    
    return render(request, "user_side/change_password.html")


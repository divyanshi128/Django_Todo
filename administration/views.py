from django.shortcuts import render, redirect
from user_side.models import Todo
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url="login")
@staff_member_required
def admin_dashboard(request):
    
    # get the number of todos each user has
    
    users = User.objects.all()
    
    user_todo_count = []
    
    for user in users:
        todos = Todo.objects.filter(user=user)
        user_todo_count.append({
            "user": user,
            "todo_count": len(todos)
        })
        
    parameters = {
        "user_todo_count": user_todo_count
    }
    return render(request, 'administration/admin_dashboard.html', parameters)

# ====================================== DELETE USER ==================================

@login_required(login_url="login")
@staff_member_required
def delete_user(request, user_id):
    
    user = User.objects.get(id = user_id)
    user.delete()
    
    return redirect("admin_dashboard")
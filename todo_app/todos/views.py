from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo
from django.views import View
from django.contrib.auth.models import User

class Home(View):
    def get(self, request):
        return render(request, 'home.html')  # Render the home template

def register(request):
    username_taken = False  # Default value for the context variable
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            username_taken = True  # Set this to True if username is taken
            messages.error(request, 'Username already exists.')  # Show error message
        elif password == password_confirm:
            # Create the user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html', {'username_taken': username_taken})  # Pass the context variable

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            return redirect('todos')  # Redirect to the todo list after login
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')

 

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list(request):
    # Fetch the todos for the logged-in user
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title:  # Ensure the title is provided
            todo = Todo.objects.create(user=request.user, title=title, description=description)
            todo.save()
            messages.success(request, 'To-Do added successfully!')
            return redirect('todos')  # Redirect to the to-do list after adding a todo
        else:
            messages.error(request, 'Title is required.')
    
    return render(request, 'add_todo.html')


@login_required
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todos')  # Redirect to the todo list after editing a todo
    return render(request, 'edit_todo.html', {'todo': todo})

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todos')  # Redirect to the todo list after deleting a todo







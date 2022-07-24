from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def get_todo(todo_id):
    return Todo.objects.get(id=todo_id)

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_new(request):
    todo = TodoForm(request.POST or None)
    if todo.is_valid():
        todo.save()
        return redirect('todos:todo_list')
    return render(request, 'todos/todo_new.html', {'todo': todo})

def todo_show(request, todo_id):
    todo = get_todo(todo_id)
    return render(request, 'todos/todo_show.html', {'todo': todo})

def todo_update(request, todo_id):
    todo = TodoForm(request.POST or None, instance=get_todo(todo_id))
    if todo.is_valid():
        todo.save()
        return redirect('todos:todo_show', todo_id)
    return render(request, 'todos/todo_update.html', {'todo': todo})


def todo_delete(request, todo_id):
    todo = get_todo(todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:todo_list')
    return render(request, 'todos/todo_delete.html', {'todo': todo})
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        todo_title = request.POST.get("todo_title")
        todo_description = request.POST.get("todo_description")
        Todo.objects.create(title=todo_title, description=todo_description)
        return redirect(request.path)
    todos = Todo.objects.all()
    context['todos'] = todos
    return render(request, "todo_app/index.html", context)

def delete_todo(request, id):
    Todo.objects.get(pk=id).delete()
    return redirect("home")

def update_todo(request, id):
    todo_item = Todo.objects.get(pk=id)
    context = {}
    if request.method == "POST":
        todo_title = request.POST.get("todo_title")
        todo_description = request.POST.get("todo_description")
        todo_item.title = todo_title
        todo_item.description = todo_description
        todo_item.save()
        return redirect("home")
    context["todo_item"] = todo_item
    return render(request, "todo_app/update.html", context)
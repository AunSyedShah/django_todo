from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoModelForm


# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        if "todo_insert_submit_button" in request.POST:
            form = TodoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(request.path)
        elif "is_completed_field" in request.POST:
            todo_object_id = request.POST.get("is_completed_field")
            todo_object = Todo.objects.get(pk=todo_object_id)
            current_status = todo_object.is_completed
            if current_status:
                todo_object.is_completed = False
            else:
                todo_object.is_completed = True
            todo_object.save()
    todos = Todo.objects.all()
    context["todos"] = todos
    context["form"] = TodoModelForm()
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


def is_checked(request, id):
    todo = Todo.objects.get(pk=id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return JsonResponse({"data": todo.is_completed})

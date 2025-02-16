from django.shortcuts import render, redirect, get_object_or_404
from todo_list.models import Task, Tag
from todo_list.forms import TaskForm, TagForm


def home(request):
    tasks = Task.objects.prefetch_related("tags").order_by("is_done", "-created_at")
    return render(request, "home.html", {"tasks": tasks})


def tag_list(request):
    tags = Tag.objects.prefetch_related("tasks").all()
    return render(request, "tags.html", {"tags": tags})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list:home")
    else:
        form = TaskForm()
    return render(request, "add_task.html", {"form": form})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list:tag_list")
    else:
        form = TagForm()
    return render(request, "add_tag.html", {"form": form})


def update_task(request, pk):
    task = get_object_or_404(Task.objects.prefetch_related("tags"), pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo_list:home")
    else:
        form = TaskForm(instance=task)
    return render(request, "edit_task.html", {"form": form, "task": task})


def update_tag(request, pk):
    tag = get_object_or_404(Tag.objects.prefetch_related("tasks"), pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("todo_list:tag_list")
    else:
        form = TagForm(instance=tag)
    return render(request, "edit_tag.html", {"form": form, "tag": tag})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("todo_list:home")


def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect("todo_list:tag_list")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo_list:home")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from authentication.models import User
from .models import Item

from .forms import NewItemForm, CategoryForm


@login_required
def list(request):
    """
    Get a list of users task items and display them.
    """
    form = CategoryForm()

    items = Item.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.data['category']
            items = Item.objects.filter(user=request.user, category=category)
            return render(request, 'items/items.html', {'items': items, 'user': request.user, 'form': form})
    else:
        return render(request, 'items/items.html', {'items': items, 'user': request.user, 'form': form})


@login_required
def add_item(request, error=False):
    """
    Add a new item to a users personal list.
    """
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            # form = NewItemForm()
            return redirect('list')
        else:
            error = True
            return render(request, 'items/new_item_form.html', {'form': form, 'user': request.user, 'error': error})
    else:
        form = NewItemForm()
        return render(request, 'items/new_item_form.html', {'form': form, 'user': request.user, 'error': error})


@login_required
def complete_task(request, pk):
    """
    View to mark a task item as complete.
    """
    item = Item.objects.get(pk=pk)
    if item.user == request.user:
        item.is_completed = True
        item.save()
        return redirect('list')
    else:
        return HttpResponse('Not permitted.')


@login_required
def delete_task(request, pk):
    """
    View to delete a task from the db.
    """
    item = Item.objects.get(pk=pk)
    if item.user == request.user:
        item.delete()
        return redirect('list')
    else:
        return HttpResponse('Not permitted.')
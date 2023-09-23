from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import NewItemForm, EditItemForm
from .models import Category, Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_reserved=False).exclude(pk=item.pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('item:detail', pk=item.pk)
    else:
        form = NewItemForm()
    
    return render(request, 'item/new.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required
def edit(request, pk):
        
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        print("post")
        if form.is_valid():
            print('valid')
            item.save()
            
            return redirect('item:detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/new.html', {
        'form': form,
        'title': 'Edit Item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
  
    return render(request, 'item/deleteConfirmation.html',{
        'item': item
        })

@login_required
def deleteComfirmed(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')
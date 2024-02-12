from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Item
from .forms import NewItemForm, EditItemForm


def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.all()

    if query:
        items = items.filter(name__icontains=query)

    # Order the items by the created_at field in descending order (newest first)
    items = items.order_by('-created_at')

    return render(request, 'items/items.html', {
        'items': items,
        'query': query
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/detail.html', {'item': item})


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'New item',
    })


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = EditItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'Edit item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()

    return redirect('core:index')

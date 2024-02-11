from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Item
from .forms import NewItemForm, EditItemForm


def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(name__icontains=query)

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

            return redirect('/', pk=item.id)
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
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })


@login_required
def delete(request, pk):
    pass
    # item = get_object_or_404(Item, pk=pk)
    # item.delete()

    # return redirect('dashboard:index')

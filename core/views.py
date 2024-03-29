from django.shortcuts import render, redirect
from .models import Item
from .forms import SignUpForm


def index(request):
    items = Item.objects.all()
    ordered_items = items.order_by('-created_at')
    return render(request, 'core/index.html', {
        'items': ordered_items
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form

    })

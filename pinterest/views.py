from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from pins.models import Pin


@login_required
def home(request):
    pins = Pin.objects.all().order_by('?')[:100]
    context = {'pins':pins}
    return render(request, 'home.html', context)


@login_required
def search(request):
    query = request.GET.get('q')

    q = Q(title__icontains=query) | Q(description__icontains=query) | Q(user__username__icontains=query)
    pins = Pin.objects.filter(
        q
        # title__icontains=query,
        # description__icontains=query
        
        ).all()
    context = {'pins':pins[:100]}
    return render(request, 'home.html', context)
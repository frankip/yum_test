from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login

from .models import Details
from .forms import FeedBackForm

# Create your views here.
@login_required
def list_details(request):
    instance = Details.objects.all()
    ctx = {
        'instance': instance
    }
    return render(request, 'index.html', ctx)

@login_required
def add_details(request):
    form  = FeedBackForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance = form.save()
            return redirect('details')
    ctx = {
        'form':form
    }
    return render(request, 'form.html', ctx)
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRigisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def All_Users(request):
    model=User.objects.all()
    return render(request,'base.html',{'model':model})

def Register(request):
    if request.method=='POST':
        form=UserRigisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'account create for {username}')
            return redirect('login')
    else:
        form=UserRigisterForm()
    return render(request,'rigister.html',{'form':form})
@login_required
def Profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
        
    return render (request,'Profile.html',context)
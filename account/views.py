from django.shortcuts import render
from .models import User
from django.shortcuts import redirect
from django.contrib import auth, messages



def login(request):
    content = {}
    try:
        email  = request.POST['email']
        password  = request.POST['password']
    except:
        return render(request,'account/login.html',content)
    
    try:
        user = User.objects.get(UserEmail = email,UserPassword = password)
        request.session['email'] = email
        
        return redirect('/home')
    except:
        content['flag'] = 'faliure'
        return render(request, 'account/login.html',content)
    return render(request,'account/login.html')

def signup(request):
    content = {}
    try:
        email = request.POST['email']
        password = request.POST['password']
    except:    
        return render(request,'account/signup.html',content)

    try:
        user = User(UserEmail = email,UserPassword = password)
        user.save()
        content['flag'] = 'success'
        return render(request,'account/login.html',content)
    except:
        content['flag'] = 'faliure'
        return render(request,'account/signup.html',content)



def home(request):
    if request.session.get('email', None) == None:
        return render(request,'account/login.html')
    return redirect('/home')


def logout(request):
    if request.session.get('email', None) == None:
        return redirect('/account/login')
    del request.session['email']
    return redirect('/account/login')


def reset_password(request):
    content = {}
    if request.session.get('email', None) == None:
        return redirect('/account/login')
    try:
        old = request.POST['old']
        new = request.POST['new']
        newagain = request.POST['newagain']
        try:
            user = User.objects.get(UserEmail = request.session['email'],UserPassword = old)
            user.UserPassword = new
            user.save()
            content['message'] = 'PasswordChangeSuccess'
            return render(request,'home/index.html',content)
        except:
                content['message'] = 'OldMatchError'
                return render(request,'account/reset_password.html',content)
    except:
        return render(request,'account/reset_password.html')


    
    
    
    


    
    

    
    
    

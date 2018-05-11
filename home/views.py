from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    if request.session.get('email', None) == None:
        return redirect('/account/login')
    return render(request,'home/index.html')
from django.shortcuts import render, redirect
from scripts.AppFunctions import user_access_level, AccessLevel, make_datetime
from josie.settings import SITE_NAME
from django.contrib.auth import authenticate, login, logout
from django.http import request

# Create your views here.
def dashboard(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    
    access: AccessLevel = user_access_level(request)

    if access.is_staff() or access.is_admin():
        ctx['page_heading'] = 'Dashboard'
        ctx['page_title'] = '{} | {}'.format(ctx['page_heading'], SITE_NAME)
        return render(request, 'Panel/dashboard.html', context=ctx)
    else:
        return redirect('/panel/login')

def log_in(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    
    access: AccessLevel = user_access_level(request)

    if access.is_staff() or access.is_admin():
        return redirect('/panel')
    else:
        if request.method == 'POST':
            # Attempt django authentication
            user = authenticate(
                request,
                username=str(request.POST['username']),
                password=str(request.POST['password']), )
            
            # Check if backend authenticated
            if user is not None:
                # Log in the user
                login(request, user)
                # If it did, redirect to panel
                return redirect('/panel')
            else:
                ctx['page_heading'] = 'Log In'
                ctx['page_title'] = '{} | {}'.format(ctx['page_heading'], SITE_NAME)
                ctx['error_message'] = 'Your username or password is incorrect.'
                return render(request, 'Panel/login.html', context=ctx)
        else:
            ctx['page_heading'] = 'Log In'
            ctx['page_title'] = '{} | {}'.format(ctx['page_heading'], SITE_NAME)
            return render(request, 'Panel/login.html', context=ctx)
    

def log_out(request):
    logout(request)
    return redirect('/set-timezone')
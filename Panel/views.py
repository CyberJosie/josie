from django.shortcuts import render, redirect
from scripts.AppFunctions import user_access_level, AccessLevel

# Create your views here.
def panel(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    
    access: AccessLevel = user_access_level(request)

    if access.is_staff() or access.is_admin():
        ctx['page_heading'] = 'Panel Dashboard'
        ctx['page_title'] = '{} | {}'.format(ctx['page_heading'], SITE_NAME)
        return render(request, 'Panel/dashboard.html', context=ctx)
    else:
        return redirect('/panel/login/')

def login(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    
    access: AccessLevel = user_access_level(request)

    if access.is_staff() or access.is_admin():
        return redirect('/panel/')
    else:
        ctx['page_heading'] = 'Log In'
        ctx['page_title'] = '{} | {}'.format(ctx['page_heading'], SITE_NAME)
        return render(request, 'Panel/log_in.html', context=ctx)

def logout(request):
    pass
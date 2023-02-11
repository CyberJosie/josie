import pytz
import json
from django.shortcuts import render, redirect
from josie.settings import SITE_NAME
from scripts.AppFunctions import make_datetime


def set_timezone(request):
    if request.method == 'POST':
        jdata = json.loads(request.body)
        request.session['django_timezone'] = jdata['timezone']
        return redirect('/')

def index(request):
    ctx = {}
    ctx['page_title'] = 'Home | {}'.format(SITE_NAME)
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    return render(request, 'Site/index.html', context=ctx)

def services(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    ctx['page_title'] = 'Services | {}'.format(SITE_NAME)
    return render(request, 'Site/services.html', context=ctx)

def projects(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    ctx['page_title'] = 'Projects | {}'.format(SITE_NAME)
    return render(request, 'Site/projects.html', context=ctx)

def about_me(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    ctx['page_title'] = 'About Me | {}'.format(SITE_NAME)
    return render(request, 'Site/about_me.html', context=ctx)

def contact(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    ctx['page_title'] = 'Contact | {}'.format(SITE_NAME)
    return render(request, 'Site/contact.html', context=ctx)

def portfolio(request):
    ctx = {}
    if 'django_timezone' in request.session:
        ctx['date'], ctx['time'] = make_datetime(request.session['django_timezone'])
    ctx['page_title'] = 'Portfolio | {}'.format(SITE_NAME)
    return render(request, 'Site/portfolio.html', context=ctx)
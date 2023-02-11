from django.shortcuts import render
from josie.settings import SITE_NAME

def index(request):
    ctx = {}
    ctx['page_title'] = 'Home | {}'.format(SITE_NAME)
    return render(request, 'Site/index.html', context=ctx)

def services(request):
    ctx = {}
    ctx['page_title'] = 'Services | {}'.format(SITE_NAME)
    return render(request, 'Site/services.html', context=ctx)

def projects(request):
    ctx = {}
    ctx['page_title'] = 'Projects | {}'.format(SITE_NAME)
    return render(request, 'Site/projects.html', context=ctx)

def about_me(request):
    ctx = {}
    ctx['page_title'] = 'About Me | {}'.format(SITE_NAME)
    return render(request, 'Site/about_me.html', context=ctx)

def contact(request):
    ctx = {}
    ctx['page_title'] = 'Contact | {}'.format(SITE_NAME)
    return render(request, 'Site/contact.html', context=ctx)

def portfolio(request):
    ctx = {}
    ctx['page_title'] = 'Portfolio | {}'.format(SITE_NAME)
    return render(request, 'Site/portfolio.html', context=ctx)
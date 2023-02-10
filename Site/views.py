from django.shortcuts import render
from josie.settings import SITE_NAME

def index(request):
    ctx = {}
    ctx['page_title'] = 'Welcome | Josie'
    return render(request, 'Site/index.html', context=ctx)

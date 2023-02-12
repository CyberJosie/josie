from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Site.urls')),
    path('panel/', include('Panel.urls')),
    # path('blog/', include('Blog.urls')),
]

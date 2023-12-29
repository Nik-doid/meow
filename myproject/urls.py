# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import home,user_login,dashboard,user_logout,register
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static 
from django.contrib.auth.decorators import login_required # Import your home view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('myapp.urls')),
    path('', user_login, name='login'),
    path('dashboard/', login_required(dashboard), name='dashboard'),
    path('dashboard/register/<int:class_id>/', register, name='register'),
    path('home/',login_required(home),name='home'),
    path('logout/', user_logout, name='logout'),

  # Add this line for the root path
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



from django.contrib import admin
from django.urls import path, include
from attendance import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/', include( 'accounts.urls')),
    path('attendance/', include('attendance.urls'))
]

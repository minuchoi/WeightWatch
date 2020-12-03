"""WeightWatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import weightpage.views
import loginpage.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', loginpage.views.displaylogin, name='loginpage'),
                  path('dashboard/<str:variable>', weightpage.views.dashboard, name='dashboard'),
                  path('dashboard/analytics/edit/<int:weight_id>', weightpage.views.edit_info, name='edit_info'),
                  path('dashboard/analytics/delete/<int:weight_id>', weightpage.views.delete_data_page,
                       name='delete_page'),
                  path('dashboard/analytics/delete/deleted/<int:weight_id>', weightpage.views.delete_data,
                       name='delete_data'),
                  path('register', loginpage.views.register, name='register'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

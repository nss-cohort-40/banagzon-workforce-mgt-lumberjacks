from django.urls import path, include
from django.conf import settings
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employee/form', employee_form, name='employee_form'),
    path('computers/', computer_list, name='computer_list'),
    path('departments/', department_list, name='department_list'),
]



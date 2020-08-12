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
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('employees/<int:employee_id>/form/', employee_edit_form, name='employee_edit_form'),
    path('employee/form', employee_form, name='employee_form'),
    path('departments/', department_list, name='department_list'),
    path('computers/', computer_list, name='computer_list'),
    path('training/', training_list, name='training_list'),
    path('departments/form', department_form, name='department_form'),
    path('departments/<int:department_id>/', department_detail, name='department'),
    path('computers/', computer_list, name='computer_list'),
    path('computers/form', computer_form, name='computer_form'),
    path('computers/<int:computer_id>/', computer_details, name='computer')
]

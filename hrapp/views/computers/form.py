import sqlite3
from django.shortcuts import render
from hrapp.models import Computer

def computer_form(request):
    if request.method == 'GET':
        template = 'computers/form.html'
        context = {}

        return render(request, template, context)
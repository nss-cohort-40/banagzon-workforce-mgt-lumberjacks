import sqlite3
from django.shortcuts import render
from hrapp.models import Computer, Employee
from ..connection import Connection
import datetime

def get_employees():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('''
        SELECT
            e.id,
            e.first_name,
            e.last_name
        FROM hrapp_employee e
        ''')

        return db_cursor.fetchall()

def computer_form(request):
    if request.method == 'GET':
        employees = get_employees()
        template = 'computers/form.html'
        context = {
            'all_employees': employees,
            'date': datetime.date.today()
        }

        return render(request, template, context)
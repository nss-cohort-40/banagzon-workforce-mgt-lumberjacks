import sqlite3
from django.shortcuts import render
from hrapp.models import Computer, Employee
from ..connection import Connection

def get_employees():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('''
        SELECT
            e.id,
            e.first_name,
            e.last_name
        ''')

        return db_cursor.fetchall()

def computer_form(request):
    if request.method == 'GET':
        template = 'computers/form.html'
        context = {
            'all_computers': computers
        }

        return render(request, template, context)
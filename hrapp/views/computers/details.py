import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from hrapp.models import Computer
from ..connection import Connection

def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('''
        SELECT
            c.id computer_id,
            c.manufacturer,
            c.make,
            c.purchase_date,
            c.decommission_date
        FROM hrapp_computer c
        WHERE c.id = ?
        ''', (computer_id,))

        return db_cursor.fetchone()

def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)

        template = 'computers/details.html'
        context = {
            'computer': computer
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST
        if ('actual_method' in form_data and form_data['actual_method'] == 'DELETE'):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE from hrapp_computer
                WHERE id = ?
                """, (computer_id,))

            return redirect(reverse('hrapp:computer_list'))
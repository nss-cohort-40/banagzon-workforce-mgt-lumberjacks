import sqlite3
from django.shortcuts import redirect, reverse, render
from hrapp.models import Computer
from ..connection import Connection
import datetime

def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute('''
            SELECT
                c.id,
                c.manufacturer,
                c.make,
                c.purchase_date,
                c.decommission_date
            from hrapp_computer c
            ''')

            all_computers = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                computer = Computer()
                computer.id = row['id']
                computer.manufacturer = row['manufacturer']
                computer.make = row['make']
                computer.purchase_date = row['purchase_date']
                computer.decommission_date = row['decommission_date']

                all_computers.append(computer)

            template = 'computers/list.html'
            context = {
                'all_computers': all_computers
            }

            return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute('''
            INSERT INTO hrapp_computer
            (
                manufacturer, make, purchase_date   
            )
            VALUES (?, ?, ?)
            ''', (form_data['manufacturer'], form_data['make'], form_data['purchase_date']))

            db_cursor.execute('''
            SELECT *
            FROM hrapp_computer
            ORDER BY column
            DESC LIMIT 1
            ''')

            db_cursor.execute('''
            INSERT INTO hrapp_employeecomputer
            (
                employee, computer, assign_date
            )
            VALUES (?, ?, ?)
            ''', (form_data['employee'], form_data['computer'], form_data['assign_date']))

        return redirect(reverse('hrapp:computer_list'))
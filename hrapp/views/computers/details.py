import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from hrapp.models import Computer
from hrapp.models import Employee
from ..connection import Connection

def get_employee_computers(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT ec.id, ec.computer_id, ec.employee_id
        FROM hrapp_employeecomputer ec
        WHERE ec.computer_id = ?
        """, (computer_id,))

        return db_cursor.fetchall()

def create_computer(cursor, row):
    _row = sqlite3.Row(cursor, row)

    computer = Computer()
    computer.id = _row["id"]
    computer.manufacturer = _row["manufacturer"]
    computer.make = _row["make"]
    computer.purchase_date = _row["purchase_date"]
    computer.decommission_date = _row["decommission_date"]

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    employee.is_supervisor = _row["is_supervisor"]
    employee.department_id = _row["department_id"]

    computer.assigned_employee = employee

    return computer

def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_computer
        db_cursor = conn.cursor()

        db_cursor.execute('''
        SELECT
            c.id,
            c.manufacturer,
            c.make,
            c.purchase_date,
            c.decommission_date,
            e.id employee_id,
            e.first_name,
            e.last_name,
            e.start_date,
            e.is_supervisor,
            e.department_id
        FROM hrapp_computer c
        LEFT JOIN hrapp_employeecomputer ec ON ec.computer_id = c.id
        LEFT JOIN hrapp_employee e ON e.id = ec.employee_id
        WHERE c.id = ?
        ''', (computer_id,))

        return db_cursor.fetchone()

def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)

        template = 'computers/details.html'

        if not computer.assigned_employee.id == None:

            context = {
                'computer': computer,
                'is_assigned': True
            }

            return render(request, template, context)

        else:

            context = {
                'computer': computer,
                'is_assigned': False
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
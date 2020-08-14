import sqlite3
from django.shortcuts import render
from hrapp.models import Computer, Employee, EmployeeComputer
from ..connection import Connection
import datetime

def get_employees_without_comp():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        db_cursor = conn.cursor()

        db_cursor.execute('''
        SELECT
            e.id,
            e.first_name,
            e.last_name,
            ec.computer_id,
            ec.unassign_date
        FROM hrapp_employee e
        LEFT JOIN hrapp_employeecomputer ec ON ec.employee_id = e.id
        WHERE ec.unassign_date ISNULL
        ''')

        dataset = db_cursor.fetchall()

        print('DATASET:', dataset)

        employee_dropdown = []

        for (employee) in dataset:
            print('COMPUTER IDS:', employee.computer_id)
            if employee.computer_id is None:
                employee_dropdown.append(employee)

        print('EMPLOYEE_DROPDOWN:', employee_dropdown)
        return employee_dropdown

def computer_form(request):
    if request.method == 'GET':
        employee_dropdown = get_employees_without_comp()
        template = 'computers/form.html'
        context = {
            'employee_dropdown': employee_dropdown
        }

        return render(request, template, context)

def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    employee.id = _row['id']
    employee.first_name = _row['first_name']
    employee.last_name = _row['last_name']

    employee.computer_id = _row['computer_id']
    employee.unassign_date = _row['unassign_date']

    return (employee)
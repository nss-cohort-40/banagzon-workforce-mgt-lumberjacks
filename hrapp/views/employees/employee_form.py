import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Department, Computer
from ..connection import Connection

def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id employee_id,
            e.first_name,
            e.last_name,
            e.start_date,
            e.is_supervisor,
            e.department_id,
            d.name department_name
        FROM hrapp_employee e
        JOIN hrapp_department d ON e.department_id = d.id
        WHERE e.id = ?
        """,(employee_id,))

        return db_cursor.fetchone()

def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)
    supervisor = False
    if "is_supervisor"== 1 in _row:
        supervisor = True

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    employee.is_supervisor = supervisor
    employee.department_id = _row["department_id"]

    department = Department()
    department.id = _row["department_id"]
    department.name = _row["department_name"]

    employee.department = department

    return employee

def get_departments():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.name,
            d.budget
        from hrapp_department d
        """)

        return db_cursor.fetchall()



def employee_form(request):
    if request.method == 'GET':
        departments = get_departments()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)


def employee_edit_form(request, employee_id):

    if request.method == 'GET':
        employee = get_employee(employee_id)
        departments = get_departments()

        template = 'employees/employee_form.html'
        context = {
            'employee': employee,
            'all_departments': departments
        }

        return render(request, template, context)
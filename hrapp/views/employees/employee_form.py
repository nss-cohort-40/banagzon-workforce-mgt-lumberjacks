import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Department, Computer, EmployeeComputer
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
            d.name department_name,
            c.id computer_id,
            c.make,
            c.manufacturer,
            ec.computer_id compid,
            ec.id emp_id
        FROM hrapp_employee e
        JOIN hrapp_department d ON e.department_id = d.id
        left JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
        left JOIN hrapp_computer c ON ec.computer_id = c.id
        WHERE ec.unassign_date ISNULL
        AND e.id = ?
        """,(employee_id,))

        return db_cursor.fetchone()

def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    employee.is_supervisor = _row["is_supervisor"]
    employee.department_id = _row["department_id"]
    employee.emp_id = _row["emp_id"]

    computer = Computer()
    computer.id = _row["compid"]
    computer.make = _row["make"]
    computer.manufacturer = _row["manufacturer"]

    department = Department()
    department.id = _row["department_id"]
    department.name = _row["department_name"]



    employee.computer = computer
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
def get_computers():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.make,
            c.manufacturer,
            c.purchase_date,
            c.decommission_date,
            ec.employee_id,
            ec.computer_id,
            ec.assign_date,
            ec.unassign_date

        from hrapp_computer c
        left join hrapp_employeecomputer ec on c.id = ec.computer_id
        where c.decommission_date ISNULL
        """)

        return db_cursor.fetchall()
    

def get_employee_computers(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            ec.id,
            ec.computer_id,
            ec.employee_id,
            ec.assign_date,
            ec.unassign_date

        from hrapp_employeecomputer ec
        """)

        return db_cursor.fetchall()

def employee_form(request):
    if request.method == 'GET':
        departments = get_departments()
        computers = get_computers()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': departments,
            'all_computers': computers
        }

        return render(request, template, context)


def employee_edit_form(request, employee_id):

    if request.method == 'GET':
        employee = get_employee(employee_id)
        departments = get_departments()
        computers = get_computers()
        employeecomputers = get_employee_computers(employee_id)

        template = 'employees/employee_form.html'
        context = {
            'employee': employee,
            'all_departments': departments,
            'all_computers': computers,
            'employeecomputers': employeecomputers
        }

        return render(request, template, context)
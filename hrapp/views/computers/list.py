import sqlite3
from django.shortcuts import redirect, reverse, render
from hrapp.models import Computer, Employee
from ..connection import Connection
import datetime

def computer_list_by_make(search_keyword):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_computer
        db_cursor = conn.cursor()

        like_string = f'{search_keyword}%'

        db_cursor.execute("""
        SELECT
            c.id computer_id,
            c.manufacturer,
            c.make,
            c.purchase_date,
            c.decommission_date,
            e.id employee_id,
            e.first_name,
            e.last_name
        FROM hrapp_computer c
        LEFT JOIN hrapp_employeecomputer ec ON ec.computer_id = c.id
        LEFT JOIN hrapp_employee e ON e.id = ec.employee_id
        WHERE c.make LIKE ?
        """, (like_string,))

        dataset = db_cursor.fetchall()

        all_computers = {}

        for (computer, employee) in dataset:
            all_computers[computer.id] = computer

        return all_computers

def computer_list_by_manufacturer(search_keyword):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_computer
        db_cursor = conn.cursor()

        like_string = f'{search_keyword}%'

        db_cursor.execute("""
        SELECT
            c.id computer_id,
            c.manufacturer,
            c.make,
            c.purchase_date,
            c.decommission_date,
            e.id employee_id,
            e.first_name,
            e.last_name
        FROM hrapp_computer c
        LEFT JOIN hrapp_employeecomputer ec ON ec.computer_id = c.id
        LEFT JOIN hrapp_employee e ON e.id = ec.employee_id
        WHERE c.manufacturer LIKE ?
        """, (like_string,))

        dataset = db_cursor.fetchall()

        all_computers = {}

        for (computer, employee) in dataset:
            all_computers[computer.id] = computer

        return all_computers

def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_computer
            db_cursor = conn.cursor()

            db_cursor.execute('''
                SELECT
                    c.id computer_id,
                    c.manufacturer,
                    c.make,
                    c.purchase_date,
                    c.decommission_date,
                    e.id employee_id,
                    e.first_name,
                    e.last_name
                FROM hrapp_computer c
                LEFT JOIN hrapp_employeecomputer ec ON ec.computer_id = c.id
                LEFT JOIN hrapp_employee e ON e.id = ec.employee_id;
            ''')

            dataset = db_cursor.fetchall()

            all_computers = {}

            for (computer, employee) in dataset:
                all_computers[computer.id] = computer

            template = 'computers/list.html'
            context = {
                'all_computers': all_computers
            }

            return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if ("actual_method" in form_data and form_data["actual_method"] == "filter_by_make"):
            search_keyword = form_data["make"]
            all_computers = computer_list_by_make(search_keyword)

            template = 'computers/list.html'

            context = {
                'all_computers': all_computers
            }

            return render(request, template, context)

        elif ("actual_method" in form_data and form_data["actual_method"] == "filter_by_manufacturer"):
            search_keyword = form_data["manufacturer"]
            all_computers = computer_list_by_manufacturer(search_keyword)

            template = 'computers/list.html'

            context = {
                'all_computers': all_computers
            }

            return render(request, template, context)
        else:
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute('''
                INSERT INTO hrapp_computer
                (
                    manufacturer, make, purchase_date   
                )
                VALUES (?, ?, ?)
                ''', (form_data['manufacturer'], form_data['make'], form_data['purchase_date']))

                computer_id = db_cursor.lastrowid

                db_cursor.execute('''
                INSERT INTO hrapp_employeecomputer
                (employee_id, computer_id, assign_date)
                VALUES (?, ?, ?)
                ''', (form_data['employee'], computer_id, datetime.date.today()))

            return redirect(reverse('hrapp:computer_list'))

def create_computer(cursor, row):
    _row = sqlite3.Row(cursor, row)

    computer = Computer()
    computer.id = _row['computer_id']
    computer.manufacturer = _row['manufacturer']
    computer.make = _row['make']
    computer.purchase_date = _row['purchase_date']
    computer.decommission_date = _row['decommission_date']

    employee = Employee()
    employee.id = _row['employee_id']
    employee.first_name = _row['first_name']
    employee.last_name = _row['last_name']

    computer.employee = employee

    return (computer, employee,)
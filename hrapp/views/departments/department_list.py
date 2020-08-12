import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Department
from hrapp.models import Employee
from ..connection import Connection
from ..helpers.create_department import create_department

def department_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_department
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT d.id, d.name, d.budget, e.id employee_id, e.first_name, e.last_name, e.start_date, e.is_supervisor, e.department_id
            FROM hrapp_department d
            LEFT JOIN hrapp_employee e ON e.department_id = d.id;
            """)

            department_dict = dict()

            departments = db_cursor.fetchall()

            for (department, employee) in departments:

                if department.id not in department_dict:
                    department_dict[department.id] = department
                    if not employee.id == None:
                        department_dict[department.id].employees.append(employee)               
                else:
                    department_dict[department.id].employees.append(employee)

            template = 'departments/department_list.html'

            context = {
                'all_departments': department_dict.values()
            }

        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_department
            (name, budget)
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['budget']))

            return redirect(reverse('hrapp:department_list'))

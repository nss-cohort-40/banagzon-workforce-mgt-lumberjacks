import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department, Employee
from ..connection import Connection
from ..helpers.create_department import create_department

def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_department
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT d.id, d.name, d.budget, e.id employee_id, e.first_name, e.last_name, e.start_date, e.is_supervisor, e.department_id
        FROM hrapp_department d
        LEFT JOIN hrapp_employee e ON e.department_id = d.id
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchall()

def department_detail(request, department_id):
    if request.method == 'GET':

        department = get_department(department_id)

        print('Department from row_factory:', department)

        department_dict = dict()

        for (department, employee) in department:
            if department.id not in department_dict:
                department_dict[department.id] = department
                department_dict[department.id].employees.append(employee)
            else:
                department_dict[department.id].employees.append(employee)

        template = 'departments/department_detail.html'


        context = {
            'department': department_dict.values()
        }

    return render(request, template, context)
import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.views.employees.employee_form import get_employee

def employee_details(request, employee_id):
    if request.method == "GET":
        employee = get_employee(employee_id)
        template_name = 'employees/detail.html'
        return render(request, template_name, {'employee': employee})

    elif request.method == 'POST':
        form_data = request.POST

        #check if this is editing an employee
        if(
            "actual_method" in form_data
            and form_data['actual_method'] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_employee
                SET first_name = ?,
                    last_name = ?,
                    start_date = ?,
                    is_supervisor = ?,
                    department_id = ?
                WHERE id = ?
                """,
                (
                    form_data['first_name'], form_data['last_name'], form_data['start_date'],
                    supervisor, form_data['department_id'], employee_id,
                ))
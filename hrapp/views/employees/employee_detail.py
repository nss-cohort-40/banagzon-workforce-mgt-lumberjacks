import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.views.employees.employee_form import get_employee

def employee_details(request, employee_id):
    if request.method == "GET":
        employee = get_employee(employee_id)
        template_name = 'employees/employee_detail.html'
        return render(request, template_name, {'employee': employee})

    elif request.method == 'POST':
        form_data = request.POST
        supervisor = 0
        if 'is_supervisor' in form_data:
            supervisor = 1

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
                    supervisor, form_data['department'], employee_id,
                ))
                
                db_cursor.execute("""
                UPDATE hrapp_employeecomputer
                SET computer_id = ?
                WHERE employee_id = ?
                """,
                (
                     form_data['computer'],employee_id,
                ))


                
            return redirect(reverse('hrapp:employee_list'))
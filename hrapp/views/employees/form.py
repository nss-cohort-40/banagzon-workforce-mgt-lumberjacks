import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
            e.is_supervisor
        FROM hrapp_employee e
        WHERE e.id = ?
        """,(employee_id,))

        return db_cursor.fetchone()


@login_required
def employee_form(request):
    if request.method == 'GET':
        employees = get_employees()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)

@login_required
def employee_edit_form(request, employee_id):

    if request.method == 'GET':
        book = get_employee(employee_id)
        libraries = get_libraries()

        template = 'books/form.html'
        context = {
            'book': book,
            'all_libraries': libraries
        }

        return render(request, template, context)
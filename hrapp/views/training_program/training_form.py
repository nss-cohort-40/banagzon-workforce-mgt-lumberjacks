import sqlite3
from django.shortcuts import render
from hrapp.models import Training_Program
from ..connection import Connection


def training_form(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.id,
                p.program_name,
                p.program_description,
                p.start_date,
                p.end_date,
                p.max_attendees
            from hrapp_training_program p
            """)

def training_form(request):
    if request.method == 'GET':
        template = 'training_programs/form.html'

        return render(request, template, context=None)
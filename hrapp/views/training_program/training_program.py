import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Training_Program
from ..connection import Connection


def training_list(request):
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

            list_training_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                program = Training_Program()
                program.id = row['id']
                program.name = row['program_name']
                program.description = row['program_description']
                program.start = row['start_date']
                program.end = row['end_date']
                program.max_attendees = row['max_attendees']

                list_training_programs.append(program)

        template = 'training_programs/list.html'
        context = {
            'all_training': list_training_programs
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute('''
                INSERT INTO hrapp_training_program
                (
                    program_name, program_description, start_date, end_date, max_attendees
                )
                VALUES(?, ?, ?, ?, ?)
                ''',
                (form_data['program_name'], form_data['program_description'], form_data['start_date'], form_data['end_date'], form_data['max_attendees']))

        return redirect(reverse('hrapp:training_list'))
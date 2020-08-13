import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection

def get_training_program(training_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('''
        SELECT
            p.id,
            p.program_name,
            p.program_description,
            p.start_date,
            p.end_date,
            p.max_attendees
        
        FROM hrapp_training_program p
        WHERE p.id = ?
        ''', (training_id,))

        return db_cursor.fetchone()

def training_details(request, training_id):
    if request.method == 'GET':
        training = get_training_program(training_id)

        template = 'training_programs/detail.html'
        context = {
            'training': training
        }

        return render(request, template, context)
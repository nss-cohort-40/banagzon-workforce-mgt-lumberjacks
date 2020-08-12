import sqlite3
from django.shortcuts import redirect, reverse, render
from hrapp.models import Computer
from ..connection import Connection

def computer_list_by_make(search_keyword):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        like_string = f'{search_keyword}%'

        db_cursor.execute("""
        SELECT
            c.id,
            c.manufacturer,
            c.make,
            c.purchase_date,
            c.decommission_date
        FROM hrapp_computer c
        WHERE c.make LIKE ?
        """, (like_string,))

        all_computers = list()

        dataset = db_cursor.fetchall()

        for row in dataset:
            computer = Computer()
            computer.id = row['id']
            computer.manufacturer = row['manufacturer']
            computer.make = row['make']
            computer.purchase_date = row['purchase_date']
            computer.decommission_date = row['decommission_date']

            all_computers.append(computer)

        return all_computers

def computer_list_by_manufacturer(search_keyword):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        like_string = f'{search_keyword}%'

        db_cursor.execute("""
        SELECT
            c.id,
            c.manufacturer,
            c.make,
            c.purchase_date,
            c.decommission_date
        FROM hrapp_computer c
        WHERE c.manufacturer LIKE ?
        """, (like_string,))

        all_computers = list()

        dataset = db_cursor.fetchall()

        for row in dataset:
            computer = Computer()
            computer.id = row['id']
            computer.manufacturer = row['manufacturer']
            computer.make = row['make']
            computer.purchase_date = row['purchase_date']
            computer.decommission_date = row['decommission_date']

            all_computers.append(computer)

        return all_computers

def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute('''
            SELECT
                c.id,
                c.manufacturer,
                c.make,
                c.purchase_date,
                c.decommission_date
            from hrapp_computer c
            ''')

            all_computers = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                computer = Computer()
                computer.id = row['id']
                computer.manufacturer = row['manufacturer']
                computer.make = row['make']
                computer.purchase_date = row['purchase_date']
                computer.decommission_date = row['decommission_date']

                all_computers.append(computer)

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
                ''',
                (form_data['manufacturer'], form_data['make'], form_data['purchase_date']))

            return redirect(reverse('hrapp:computer_list'))

            
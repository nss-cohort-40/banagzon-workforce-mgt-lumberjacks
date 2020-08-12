import sqlite3
from hrapp.models import Department, Employee
from ..connection import Connection


def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["id"]
    department.name = _row["name"]
    department.budget = _row["budget"]

    department.employees = list()

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    employee.is_supervisor = _row["is_supervisor"]
    employee.department_id = _row["department_id"]

    return (department, employee,)
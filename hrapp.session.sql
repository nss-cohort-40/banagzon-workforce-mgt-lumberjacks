SELECT d.id, d.name, d.budget, e.id employee_id, e.first_name, e.last_name, e.start_date, e.is_supervisor, e.department_id
FROM hrapp_department d
LEFT JOIN hrapp_employee e ON e.department_id = d.id
WHERE d.id = 1;

SELECT
    c.id,
    c.manufacturer,
    c.make,
    c.purchase_date,
    c.decommission_date
FROM hrapp_computer c
WHERE c.manufacturer LIKE '%ap%';

SELECT
    c.id computer_id,
    c.manufacturer,
    c.make,
    c.purchase_date,
    c.decommission_date,
    e.id,
    e.first_name,
    e.last_name
FROM hrapp_computer c
LEFT JOIN hrapp_employeecomputer ec ON ec.computer_id = c.id
LEFT JOIN hrapp_employee e ON e.id = ec.employee_id;

select
            c.id computer_id,
            ec.id employee_computer_id,
            c.make,
            c.manufacturer,
            c.purchase_date,
            c.decommission_date

        from hrapp_computer c
        left join hrapp_employeecomputer ec on ec.computer_id = c.id

select
            c.id computer_id,
            ec.computer_id,
            c.make,
            c.manufacturer,
            c.purchase_date,
            c.decommission_date

        from hrapp_computer c
        left join hrapp_employeecomputer ec on ec.computer_id = c.id

select
            ec.id,
            ec.computer_id,
            ec.employee_id,
            ec.assign_date,
            ec.unassign_date

        from hrapp_employeecomputer ec

SELECT
            e.id employee_id,
            e.first_name,
            e.last_name,
            e.start_date,
            e.is_supervisor,
            e.department_id,
            d.name department_name,
            c.id computer_id,
            c.make,
            c.manufacturer,
            ec.computer_id compid
        FROM hrapp_employee e
        JOIN hrapp_department d ON e.department_id = d.id
        left JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
        left JOIN hrapp_computer c ON ec.computer_id = c.id


SELECT
            e.id employee_id,
            e.first_name,
            e.last_name,
            e.start_date,
            e.is_supervisor,
            e.department_id,
            d.name department_name,
            c.id computer_id,
            c.make,
            c.manufacturer,
            ec.computer_id compid
        FROM hrapp_employee e
        JOIN hrapp_department d ON e.department_id = d.id
        left JOIN hrapp_employeecomputer ec ON e.id = ec.employe
        
select
    c.id,
    c.make,
    c.manufacturer,
    c.purchase_date,
    c.decommission_date,
    ec.employee_id,
    ec.computer_id
from hrapp_computer c
left join hrapp_employeecomputer ec on c.id = ec.computer_id

select
    e.id,
    e.first_name,
    e.last_name,
    e.start_date,
    e.is_supervisor,
    d.id department,
    c.id computer_id,
    c.make computer_make,
    c.manufacturer,
    ec.id employee_computer_id,
    ec.unassign_date
    
from hrapp_employee e
left join hrapp_department d on e.department_id = d.id
left join hrapp_employeecomputer ec on ec.employee_id = e.id
left join hrapp_computer c on c.id = ec.computer_id


select
    e.id,
    e.first_name,
    e.last_name,
    e.start_date,
    e.is_supervisor,
    d.id department,
    c.id computer_id,
    c.make computer_make,
    c.manufacturer,
    ec.id employee_computer_id,
    ec.unassign_date
    
from hrapp_employee e
    left join hrapp_department d on e.department_id = d.id
    left join hrapp_employeecomputer ec on ec.employee_id = e.id
    left join hrapp_computer c on c.id = ec.computer_id

select
    e.id,
    e.first_name,
    e.last_name,
    e.start_date,
    e.is_supervisor,
    d.id department,
    c.id computer_id,
    c.make computer_make,
    c.manufacturer,
    ec.id employee_computer_id,
    ec.unassign_date
    
from hrapp_employee e
    left join hrapp_department d on e.department_id = d.id
    left join hrapp_employeecomputer ec on ec.employee_id = e.id
    left join hrapp_computer c on c.id = ec.computer_id
where ec.unassign_date ISNULL

SELECT
    e.id employee_id,
    e.first_name,
    e.last_name,
    e.start_date,
    e.is_supervisor,
    e.department_id,
    d.name department_name,
    c.id computer_id,
    c.make,
    c.manufacturer,
    ec.computer_id compid,
    ec.unassign_date
FROM hrapp_employee e
JOIN hrapp_department d ON e.department_id = d.id
left JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
left JOIN hrapp_computer c ON ec.computer_id = c.id
WHERE ec.unassign_date ISNULL
AND e.id = 2

select
    c.id,
    c.make,
    c.manufacturer,
    c.purchase_date,
    c.decommission_date,
    ec.employee_id,
    ec.computer_id,
    ec.assign_date,
    ec.unassign_date

from hrapp_computer c
left join hrapp_employeecomputer ec on c.id = ec.computer_id
where ec.unassign_date is not NULL

SELECT
    e.id employee_id,
    e.first_name,
    e.last_name,
    e.start_date,
    e.is_supervisor,
    e.department_id,
    d.name department_name,
    c.id computer_id,
    c.make,
    c.manufacturer,
    ec.computer_id compid,
    ec.id emp_id
FROM hrapp_employee e
JOIN hrapp_department d ON e.department_id = d.id
left JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
left JOIN hrapp_computer c ON ec.computer_id = c.id
WHERE ec.unassign_date ISNULL
AND e.id = 9


select
    c.id,
    c.make,
    c.manufacturer,
    c.purchase_date,
    c.decommission_date,
    ec.employee_id,
    ec.computer_id,
    ec.assign_date,
    ec.unassign_date

from hrapp_computer c
left join hrapp_employeecomputer ec on c.id = ec.computer_id
where ec.unassign_date is not NULL
GROUP BY c.id

select
    c.id,
    c.make,
    c.manufacturer,
    c.purchase_date,
    c.decommission_date,
    ec.employee_id,
    ec.computer_id,
    ec.assign_date,
    ec.unassign_date

from hrapp_computer c
left join hrapp_employeecomputer ec on c.id = ec.computer_id
where c.decommission_date ISNULL

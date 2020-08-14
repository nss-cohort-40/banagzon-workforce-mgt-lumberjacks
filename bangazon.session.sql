select
            c.id computer_id,
            ec.computer_id employee_computer_id,
            c.make,
            c.manufacturer,
            c.purchase_date,
            c.decommission_date

        from hrapp_computer c
        left join hrapp_employeecomputer ec on ec.computer_id = c.id
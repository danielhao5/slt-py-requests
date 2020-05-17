#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Tests the simple and free REST API hosted at
http://dummy.restapiexample.com/ using all available endpoints
"""

import requests
from print_response import print_response


def main():
    """
    Execution starts here.
    """

    # Test GET all employees
    resp = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    print_response(resp, filename="get_employees")

    # Test GET employee with ID of 1
    resp = requests.get("http://dummy.restapiexample.com/api/v1/employee/1")
    print_response(resp, filename="get_employee_1")

    # Create a new employee
    new_employee = {
        "employee_name": "Nick Russo",
        "employee_salary": "75000",
        "employee_age": "34",
    }

    # Test POST to add a new employee
    resp = requests.post(
        "http://dummy.restapiexample.com/api/v1/create", json=new_employee
    )
    print_response(resp, filename="add_employee_success")


if __name__ == "__main__":
    main()

#!/usr/bin/python3

"""
This script fetches the task data of a given employee from the public 
API (jsonplaceholder.typicode.com) and displays the progress of completed tasks.

It takes an employee ID as a command-line argument and prints the following:

1. The employee's name.
2. The number of completed tasks vs the total number of tasks.
3. The titles of completed tasks.

The script uses the requests module to fetch the data from the API and handles 
error cases gracefully.

Usage:
    $ python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def fetch_employee_tasks(employee_id):
    """
    Fetches the tasks for a given employee from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of task dictionaries.
    """
    # Define the API URL
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        # Send GET request to the API
        response = requests.get(url)
        # Raise an


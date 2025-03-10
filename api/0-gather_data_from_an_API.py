#!/usr/bin/python3
"""
Fetches TODO list progress for a given employee ID from an API.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetch and display the employee's TODO list progress."""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    
    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)


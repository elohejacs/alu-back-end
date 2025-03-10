#!/usr/bin/python3
"""
Script to fetch employee TODO list progress using an API.
"""
import requests
import sys


def fetch_todo_list(employee_id):
    """Fetch and display the TODO list progress for an employee."""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, employee_id)).json()
    todos = requests.get("{}todos".format(url), params={"userId": employee_id}).json()

    if "name" not in user:
        print("User not found")
        return

    employee_name = user.get("name")
    done_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
    else:
        fetch_todo_list(int(sys.argv[1]))

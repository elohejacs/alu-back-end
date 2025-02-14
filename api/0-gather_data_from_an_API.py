#!/usr/bin/python3

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
        # Raise an exception if the response status is not 200 OK
        response.raise_for_status()
        # Return the JSON data
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle any HTTP errors or request issues
        print(f"Error fetching data: {e}")
        sys.exit(1)


def display_employee_progress(employee_id):
    """
    Displays the task progress of an employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Fetch tasks for the given employee
    tasks = fetch_employee_tasks(employee_id)
    
    # Retrieve employee's name from the first task (assumed)
    employee_name = tasks[0].get('userId')  # Using get to access dictionary values safely
    # Retrieve tasks related to the employee
    completed_tasks = [task['title'] for task in tasks if task.get('completed')]
    total_tasks = len(tasks)
    completed_count = len(completed_tasks)
    
    # Print the required output
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    # Ensure the script is run with an employee ID argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    # Get employee ID from the command-line argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
    
    # Display the progress for the employee
    display_employee_progress(employee_id)

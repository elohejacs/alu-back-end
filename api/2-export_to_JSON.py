#!/usr/bin/python3
"""
This script fetches an employee's tasks from the JSONPlaceholder API
and exports them in JSON format, structured as follows:
{
    "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
         "username": "USERNAME"},
        ...
    ]
}
The output file is named USER_ID.json.
"""

import json
import requests
import sys


def export_to_json(user_id):
    """Fetch tasks for a given user and save them in a JSON file."""
    user_id = str(user_id)  # Ensure user_id is a string
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(url)
    todos_response = requests.get(url + "/todos")
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        return  # Exit if API request fails
    
    user = user_response.json()
    todos = todos_response.json()
    
    if "id" not in user or "username" not in user:
        return  # Ensure user data is valid
    
    tasks = [{"task": t["title"], "completed": t["completed"],
              "username": user["username"]} for t in todos]
    
    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: tasks}, f)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        export_to_json(int(sys.argv[1]))

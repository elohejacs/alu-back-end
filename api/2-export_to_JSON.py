import json
import requests
import sys


def export_to_json(user_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(url).json()
    todos = requests.get(url + "/todos").json()
    
    tasks = [{"task": t["title"], "completed": t["completed"],
              "username": user["username"]} for t in todos]
    
    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: tasks}, f)


if __name__ == "__main__":
    export_to_json(sys.argv[1])

#!/usr/bin/python3
"""
Return to-do list information for a given employee ID
"""
import json
import requests
import sys
if __name__ == "__main__":
    """ Program Entry point """
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{id}").json()
    todos = requests.get(f"{url}todos", params={"userId": id}).json()
    with open(f'{id}.json', 'w') as fich:
        json.dump({
            id: [{
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user['name']}
                 for todo in todos]}, fich)

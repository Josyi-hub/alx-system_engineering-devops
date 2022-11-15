#!/usr/bin/python3
""" Return to-do list information for a given employee ID """
import requests
import sys
if __name__ == "__main__":
    """ Program Entry point """
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{id}").json()
    todos = requests.get(f"{url}todos", params={"userId": id}).json()
    finished = [todo['title'] for todo in todos if todo['completed'] is True]
    sentence = "is done with task"
    t = f"Employee {user['name']} {sentence} {len(finished)}/{len(todos)}: "
    print(t)
    [print("\t ", todo_title) for todo_title in finished]

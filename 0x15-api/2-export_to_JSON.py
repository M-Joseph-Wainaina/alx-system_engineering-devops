#!/usr/bin/python3
<<<<<<< HEAD
""" send a get request to an api and export to csv the todos"""

import json
import os
import requests
import sys


if __name__ == '__main__':
    try:
        userId = int(sys.argv[1])
    except ValueError:
        exit()

    apiUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{apiUrl}/users/{userId}"
    todosUrl = f"{userUrl}/todos"

    # user details response
    res = requests.get(userUrl).json()
    userName = res.get('name')

    # user todos
    todos = requests.get(todosUrl).json()

    numberOfTasks = len(todos)

    # get the number of completed tasks
    completedTasks = 0
    for todo in todos:
        if todo.get('completed'):
            completedTasks += 1
    incompleteTasks = numberOfTasks - completedTasks

    # export to csv
    with open(f"{userId}.json", mode='w', encoding='utf-') as f:
        tasksList = []
        for todo in todos:
            status = todo.get('completed')
            title = todo.get('title')
            taskDict = {"task": title, "completed":status, "username": userName}
            tasksList.append(taskDict)
        userDict = {str(userId):tasksList}
        f.write(json.dumps(userDict))
=======
"""Export data from an API to JSON format.
"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    # Checks if the argument can be converted to a number
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Main formatted names to API uris and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.json'.format(emp_id=emp_id)

    # User Response
    u_res = requests.get(user_uri).json()

    # User TODO Response
    t_res = requests.get(todo_uri).json()

    # A list of all tasks of an user
    user_tasks = list()

    for elem in t_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': u_res.get('username')
        }

        user_tasks.append(data)

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.json`
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: user_tasks}))
>>>>>>> c8110319d837e034739db7db32dc128c7e0de95d

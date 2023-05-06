#!/usr/bin/python3
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
    with open("todo_all_employees.json", mode='w', encoding='utf-8') as f:
        tasksList = []
        for todo in todos:
            status = todo.get('completed')
            title = todo.get('title')
            taskDict = {"task": title, "completed":status, "username": userName}
            tasksList.append(taskDict)
        userDict = {str(userId):tasksList}
        f.write(json.dumps(userDict))

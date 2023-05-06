#!/usr/bin/python3
""" send a get request to an api and export to csv the todos"""

import csv
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
    with open(f"{userId}.csv", mode='w', encoding='utf-') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            status = todo.get('completed')
            title = todo.get('title')
            writer.writerow([userId, userName, status, title])

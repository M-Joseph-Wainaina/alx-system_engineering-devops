#!/usr/bin/python3
<<<<<<< HEAD
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
=======
"""Export data from an API to CSV format.
"""
import csv
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
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    # User Response
    res = requests.get(user_uri).json()

    # Username of the employee
    username = res.get('username')

    # User TODO Response
    res = requests.get(todo_uri).json()

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.csv`
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in res:
            # Completed or non-completed task
            status = elem.get('completed')

            # The task name
            title = elem.get('title')

            # Writing each result of API response in a row of a CSV file
            writer.writerow([emp_id, username, status, title])
>>>>>>> c8110319d837e034739db7db32dc128c7e0de95d

#!/usr/bin/python3
""" send a get request to an api and print the todos"""

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

    # printing the output

    str = "Employee {name} is done with tasks({comp}/{all}):"
    print(str.format(name=userName, comp=completedTasks, all=incompleteTasks))
    for todo in todos:
        if todo.get('completed'):
            print("\t " + todo.get('title'))

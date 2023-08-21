#!/usr/bin/python3
"""
Empolyee todo progress
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """_summary_

    Args:
        employee_id (_type_): _description_
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if (user_response.status_code != 200 or
                todos_response.status_code != 200):
            print("Error fetching data from the API")
            return

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get("name")
        completed_tasks = [task for task in todos_data if task["completed"]]
        total_tasks = len(todos_data)
        done_tasks = len(completed_tasks)

        print(
            f"Employee {employee_name} is done with tasks "
            f"({done_tasks}/{total_tasks}): "
        )

        for task in completed_tasks:
            print("\t", task["title"])

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

#!/usr/bin/python3
""" Script to export data in the JSON format"""


if __name__ == "__main__":
    import json
    import requests

    # Endpoint URL
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    users_todo_dict = {}

    for user in users:
        user_id = user.get('id')
        user_todo_query = {'userId': user_id}
        response_2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                                  params=user_todo_query)
        todo_list = response_2.json()

        username = user.get('username')
        tasks = [{"task": task.get('title'), "username": username,
                  "completed": task.get('completed')} for task in todo_list]

        users_todo_dict[user_id] = tasks

    json_object = json.dumps(users_todo_dict)

    with open('todo_all_employees.json', "w") as jsonfile:
        jsonfile.write(json_object)

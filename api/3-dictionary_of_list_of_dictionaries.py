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
        # Extracting actual user id for extracts its TODO tasks
        user_id = user.get('id')
        user_todo_query = {'userId': user_id}
        response_2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                                  params=user_todo_query)
        todo_list = response_2.json()

        # Creating a list of user's tasks (each contained in dictionary form)
        username = user.get('username')
        tasks = [{"task": task.get('title'), "username": username,
                  "completed": task.get('completed')} for task in todo_list]

        # Updating users task's dictionary with actual user and its tasks
        users_todo_dict[user_id] = tasks

    # Serializing to json
    json_object = json.dumps(users_todo_dict)

    # Writing to json file
    with open('todo_all_employees.json', "w") as jsonfile:
        jsonfile.write(json_object)

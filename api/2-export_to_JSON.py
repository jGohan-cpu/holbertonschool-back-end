#!/usr/bin/python3
"""Script to export data i  the JSON format"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    u_id = argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    api_url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(u_id)
    response = requests.get(api_url).json()
    EMPLOYEE_NAME = response.get('username')
    response = requests.get(api_url2).json()
    f_name = u_id + '.json'
    u_list = {u_id: []}
    for info in response:
        dic = {"task": info.get('title'), "completed": info.get('completed'),
               "username": EMPLOYEE_NAME}
        u_list.get(u_id).append(dic)
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(u_list, f)

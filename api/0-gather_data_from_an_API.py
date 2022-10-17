#!/usr/bin/python3

"""
Module
"""

import requests
from sys import argv

url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
url_2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/"

response = requests.get(url)
result = response.json()
response_2 = requests.get(url_2)
result_2 = response_2.json()

item_2 = result_2['name']

# [item for item in list]
# arg = argv[1]

# names = [item['title'] for item in result if item['completed'] == True and item['userId'] == int(argv[1])]
# print(names)

# for employee in result:
#     print(employee)
# print(result_2['name'])

count = 0
count_2 = 0

for item in result:
    if (item['completed'] == True or item['completed'] == False) and item['userId'] == int(argv[1]):
        count_2 += 1
    if item['completed'] == True and item['userId'] == int(argv[1]):
        count += 1
print('Employee {} is done with tasks({}/{}):'.format(item_2, count, count_2))

for item in result:
    if item['completed'] == True and item['userId'] == int(argv[1]):
        print('\t', ' ', end='')
        print(item['title'])
#!/usr/bin/python3

"""
Module
"""

import requests
import sys

url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(sys.argv[1])
url_2 = "https://jsonplaceholder.typicode.com/users/{}/".format(sys.argv[1])

response = requests.get(url)
result = response.json()
response_2 = requests.get(url_2)
result_2 = response_2.json()

item_2 = result_2['name']

count = 0
count_2 = 0

for item in result:
    if (item['completed'] is True or item['completed'] is False) \
            and item['userId'] == int(sys.argv[1]):
        count_2 += 1
    if item['completed'] is True and item['userId'] == int(sys.argv[1]):
        count += 1
print('Employee {} is done with tasks({}/{}):'.format(item_2, count, count_2))

for item in result:
    if item['completed'] is True and item['userId'] is int(sys.argv[1]):
        print("\t {}".format(item['title']))

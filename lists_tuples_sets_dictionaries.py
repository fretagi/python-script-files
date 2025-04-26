#!/usr/bin/env python3

# servers = ['web1', 'web2', 'db1']
# first_server = servers[0]
# print("First Server: ", first_server)

# servers.append('cache1')
# print("List after adding cache1: ", servers)

# servers.remove('db1')
# print("List after removing 'db1': ", servers)

# web_servers = servers[:2]
# print("The first two servers: ", web_servers)

# Tuples
# config = ('localhost', 8080)
# host = config[0]
# port = config[1]
# print(f"Host: ", host)
# print(f"Port: ", port)

# SETs
# unique_users = {'alice', 'bob', 'charlie'}
# unique_users.add('david')
# print("Set after adding 'david:", unique_users)
# print("=== All users ====")
# set1 = {'alice', 'bob', 'david'}
# set2 = {'charlie', 'david', 'eve'}
# all_users = set1.union(set2)
# print("Union of set1 and set2:", all_users)
# print("== Common Users ==")
# common_users = set1.intersection(set2)
# print("Intersection of set1 and set2:", common_users)
# print("=== Diff Users ==")
# diff_users = set1.difference(set2)
# print("Differebce between set1 and set2 is: ", diff_users)

# DICTIONARIES

user_roles = {'alice': 'admin', 'bob': 'user'}
print("To access a value")
role = user_roles['alice']
print("Alice's role:", role)
print("Add a new entry")
user_roles['charlie'] = 'moderator'
print("Dictionary after adding 'Charlie' ", user_roles)
print("To modify a user role")
user_roles['bob'] = 'editor'
print("Dictionary after changing Bob's role ", user_roles)
print("=============")

keys = user_roles.keys()
values = user_roles.values()
items = user_roles.items()
print("keys:", keys)
print("Values:", values)
print("Items:", items)

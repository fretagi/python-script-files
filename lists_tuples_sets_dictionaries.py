servers = ['web1', 'web2', 'db1']
first_server = servers[0]
print("First Server: ", first_server)

servers.append('cache1')
print("List after adding cache1: ", servers)

servers.remove('db1')
print("List after removing 'db1': ", servers)

web_servers = servers[:2]
print("The first two servers: ", web_servers)

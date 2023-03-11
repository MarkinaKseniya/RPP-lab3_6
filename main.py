import http.client
import json
def operate(data: str, left: int):
    d = json.loads(data)
    if d['operation'] == 'div':
        return left / d['number']
    if d['operation'] == 'mul':
        return left * d['number']
    if d['operation'] == 'sum':
        return left + d['number']
    if d['operation'] == 'sub':
        return left - d['number']

# Задание 1 - Отправить HTTP запрос GET
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/6')
response = conn.getresponse()
print(response.status, response.reason)

dt1 = response.read().decode()
left = json.loads(dt1)['number']
print(left)

# Задание 2 - Отправить HTTP запрос GET с параметром
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/?option=6')
response = conn.getresponse()
print(response.status, response.reason)

dt1 = response.read().decode()
left = operate(dt1, left)
print(left)

# Задание 3 - Отправить HTTP запрос POST
conn = http.client.HTTPConnection("167.172.172.227:8000")
header = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/number/', 'option=6', header)
response = conn.getresponse()
print(response.status, response.reason)

dt1 = response.read().decode()
left = operate(dt1, left)
print(left)

# Задание 4 - Отправить HTTP запрос PUT с телом JSON
conn = http.client.HTTPConnection("167.172.172.227:8000")
header = {'Content-type': 'application/json'}
conn.request('PUT', '/number/', json.dumps({'option': 6}), header)
response = conn.getresponse()
print(response.status, response.reason)

dt1 = response.read().decode()
left = operate(dt1, left)
print(left)

# Задание 5 - Отправить HTTP запрос DELETE с телом JSON
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('DELETE', '/number/', json.dumps({'option': 6}))
response = conn.getresponse()
print(response.status, response.reason)

dt1 = response.read().decode()
left = operate(dt1, left)
print(left)

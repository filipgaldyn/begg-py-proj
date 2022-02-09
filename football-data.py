
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'KEY' }
connection.request('GET', '/v2/competitions/PL', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response)
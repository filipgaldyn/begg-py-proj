
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'c871a127e8ec4446bda54a895759d7f2' }
connection.request('GET', '/v2/competitions/PL', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response)
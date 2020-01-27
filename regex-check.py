from os import getenv, environ, listdir
from re import search
from sys import exit
import json

print(environ, flush=True)

workspace = getenv('GITHUB_WORKSPACE')
event_path = getenv('GITHUB_EVENT_PATH')

print([f for f in listdir('/github/workflow')], flush=True)

with open('/github/workflow/event.json') as f:
  event_data = json.load(f)
  print(event_data.keys(), flush=True)

print(event_data['pull_request'].keys(), flush=True)
print(event_data.get('pull_request'), flush=True)

try:
  regex = workspace
except:
  exit('You must provide a regex as the first arg')

try:
  string = getenv('GITHUB_WORKSPACE', 'String')
except:
  exit('You must provide a string to search as the second arg')

string = str(string)
match = search(regex, string)
print(match, flush=True)

if match:
  print("The regex found a match", flush=True)
  exit()
else:
  exit("No match was found for the provided regex")

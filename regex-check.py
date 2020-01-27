from os import getenv, environ, listdir
from re import findall
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
print(event_data.get('pull_request', {}).get('title'), flush=True)

try:
  regex = getenv('INPUT_PATTERN')
except:
  exit('You must provide a pattern using the "with:" key in the workflow config')

try:
  string = getenv('INPUT_STRING')
except:
  exit('You must provide a string using the "with:" key in the workflow config')

string = str(string)
match = findall(regex, string)
print(dir(match), flush=True)

if match:
  print("The regex found a match", flush=True)
  exit()
else:
  exit("No match was found for the provided regex")

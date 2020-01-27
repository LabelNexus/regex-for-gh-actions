from os import getenv, environ, listdir
from re import search
from sys import exit

print(environ, flush=True)

workspace = getenv('GITHUB_WORKSPACE')
event_path = getenv('GITHUB_EVENT_PATH')

print([f for f in listdir('github/home')])
print([f for f in listdir('github/workspace')])
print([f for f in listdir('github/workflow')])

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

if match:
  print("The regex found a match", flush=True)
  exit()
else:
  exit("No match was found for the provided regex")

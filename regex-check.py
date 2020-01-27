from os import getenv, environ
from re import findall
from sys import exit
import json

event_path = getenv('GITHUB_EVENT_PATH')

with open(event_path) as f:
  event_data = json.load(f)

regex = getenv('INPUT_PATTERN')
string = getenv('INPUT_STRING')

string = str(string)
match = findall(regex, string)

if match:
  print(f"The regex found a match in the provided string: {string}", flush=True)
  print(f"Matches: {[x for x in match]}", flush=True)
  exit()

else:
  exit(f"No match was found for the provided pattern - {regex} - and string - {string}")

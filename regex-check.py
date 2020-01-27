from os import getenv, environ
from re import findall
from sys import exit
import json

regex = getenv('INPUT_PATTERN')
string = getenv('INPUT_STRING')

string = str(string)
match = findall(regex, string)

if match:
  print(f"The regex found a match in the provided string: {string}", flush=True)
  print(f"Matche(s): {match}", flush=True)
  environ['OUTPUT_MATCHES'] = str(match)
  exit()

exit(f"No match was found for the provided pattern - {regex} - and string - {string}")

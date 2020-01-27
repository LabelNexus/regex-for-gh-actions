from re import findall
from os import getenv
from sys import exit

regex = getenv('INPUT_PATTERN')
string = getenv('INPUT_STRING')

string = str(string)
match = findall(regex, string)

if match:
  print(f"The regex found a match in the provided string: {string}", flush=True)
  print(f"Matche(s): {match}", flush=True)
  exit()

exit(f"No match was found for the provided pattern - {regex} - and string - {string}")

from sys import exit
from re import search
from os import getenv, environ

print(os.environ, flush=True)
try:
  regex = getenv('GITHUB_WORKSPACE')
except:
  exit('You must provide a regex as the first arg')

try:
  string = argv[2]
except:
  exit('You must provide a string to search as the second arg')

string = str(string)
match = search(regex, string)

if match:
  print("The regex found a match", flush=True)
  exit()
else:
  exit("No match was found for the provided regex")

import requests
import json
url = "https://api.bitbucket.org/2.0/repositories/mugunthanvellingiri"
response = requests.request(
   "GET",
   url
)
x=(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
a=json.loads(x)
b=(a["values"])
for i in range(0,len(b)):
  #slug.append(b[i].items())
  val=b[i].items()
  for j in val:
    if('slug' in j):
      Z=print(j[1])

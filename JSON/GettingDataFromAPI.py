import requests
import json
import jsonpath

api_URL="http://api.plos.org/search?q=title:DNA"
response=requests.get(api_URL)
print(response.text)

# Validating status code
assert response.status_code==200, "[Its not valid]"

# parsing response into JSON format
parsed_response=json.loads(response.text)
print(parsed_response)

#Applying JSON path
x=jsonpath.jsonpath(parsed_response,'response.numFound')
print(x)
y=jsonpath.jsonpath(parsed_response,'response.docs[0].id')
print(y)

for i in parsed_response['response.docs']:
    print(i['id'])



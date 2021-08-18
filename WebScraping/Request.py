# need to import request module
import requests

# Getting details via url
url="https://en-gb.facebook.com/"
response= requests.get(url)

# Printing HTML of the page
#print(response.text)

# Printing status code of the page
#print(response.status_code)

# Saving the read data in the txt file

f=open("C:/Users/ramadhma/Selenium/read.txt",'wb')

for data in response.iter_content(10000):
    f.write(data)

f.close()

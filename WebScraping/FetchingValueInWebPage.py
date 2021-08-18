import requests
import bs4

url="https://en-gb.facebook.com/"

response=requests.get(url)
# features="html.parser" is a additional argument for the BeautifulSoup Constructor to remove the warning
parsed_Data= bs4.BeautifulSoup(response.text,features="html.parser")
all_links= parsed_Data.select('a')

print(len(all_links))

for i in all_links:
    #print(i.getText())  # to print the text in the page
     print(i.get('href'))
     print(i.get('title'))
     # Attibutes
     print(i.attrs)
#!/root/Desktop/python
from bs4 import BeautifulSoup
import requests
url = raw_input("enter website")
#to take the url
r=requests.get("http://"+url) #this is done by using get function from requests library
data = r.text
#print data
soup=BeautifulSoup(data) #beautifulsoup helps us in extracting data
for link in soup.find_all('a'): #this finds all the anchor links. here 'a' stands for anchor tag 
	print link.get('href') #helps in getting all the links


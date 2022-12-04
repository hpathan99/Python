#Hassan Pathan
#This is an ongoing project to make a random movie selector from web-
#scraping data from websites. So far i got the text of the IMDB movie 
#list but still need to extract just the titles 

#from selenium import webdriver
from bs4 import BeautifulSoup
import requests



#this makes a request to the website
response = requests.get('https://www.imdb.com/chart/top/')

#parse the html content
soup = BeautifulSoup(response.content, 'html.parser')

#extract the specific data you are interested in
data = soup.find('table', attrs={'data-caller-name':'chart-top250movie'})
#convert to string
final = str(data)

#print(data)
#writes to a file
with open('movielist.txt','w') as file:
    file.write(final)

#Hassan Pathan
#This is an ongoing project to make a random movie selector from web-
#scraping data from websites. This one so far just has IMDB as its source

#from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import random



#this makes a request to the website
response = requests.get('https://www.imdb.com/chart/top/').text

#parse the html content
soup = BeautifulSoup(response, 'html.parser')

#extract the specific data you are interested in
data = soup.find('tbody', attrs={'class':'lister-list'})

#convert to string
final = str(data)

#writes to a file
#with open('movielisttest.txt','w') as file:
     #file.write(final)

file2 = open('Top 250 Movies Ever.txt','w')

movieList = []

with open('movielisttest.txt', 'r') as file:

#here we wanna get just the titles of the movies
     for line in file:
          start = line.find('alt=\"')
          end = line.find('\" height=')
          extracted_data = str(line[start:end])
          extracted_data = extracted_data.replace("alt=\"","")
          #here we have to check that the data we extracted is the proper length,
          #if not it will give us lots of blank spaces where it could not find the
          #start val and end val
          if len(extracted_data) >0:
            movieList.append(extracted_data)
          
for i in movieList:
     file2.write(i+'\n')

#file2.close()
#print(movieList)
rando = random.choice(movieList)
print(rando)



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
data = soup.find('tbody', attrs={'class':'lister-list'})

#dats = soup.find('td', attrs={'class':'titleColumn'})

#data2 = soup.find('table', attrs={'data-caller-name':'chart-top250movie'})
#convert to string
final = str(data)
#other = str(data2)
#print(final)

#print(len(final))

#other test
#print(len(other))


#writes to a file
with open('movielisttest.txt','w') as file:
    file.write(final)

file2 = open('moviesfromlist.txt','a+')

with open('movielisttest.txt', 'r') as file:
    #dau = file.read()
#here we wanna get just the titles of the movies
    for line in file:
        start = line.find('alt=')
        end = line.find(' height=')
        extracted_data = str(line[start:end])
        #doof = str(extracted_data)
        file2.write(extracted_data)
        #print(doof)

print(file2.read())

file2.close()

#we can remove the "alt=" so we are just left with titles now
with open('moviesfromlist.txt','r') as infile,\
    open('moviesfromlist2.txt','w') as outfile:
    datas = infile.read()
    datas = datas.replace("alt="," ")
    outfile.write(datas)
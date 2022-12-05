#Hassan Pathan
#This is an ongoing project to make a random movie selector from web-
#scraping data from websites. So far i got the text of the IMDB movie 
#list but still need to extract just the titles 

#from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import random



#this makes a request to the website
response = requests.get('https://www.imdb.com/chart/top/').text

#parse the html content
soup = BeautifulSoup(response, 'html.parser')

# mobies = []
# for mov in soup.find_all('a'):
#     mobies.append(mov.text)

# print(mobies)
#50 indexes later movie names start

#extract the specific data you are interested in
data = soup.find('tbody', attrs={'class':'lister-list'})


# #dats = soup.find('td', attrs={'class':'titleColumn'})

# #data2 = soup.find('table', attrs={'data-caller-name':'chart-top250movie'})
# #convert to string
final = str(data)



# #writes to a file
with open('movielisttest.txt','w') as file:
     file.write(final)

file2 = open('moviesfromlist.txt','a+')

movieList = []

with open('movielisttest.txt', 'r') as file:
#     #dau = file.read()


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

file2.close()
#print(movieList)
rando = random.choice(movieList)
print(rando)



#we can remove the "alt=" so we are just left with titles now
#with open('moviesfromlist.txt','r') as infile,\
    # open('moviesfromlist2.txt','w') as outfile:
    # datas = infile.read()
    # datas = datas.replace("alt="," ")
    # #print(datas)
    # movieList = movieList + [datas]
    # print(movieList)

    #outfile.write(datas)
    


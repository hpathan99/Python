#Hassan Pathan
#12/5/22 1:19AM I think the site I am using does not allow webscraping
from bs4 import BeautifulSoup
import requests
import random


# url = "https://www.afi.com/afis-100-years-100-movies/"
# #h6
# response = requests.get(url)
# html = response.text

# #parse the html code
# soup = BeautifulSoup(html, "html.parser")
# movie_elements = soup.find_all("h6", class_='q_title')
# for movie_element in movie_elements:
#     title_element = movie_element.find("h6",class_='q_title')
#     title_element_text = title_element.text
#     year_element = movie_element.find("span")
#     year_element_text = year_element.text
#     #director_element = movie_element.find("span", class_="director")
#     #director_element_text = movie_element.text

#     year_element = int(year_element_text)
#     movie = Movie("Citizen Kane", 1941)
#     db.add_movie(movie)

class Movie:
    def _init_(self, title, year):
        self.title = title
        self.year = year
        #self.director = director

    def _str_(self):
        return f"{self.title} ({self.year})"# - directed by {self.director}"

class MovieDatabase:
    def _init_(self):
        self.movies = []
    
    def add_movie(self, movie):
        self.movies.append(movie)
    
    def remove_movie(self, movie):
        self.movies.remove(movie)

    def search_by_year(self, title):
        return[m for m in self.movies if m.title == title]

    def search_by_year(self, year):
        return [m for m in self.movies if m.year == year]

    #def search_by_director(self, director):
        #return [m for m in self.movies if m.director == director]

def main():
    url = "https://www.afi.com/afis-100-years-100-movies/"
#h6
    response = requests.get(url)
    html = response.text
    db = MovieDatabase()
    db.movies=[]
#parse the html code
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    movie_elements = soup.find_all("h6", class_='q_title')
    print(movie_elements)
    for movie_element in movie_elements:
        title_element = movie_element.find("h6",class_='q_title')
        title_element_text = title_element.text
        #print(title_element_text)
        year_element = movie_element.find("span")
        year_element_text = year_element.text
        #director_element = movie_element.find("span", class_="director")
        #director_element_text = movie_element.text

        year_element = int(year_element_text)
        movie = Movie(title_element_text, year_element_text)
        db.add_movie(movie)
        
    #results = db.search_by_title("Citizen Kane")
    #print(results)
    if db.movies:
        print(db.movies)
    #else:
        #print("No Movies found")
    #print(db.movies)
if __name__ == "__main__":
    main()
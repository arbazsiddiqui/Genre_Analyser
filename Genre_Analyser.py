__author__ = 'siddiqui'
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import csv


totalMoviesInEachGenre = defaultdict(int)
avgRatingUnderEachGenre = defaultdict(float)


url = "http://www.imdb.com/search/title?at=0&sort=num_votes&title_type=feature&year=2015,2015";
response = requests.get(url);
page = response.text;
soup = BeautifulSoup(page);


movies = soup.find_all('td', attrs={"class": "title"})

for movie in movies:
    print "title : " + (movie.a.get_text())

    rating = float(movie.div.find('span', attrs={"class": "value"}).get_text())
    print rating

    genre = movie.find('span', attrs={"class": "genre"}).get_text()
    words = genre.split(' | ')
    for word in words:
        totalMoviesInEachGenre[word] += 1
        avgRatingUnderEachGenre[word] += rating

for key in totalMoviesInEachGenre:
    avgRatingUnderEachGenre[key] = avgRatingUnderEachGenre[key]/totalMoviesInEachGenre[key]


print totalMoviesInEachGenre
print avgRatingUnderEachGenre

writer = csv.writer(open('totalMoviesInEachGenre.csv', 'wb'))
for key, value in totalMoviesInEachGenre.items():
   writer.writerow([key, value])

writer1 = csv.writer(open('avgRatingUnderEachGenre.csv', 'wb'))
for key, value in avgRatingUnderEachGenre.items():
   writer1.writerow([key, value])
from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot
import requests
import re

site = 'https://www.imdb.com'

resp = requests.get(site + "/name/nm0331516/")
soup = BeautifulSoup(resp.text, 'html.parser')

writer_id_re = re.compile("^actor-tt")
rating = 'ratingValue'

films = {"year": [], "name": [], "rating": []}

films_tags = soup.findAll("div", {'id': writer_id_re})
for film_tag in films_tags:
    film_ref = film_tag.b.a['href']
    film_name = film_tag.b.a.string
    film_year = film_tag.span.string
    film_soup = BeautifulSoup(requests.get(site + film_ref).text, 'html.parser')
    film_rating = film_soup.find("span", {'itemprop': rating})
    print(film_rating)
    if film_rating:
        print(film_tag['class'], film_ref, film_name, film_rating.string)
        films["year"].append(film_year)
        films["name"].append(film_name)
        films["rating"].append(float(film_rating.string))

films["year"].reverse()
films["name"].reverse()
films["rating"].reverse()
films_table = pandas.DataFrame(films, index=films["year"])

plot = films_table.plot(figsize=(8, 6), linewidth=2, )

matplotlib.pyplot.show()
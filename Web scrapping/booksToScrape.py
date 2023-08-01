import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for i in range(1,51):

    url = f"https://books.toscrape.com/catalogue/page-{i}.html" #link to catalouge pgs

    response = requests.get(url) # to request to the data to be accessed

    data = response.content

    soup = BeautifulSoup(data, 'html.parser')

    ol = soup.find('ol') # to find first instance of ol list tag

    articles = ol.find_all('article', class_='product_pod') # to create a list of articles in the article tag and be more specific enter class name

    
    for article in articles:

        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star_rating = star['class'][1]
        price = article.find('p', class_ = 'price_color').text
        price = float(price[1:])

        books.append([title, price, star_rating])

# convert to csv file

# using dataframes from panda to covert it into csv file

df = pd.DataFrame(books, columns = ['Title', 'Price', 'Star Rating'])
df.to_csv('Web scrapping\Books.csv')
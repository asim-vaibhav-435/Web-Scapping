# Web Scraping Book.toscrape.com using Beautiful Soup, Requests, and Pandas


This is a simple Python script that scrapes the book.toscrape.com website using the Beautiful Soup library, the Requests library for making HTTP requests, and the Pandas library for creating a data frame of the scraped data.

### Prerequisites

Before running the script, make sure you have the following libraries installed:

+ Beautiful Soup 4
+ Requests
+ Pandas

You can install these libraries using pip by running the following command:

For requests library:
```
    pip install requests
```

for beautifulsoup tool:
```
    pip install bs4
```

for pandas library
```
    pip install pandas
```


## Running the Script

To run the script, simply navigate to the directory where the script is located and run the following command:

```
    python booksToScrape.py
```

The script will scrape the book.toscrape.com website and create a data frame of the scraped data. The data frame will be saved to a CSV file named "books.csv".

## Understanding the Script

The script works by sending an HTTP GET request to the book.toscrape.com website and retrieving the HTML content of the page. It then uses Beautiful Soup to parse the HTML and extract the relevant data (book title, price, rating, etc.). The data is then stored in a Pandas data frame and saved to a CSV file.


## Customizing the Script

You can customize the script to scrape different websites or extract different types of data by modifying the HTML parsing logic in the script. You can also modify the data frame creation logic to store the data in a different format (e.g. JSON, SQLite, etc.).

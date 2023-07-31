import time
import requests
from bs4 import BeautifulSoup

def web_scraping_quotes_with_beautifulsoup(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the quotes and authors on the page
        quotes = soup.select(".quote .text")
        authors = soup.select(".quote .author")

        # Extract and print the quotes and authors
        for quote, author in zip(quotes, authors):
            print("Quote:", quote.get_text())
            print("Author:", author.get_text())
            print("-----")

    except Exception as e:
        print("Error occurred:", str(e))

if __name__ == "__main__":
    # Replace the URL below with the website you want to scrape
    target_url = "http://quotes.toscrape.com/"
    web_scraping_quotes_with_beautifulsoup(target_url)

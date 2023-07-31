import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Use chromedriver_autoinstaller to automatically install the appropriate ChromeDriver version.
chromedriver_autoinstaller.install()

def web_scraping_quotes(url):
    # Configure Chrome options for running in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size to avoid rendering issues

    # Initialize the WebDriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the specified URL
        driver.get(url)

        # Wait for the page to load (adjust the sleep time if needed)
        time.sleep(5)

        # Find all the quotes and authors on the page
        quotes = driver.find_elements_by_css_selector(".quote .text")
        authors = driver.find_elements_by_css_selector(".quote .author")

        # Extract and print the quotes and authors
        for quote, author in zip(quotes, authors):
            print("Quote:", quote.text)
            print("Author:", author.text)
            print("-----")

    except Exception as e:
        print("Error occurred:", str(e))

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    # Replace the URL below with the website you want to scrape
    target_url = "http://quotes.toscrape.com/"
    web_scraping_quotes(target_url)

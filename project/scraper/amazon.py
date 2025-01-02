# amazon_scraper.py

import requests
from bs4 import BeautifulSoup
from app.scraper.base_scraper import BaseScraper

class AmazonScraper(BaseScraper):
    """Scraper for Amazon."""

    def fetch_data(self, product_name):
        url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        products = []
        results = soup.find_all("div", class_="s-main-slot s-result-list s-search-results sg-row")

        if results:
            for item in results[0].find_all("div", {"data-component-type": "s-search-result"}):
                name = item.find("span", class_="a-text-normal")
                price = item.find("span", class_="a-price-whole")
                link = item.find("a", class_="a-link-normal")

                if name and price and link:
                    products.append({
                        "name": name.text.strip(),
                        "price": price.text.strip(),
                        "url": f"https://www.amazon.in{link['href']}"
                    })
        return products

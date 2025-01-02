import requests
from bs4 import BeautifulSoup
from project.scraper.base_scraper import Base

class Flip(Base):
    
    def fetch_data(self, product_name):
        url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '+')}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html-parser")
        
        products = []
        results = soup.find("div",class_="DOjaWF gdgoEp")
        
        if results:
            for i in results:
                name = i.find("div",class_="_4rR01T")
                price = i.find("div", class_="_30jeq3 _1_WHN1")
                link = i.find("a", class_="_1fQZEK")
                
                if name and price and link:
                    products.append({
                        "name": name.text.strip(),
                        "price": price.text.strip(),
                        "url": f"https://www.flipkart.com{link['href']}"
                    })
        return products
import pandas as pd
import requests
from bs4 import BeautifulSoup

# ! data for 10 pages
# for i in range(1,11):
#     url="https://www.flipkart.com/search?q=laptops+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text ,"lxml" )
    
#     next_pg = soup.find("a",class_="_9QVEpD").get("href")
    
#     complete_np = "https://www.flipkart.com"+next_pg
#     print(complete_np)
    
# print(soup)


#! for shifting to next pages 
# while True:
#     next_pg = soup.find("a",class_="_9QVEpD").get("href")
    
#     complete_np = "https://www.flipkart.com"+next_pg
    
#     url = complete_np
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text , "lxml")

product_name = []
price = []
desc = []
reviews = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=laptops+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")
    
    names = box.find_all("div", class_="KzDlHZ")
    for name in names:
        product_name.append(name.text.strip() if name else "None")
    
    prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for price_item in prices:
        price.append(price_item.text.strip() if price_item else "None")
    
    desci = box.find_all("li", class_="J+igdf")
    for description in desci:
        desc.append(description.text.strip() if description else "None")
    
    revi = box.find_all("div", class_="XQDdHH")
    for review in revi:
        reviews.append(review.text.strip() if review else "None")
max_len = max(len(product_name), len(price), len(desc), len(reviews))

product_name += [None] * (max_len - len(product_name))
price += [None] * (max_len - len(price))
desc += [None] * (max_len - len(desc))
reviews += [None] * (max_len - len(reviews))

# print(len(desc))
# print(len(product_name))
# print(len(reviews))
# print(len(price))
# print(reviews[0])
df = pd.DataFrame({
    "Product Name": product_name,
    "Prices": price,
    "Description": desc,
    "Reviews": reviews
})
df.to_csv("newlaptop_details.csv")
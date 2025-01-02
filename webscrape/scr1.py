import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to extract data from URL based on user input
def extract_data(url, name_tag, name_class, price_tag, price_class, desc_tag, desc_class, review_tag, review_class):
    # Initialize lists to store extracted data
    product_name = []
    price = []
    desc = []
    reviews = []

    # Loop through pages (can be modified if needed)
    for i in range(1, 11):
        page_url = f"{url}&page={i}"
        
        r = requests.get(page_url)
        soup = BeautifulSoup(r.text, "lxml")
        
        # Extract product names
        names = soup.find_all(name_tag, class_=name_class)
        for name in names:
            product_name.append(name.text.strip() if name else "None")
        
        # Extract product prices
        prices = soup.find_all(price_tag, class_=price_class)
        for price_item in prices:
            price.append(price_item.text.strip() if price_item else "None")
        
        # Extract product descriptions
        descriptions = soup.find_all(desc_tag, class_=desc_class)
        for description in descriptions:
            desc.append(description.text.strip() if description else "None")
        
        # Extract product reviews
        reviews_data = soup.find_all(review_tag, class_=review_class)
        for review in reviews_data:
            reviews.append(review.text.strip() if review else "None")

    # Ensure lists are the same length
    max_len = max(len(product_name), len(price), len(desc), len(reviews))
    product_name += ["None"] * (max_len - len(product_name))
    price += ["None"] * (max_len - len(price))
    desc += ["None"] * (max_len - len(desc))
    reviews += ["None"] * (max_len - len(reviews))

    # Create a DataFrame
    df = pd.DataFrame({
        "Product Name": product_name,
        "Prices": price,
        "Description": desc,
        "Reviews": reviews
    })
    
    return df

# Streamlit UI to get user inputs
st.title("Web Scraper")

# URL input
url = st.text_input("Enter the URL to scrape:")

# Dropdown for selecting tags and classes
name_tag = st.selectbox("Select tag for product name", ['div', 'span', 'a', 'li', 'p','h'])
name_class = st.text_input("Enter class for product name (e.g., 'KzDlHZ')")

price_tag = st.selectbox("Select tag for price", ['div', 'span', 'a', 'li', 'p','a'])
price_class = st.text_input("Enter class for price (e.g., 'Nx9bqj _4b5DiR')")

desc_tag = st.selectbox("Select tag for description", ['div', 'span', 'a', 'li', 'p','h'])
desc_class = st.text_input("Enter class for description (e.g., 'J+igdf')")

review_tag = st.selectbox("Select tag for review", ['div', 'span', 'a', 'li', 'p','h'])
review_class = st.text_input("Enter class for review (e.g., 'XQDdHH')")

# Button to start scraping
if st.button("Start Scraping"):
    if url and name_class and price_class and desc_class and review_class:
        st.write("Scraping data... Please wait.")

        # Call function to scrape data
        df = extract_data(url, name_tag, name_class, price_tag, price_class, desc_tag, desc_class, review_tag, review_class)
        
        # Display the extracted data
        st.write("Extracted Data:")
        st.dataframe(df)

        # Create a new CSV file and write data to it
        df.to_csv("scraped_data.csv", index=False)

        # Provide a download button to allow the user to download the newly created file
        with open("scraped_data.csv", "r") as file:
            st.download_button(label="Download CSV", data=file, file_name="scraped_data.csv", mime="text/csv")

    else:
        st.error("Please fill in all the fields.")

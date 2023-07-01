import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
app=Flask(__name__)
def get_product_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    priceofproducr = soup.find('span', {'class': 'a-price-whole'})
    if priceofproducr:
        price = priceofproducr.get_text().strip()
    else:
        price = 'Price of the selected product not traceable'
    productimg = soup.find('img', {'id': 'landingImage'})
    if productimg:
        image_url = productimg['src']
    else:
        image_url = 'Product image not traceable'
    return price, image_url

# URL must contain only dp/productid and not the lengthy ref one...
product_url = input('Enter the Product URL in this format Only:\nwww.amazon.in/dp/B0BVBFSBN2:\n')
price, image_url = get_product_info(product_url)

print('Product Price:', price)
print('Product Image URL:', image_url)


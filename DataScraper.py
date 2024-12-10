import requests
from bs4 import BeautifulSoup

URL = "https://www.autoscout24.com/lst/mercedes-benz/glc-(all)"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("article")

for listing in results:
    listing_mileage = listing["data-mileage"]
    listing_model = listing["data-model"]
    listing_first_registration = listing["data-first-registration"]
    listing_fuel_type = listing["data-fuel-type"]
    listing_price = listing["data-price"]

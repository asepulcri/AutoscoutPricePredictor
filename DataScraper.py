import requests
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame(columns = ["country", "model", "first_registration", "mileage", "fuel_type", "price"])

for page_number in range(1, 20):

    Italy = f"https://www.autoscout24.com/lst/mercedes-benz/glc-(all)?atype=C&cy=I&desc=0&page={page_number}&search_id=e4ewrnejpk&sort=standard&source=listpage_pagination&ustate=N%2CU"
    Germany = f"https://www.autoscout24.com/lst/mercedes-benz/glc-(all)?atype=C&cy=D&damaged_listing=exclude&desc=0&page={page_number}&powertype=kw&search_id=29j0vkid1us&sort=standard&source=listpage_pagination&ustate=N%2CU"
    Austria = f"https://www.autoscout24.com/lst/mercedes-benz/glc-(all)?atype=C&cy=A&damaged_listing=exclude&desc=0&page={page_number}&powertype=kw&search_id=a6mwlucw4s&sort=standard&source=listpage_pagination&ustate=N%2CU"

    URLs = [Italy, Germany, Austria]

    for URL in URLs:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all("article")

        for listing in results:
            listing_country = listing["data-listing-country"]
            listing_model = listing["data-model"]
            listing_first_registration = listing["data-first-registration"]
            listing_mileage = listing["data-mileage"]
            listing_fuel_type = listing["data-fuel-type"]
            listing_price = listing["data-price"]

            temp_df = pd.DataFrame({"country": [listing_country],
                                    "model": [listing_model],
                                    "first_registration": [listing_first_registration],
                                    "mileage": [listing_mileage],
                                    "fuel_type": [listing_fuel_type],
                                    "price": [listing_price]})

            df = pd.concat([df, temp_df], ignore_index = True)


df.to_csv("out.csv", index = False)
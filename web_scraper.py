import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_products():
    url = "https://books.toscrape.com/"  # Demo scraping website

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
    except requests.exceptions.RequestException as e:
        print("Error fetching the website:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    items = soup.find_all("article", class_="product_pod")

    for item in items:
        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").text

        products.append({
            "Product Title": title,
            "Price": price
        })

    # Convert to DataFrame
    df = pd.DataFrame(products)

    # Save to CSV
    df.to_csv("products.csv", index=False)

    print("Scraping completed successfully!")
    print("Data saved to products.csv")


if __name__ == "__main__":
    scrape_products()
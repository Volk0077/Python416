import requests
from bs4 import BeautifulSoup
import csv
import os


def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for book in books:
        name = book.find("h3").find("a").get("title")
        price = book.find("p", class_="price_color").text.replace("Â£", "")
        availability = book.find("p", class_="instock availability").text.strip()
        print(price)

        data = {
            "name": name,
            "price": price,
            "availability": availability,
        }
        write_csv(data)


def write_csv(data):
    with open("books.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        # Форматируем цену без символа валюты
        clean_price = data["price"].replace("£", "").replace("Â£", "").strip()
        formatted_price = f" {clean_price} "
        writer.writerow((data["name"], formatted_price, data["availability"]))


def main():
    if not os.path.exists("books.csv"):
        with open("books.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(("Name", "Price", "Availability"))
    for i in range(1, 5):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        get_data(get_html(url))


if __name__ == "__main__":
    main()

from typing import Container
from bs4 import BeautifulSoup
import requests


def fetch_pages():
    url = "http://www.nepalstock.com/todaysprice"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.findAll("a", {"title": "Next Page"}, href=True)
    url = results[0]['href']
    print
    # fetchData()
    # all_row_item = soup.find("div", {"class": "pager"}


fetch_pages()


def fetchData(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_row_item = soup.find("div", {"id": "home-contents"}
                             ).find("table").findAll("tr")
    all_item = all_row_item[2:len(all_row_item)-4]
    for index, i in enumerate(all_item):
        print(index+1, end=" | ")
        name = i.findAll("td")[1].text
        max_price = i.findAll("td")[3].text
        min_price = i.findAll("td")[4].text

        closing_price = i.findAll("td")[5].text
        previous_closing = i.findAll("td")[8].text
        difference = i.findAll("td")[9].text

        print("Company name :", name, end=" | ")
        print("closing_price :", closing_price, end=" |")
        print("max_price :", max_price, end=" | ")
        print("min_price :", min_price, end=" | ")
        print("previous_closing :", previous_closing, end=" | ")
        print("difference :", difference)

#"""
#1. create a webscraper that grabs the latest flyer prices from www.walmart.ca and www.voila.ca for each sale item. append the source website to the end of each item name
#2. Create a canvas that holds an item selector that contains each sale item
#3. when an item is selected, display the sale price on the canvas below the item selector
#"""
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import *
import requests
from bs4 import BeautifulSoup
from lxml import html
import lxml.html
import re
from urllib.request import urlopen
import urllib.request
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import tkinter.messagebox

#import requests
#from bs4 import BeautifulSoup
#import re


def walmart_scraper():
    walmart_url = "https://www.walmart.ca/en/grocery/N-117"
    wal_response = requests.get(walmart_url)
    wal_page = wal_response.text
    wal_soup = BeautifulSoup(wal_page, 'lxml')
    walmart_item_link = walmart_url + wal_soup.find('a', text=item_input).get('href')
    walmart_item_response = requests.get(walmart_item_link)
    walmart_item_page = walmart_item_response.text
    walmart_item_soup = BeautifulSoup(walmart_item_page, 'lxml')
    walmart_item_price = walmart_item_soup.find('span', {'class': 'price-characteristic'}).get('content')
    walmart_item_name = wal_soup.find('a', text=item_input).get('aria-label')
    walmart_item_name = walmart_item_name + ' from walmart' + '\n' + 'Regular price: ' + walmart_item_price
    return walmart_item_name

#print(walmart_scraper())

def voila_scraper():
    voila_url = "https://www.voila.ca/"
    voila_response = requests.get(voila_url)
    voila_page = voila_response.text
    voila_soup = BeautifulSoup(voila_page, 'lxml')
    voila_item_link = voila_url + voila_soup.find('a', text=item_input).get('href')
    voila_item_response = requests.get(voila_item_link)
    voila_item_page = voila_item_response.text
    voila_item_soup = BeautifulSoup(voila_item_page, 'lxml')
    voila_item_price = voila_item_soup.find('span', {'class': 'price price--withoutTax price--main'}).text
    voila_item_name = voila_soup.find('a', text=item_input).get('aria-label')
    voila_item_name = voila_item_name + ' from voila' + '\n' + 'Regular price: ' + voila_item_price
    return voila_item_name

#print(voila_scraper())

def compare_prices(item1, item2):
    if item1 < item2:
        return "1"
    elif item1 > item2:
        return "2"
    else:
        return "Tie"

def wal_voila_compare():
    walmart_item = walmart_scraper()
    voila_item = voila_scraper()
    comparison = compare_prices(walmart_item, voila_item)
    return comparison

def choose_item():
    global item_input
    item_input = simpledialog.askstring("Item", "Enter an item.")
    if item_input is None:
        root.destroy()
        exit()
    while not item_input:
        item_input = simpledialog.askstring("Item", "Enter an item.")
        if item_input is None:
            root.destroy()
            exit()

#print(wal_voila_compare())
root = tk.Tk()
root.geometry("300x300")
root.title("Grocery Price Comparison")

choose_item()

font=("Courier New", 36, "bold")

Label(root, text="WALMART", font=font).pack(fill=X)
Label(root, text=walmart_scraper(), font=font).pack(fill=X)
Label(root, text="Voila", font=font).pack(fill=X)
Label(root, text=voila_scraper(), font=font).pack(fill=X)
Label(root, text="Winner:", font=font).pack(fill=X)
Label(root, text=wal_voila_compare(), font=font).pack(fill=X)

root.mainloop()
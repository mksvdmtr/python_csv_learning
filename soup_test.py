from bs4 import BeautifulSoup
import requests
import csv

resp = requests.get("http://quotes.toscrape.com/")
html_data = BeautifulSoup(resp.text, 'html.parser')

quotes = html_data.find_all(class_='quote')

with open("quotes.csv", "w") as file:
    field_names = ['Author', 'Quote', 'Tegs']
    writer = csv.DictWriter(file, field_names, delimiter=";")
    writer.writeheader()
    for q in quotes:
        writer.writerow({'Author': q.find(class_='author').get_text(), 'Quote': q.find(class_='text').get_text(), 'Tegs': q.find(class_='keywords')['content']})

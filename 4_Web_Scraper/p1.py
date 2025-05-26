import csv
from bs4 import BeautifulSoup
import requests


url = "http://127.0.0.1:5500/4_Web_Scraper/example.html"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text,'html.parser')
titles = soup.find_all('h2',class_='article-title')
print(titles)


data = []
for title in titles:
    text = title.get_text(strip=True)
    link = title.find('a')['href'] if title.find('a') else '' 
    data.append([text, link])

with open('scraped_data.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Link']) 
    writer.writerows(data)

print("Data saved to scraped_data.csv")
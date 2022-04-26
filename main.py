import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

json_data = []
response = requests.get('https://www.themoscowtimes.com/').text
soup = BeautifulSoup(response, 'html.parser')
articles = soup.find_all('div', class_='article-excerpt-default')
for article in articles:
    title = article.find('h3', class_='article-excerpt-default__headline').get_text(strip=True)
    desc = article.find('div', class_='article-excerpt-default__teaser').get_text(strip=True) if article.find('div', class_='article-excerpt-default__teaser') else 'No info'
    category = article.find('span', class_='label').get_text(strip=True)

    image_link = article.find('img')['src']

    link = article.find('a')['href']
    print(link)
    json_data.append(
        {
            'title': title,
            'desc': desc,
            'category': category,
            'image_link': image_link,
            'link': link
        }
    )

with open('wtf.json', mode='w', encoding='utf-8',) as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)

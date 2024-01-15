
import requests
from bs4 import BeautifulSoup

def scrape_eventbrite_edmonton():
    url = 'https://www.eventbrite.com/d/canada--edmonton/tech--events/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    events = []
    for event in soup.find_all(class_='search-event-card-rectangle-image'):
        title = event.find(class_='eds-event-card-content__title').text.strip()
        date = event.find(class_='eds-event-card-content__sub-title').text.strip()
        link = event.find('a')['href']
        events.append({'title': title, 'date': date, 'link': link})

    return events

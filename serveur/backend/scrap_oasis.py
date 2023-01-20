import bs4 
from selenium import webdriver
from time import sleep
from .school import School

url = 'https://oasis.mines-paristech.fr/prod/bo/?targetProject=oasis_ensmp&public#codepage=ROOM_MANAGER_VIEW&view=timelineDay'


def scrap(school:School):
    browser = webdriver.Firefox()
    browser.get(url)

    sleep(20)

    res = browser.page_source
    oasis = bs4.BeautifulSoup(res,'html.parser')  
    browser.close()

    # Formate the data

    table = oasis.find_all('table', class_="table-bordered")[4]
    rooms = table.find_all('tr')

    for room in rooms:
        try:
            room_reservations = []
            room_id = room['data-resource-id']
            events = room.find_all('a', class_="fc-timeline-event fc-h-event fc-event fc-start fc-end")
            for event in events:
                data = event["title"]
                from_ = data[1:6]
                to = data[7:12]
                title = data[14:]
                room_reservations.append({'title': title, 'from_': from_, 'to': to})
            school[room_id].update_reservations(room_reservations)
        except:
            pass
import bs4 
from selenium import webdriver
from time import sleep

url = 'https://oasis.mines-paristech.fr/prod/bo/?targetProject=oasis_ensmp&public#codepage=ROOM_MANAGER_VIEW&view=timelineDay'

browser = webdriver.Firefox()
browser.get(url)

sleep(20)

res = browser.page_source
oasis = bs4.BeautifulSoup(res,'html.parser')  



#price = oasis.find_all('div', attrs={'class':"fc-event-container"})
price = oasis.find_all('tbody')



browser.close()
import requests
import random
import json
import os
from bs4 import BeautifulSoup
from config import anekdotsLinks

# Массив анекдотов
anekdotsArray = []
# PROXY
PROXY = 'https://anekdotovstreet.com'

# HEADERS
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

# Получает html
def get_html(url,param=None):
    r =  requests.get(url,headers=HEADERS,params=param)
    return r

# Возвращает количество страниц :int
def get_pages_count(html):
    soup = BeautifulSoup(html,'html.parser')
    pagination = soup.find('ul',class_='pagination').find_all('a')
    if pagination:
        pages = []
        for page in pagination:
            pages.append(page.get('href'))        
        countArrSplit = pages[-1].split('/')
        countPages = []
        for k in countArrSplit:
            if(k != ''):
                countPages.append(k) 
        return int(countPages[-1])
    else:
        return int(1)

# Находит контент на странице
def find_content(content):
    soup = BeautifulSoup(content,'html.parser')
    items = soup.find_all('div',class_='anekdot-text')
    start_id = 0
    if(len(anekdotsArray) > 0):
        start_id = int(anekdotsArray[-1]["id"])

    for i in range(0,len(items)):
        anekdotsArray.append(
            {
                "id":i + start_id + 1,
                "anekdot":items[i].find('p').get_text()
            }
        )
    return anekdotsArray
    
def parseDefaultPage(URL): 
    html = get_html(f"{URL}/")
    find_content(html.text)
 
#parse page - парсит все страницы 
def parsePages(URL,pages_count):
    if(pages_count > 1):
        parseDefaultPage(URL)
        for page in range(2,pages_count + 1):
            html = get_html(f"{URL}{page}/")
            find_content(html.text)
    else:
        parseDefaultPage(URL)

def saveToJson(arr,arr_name):       
    with open(f"json/json_anekdots_{arr_name}.json",'w',encoding='utf-8') as write_anekdots:
        json.dump(arr,write_anekdots,ensure_ascii=False)


def loadAnekdotsPage(urlAnekdot):
    URL = f'{PROXY}/nacionalnosti/{urlAnekdot}/'
    html = get_html(URL)
    
    if html.status_code == 200:
        html = html.text
        pages_count = get_pages_count(html)
        parsePages(URL,pages_count)
        saveToJson(anekdotsArray,urlAnekdot)
        anekdotsArray.clear()
    else:
        return 'Error!Sorry... :('

def createDirJson():
    print('Create catalog...')
    filename = 'json'
    if(os.path.exists(filename)):
        for fileJson in os.listdir(filename):
            os.remove(f"{filename}/{fileJson}")
        os.rmdir(filename)
    os.mkdir(filename) 

def renderAnekdots():
    print('Loading...')
    createDirJson()
    for anekdotLink in anekdotsLinks:
        loadAnekdotsPage(anekdotsLinks[anekdotLink])
        print(f'Parsed - {anekdotsLinks[anekdotLink]}')

    print('All Render and Save!')

def randerChooseAnekdot(anekdotLink):
    print('Loading')
    loadAnekdotsPage(anekdotsLinks[anekdotLink])
    print(f"Parsed - {anekdotsLinks[anekdotLink]}")


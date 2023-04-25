
from bs4 import BeautifulSoup
import requests
import json

def parse(start_, stop_):
    
    Q_A = {}
    
    for i in range(start_, stop_): 
        URL = f"https://www.yurist-online.net/question/{i}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        
        try:
            key = soup.find('div', class_ = 'question-details').text
            key = str(key)[10:].lstrip()

            val_list = []

            temp = soup.find_all('div', class_ ='answer-text')

            for i in list(temp):
                val_list.append(i.text)
            if len(val_list) > 0:
                Q_A[key] = val_list
        except:
            pass
        
    res = Q_A.copy()
    
    with open(f'Q_A//Q_A_{stop_}.json', 'w') as file:
        if len(res) > 0:
            json.dump(res, file)
            print(f'file {stop_} write succesfully')
        
    #return Q_A

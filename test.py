##https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director

import requests
from bs4 import BeautifulSoup

wikiurl="https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})

years = []
films = []
directors = []
qqq = []
i = 0
winners = []
year = 0
for items in indiatable:#, {"style" : "background:#FAEB86"})[1::1]:
    # i += 1
    # # print(items)
    data1 = items.find_all('tbody')#, {'style' : "background:#FAEB86"})
    for i in data1:

        data = i.find_all('tr')
        for datum in data:
            if datum.find('th')!=None:
                try:
                    year = datum.find('th').find("a").text
                    print(year)
                except:
                    pass
            tds =  datum.find_all("td")
            
            if len(tds)>=2:
                qqq.append(tds[0].text)
                qqq.append(tds[1].text)
                qqq.append(year)
                if len(tds[0].find_all("b"))==0:
                    qqq.append(0)
                else:
                    qqq.append(1)



for i, q in enumerate(qqq):
    if i % 4 == 2:
        years.append(q)
    elif i % 4 == 0:
        directors.append(q.replace("\n",""))
    elif i % 4 == 1:
        films.append(q.replace("\n",""))
    else:
        winners.append(q)



import pandas as pd

results = pd.DataFrame()
# results['year'] = years
results['director'] = directors
results['film'] = films
results['year'] = years
results['winner'] = winners
results.to_csv('BestDirector.csv')
print(results.head(15))
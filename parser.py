import requests
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar

# http://kalmcorpora.ru/parallel/2/а?page=31
# http://kalmcorpora.ru/parallel/1/%20/0/0/0/0

# response = requests.post()
# response.status_code

# r = requests.get('http://kalmcorpora.ru/parallel/2/%20?page=0')
# html = BeautifulSoup(r.content, 'html.parser')

# for el in html.select('.pagetable > tbody > tr'):
#     try:
#         ru = el.select('td')[1].select('div')[0].select('span')[1].text
#         xal = el.select('td')[1].select('div')[1].select('span')[1].text
#         print(" RU:", ru)
#         print("XAL:", xal)
#     except:
#         pass

ed = 475

bar = IncrementalBar('Progress', max=ed)
file_ = open('corpus/corpus-v2.csv', 'w', encoding='utf-8')
for i in range(ed):
    r = requests.get('http://kalmcorpora.ru/parallel/1/%20?page=' + str(i))
    html = BeautifulSoup(r.content, 'html.parser')

    for el in html.select('.pagetable > tbody > tr'):
        try:
            xal = el.select('td')[1].select('div')[0].select('span')[1].text.replace('\n', ' ')
            ru = el.select('td')[1].select('div')[1].select('span')[1].text.replace('\n', ' ')
            file_.write(xal + ' | ' + ru + '\n')
        except:
            pass
    bar.next()
file_.close()
bar.finish()
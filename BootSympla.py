# python3

import requests
import bs4
from urllib.request import urlopen

res = requests.get("https://www.sympla.com.br/eventos/uberlandia-mg")

try:
    res.raise_for_status()
except Exception as  exc:
    print('Um problema encontrado:%s'%(exc))


# newFile = open('NovoArquivo.html', 'wb')
#
# for texto in req.iter_content(200000):
#     newFile.write(texto)
#
# newFile.close()
#
# file = open('NovoArquivo.html')

htmlReq = bs4.BeautifulSoup(res.text, 'html.parser')

eventos = htmlReq.find_all('div', class_='single-event-box')

# print(type(eventos))
# print(len(eventos))

evento = eventos[0]

# print(evento)
links = evento.find_all('a')
for i in links:
    link = i.get('href')


print(link)


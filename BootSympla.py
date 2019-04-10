# python3

import requests
import bs4
import pandas as pd
from urllib.request import urlopen
import lxml.html as parser

# PAGINA 1
res = requests.get("https://www.sympla.com.br/eventos/uberlandia-mg")

# VERIFICA SE TEVE RETORNO A REQ
try:
    res.raise_for_status()
except Exception as  exc:
    print('Um problema encontrado:%s'%(exc))


# newFile = open('NovoArquivo.html', 'wb')
#
# for texto in res.iter_content(200000):
#     newFile.write(texto)
#
# newFile.close()
#
# file = open('NovoArquivo.html')

htmlReq = bs4.BeautifulSoup(res.text, 'html.parser')

eventos = htmlReq.find_all('div', class_="single-event-box")

# print(type(eventos))
# print(len(eventos))

eventos_link = []
eventos_nome = []
eventos_mes = []
eventos_dia = []
eventos_local = []
eventos_hora = []

for evento in eventos:

    # LINKS
    evento_link = evento.find_all('a')
    for i in evento_link:
        link = i.get('href')  # SALVA O LINK DO EVENTO
        eventos_link.append(link)

    # NOMES
    nome = evento.find('div', class_="event-name")
    nome = nome.text #SALVA O NOME DO EVENTO
    nome = nome.split()
    nome = ' '.join(nome)
    eventos_nome.append(nome)

    # MES
    mes = evento.find('div', class_="calendar-month")
    mes = mes.text #SALVA O MES DO EVENTO
    mes = mes.split()
    mes = ' '.join(mes)
    eventos_mes.append(mes)

    # DIA
    dia = evento.find('div', class_="calendar-day")
    dia = dia.text #SALVA O DIA DO EVENTO
    dia = dia.split()
    dia = ' '.join(dia)
    eventos_dia.append(dia)

    # LOCAL
    local = evento.find('div', class_="uppercase line")
    local = local.text #SALVA LOCAL DO EVENTO
    local = local.split()
    local = ' '.join(local)
    eventos_local.append(local)

    # HORA
    hora = evento.find_all('div', {'class':'line'})
    hora = hora[1].text #SALVA HORA DO EVENTO
    hora = hora.split()
    hora = ' '.join(hora)
    eventos_hora.append(hora)


uber_eventos = pd.DataFrame({'link': eventos_link,
                        'nome': eventos_nome,
                       'mes': eventos_mes,
                       'dia': eventos_dia,
                       'local': eventos_local,
                        'hora': eventos_hora})

# print(uber_eventos.info())
# print(uber_eventos)

uber_eventos.to_csv('uber_eventos.csv')
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def findUrlsLeilao():
    try:
        html = urlopen('https://www.ludopedia.com.br/listas?v=leiloes')
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        links = bsObj.findAll("a", {"class": "item-read"})
        for link in links:
            print("Link: "+link.attrs['href'])
            findPrecosLeilao(link.attrs['href'])
    except AttributeError as e:
        return None

def findPrecosLeilao(url):
    try:
        html = urlopen(url);
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        print("Título do Leilão: "+bsObj.body.h3.get_text())
        print("Itens:")
        itens = bsObj.findAll("div", {"class": "lista-item"})
        for item in itens:
            print(item.h3.get_text())
            preco = item.find("div", {"class": "media-body"}).b
            print("Preço: "+ preco.get_text())
            #Situacao do Item
            siutacao = item.find("div", {"class": "bloco-leilao"}).find("span", {"class": "negrito"})
            print("Situação: "+ siutacao.get_text())
    except AttributeError as e:
        return None

findUrlsLeilao()        
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from models.boardgame import BoardGame
from models.leilao import Leilao


def findUrlsLeilao():
    try:
        html = urlopen('https://www.ludopedia.com.br/listas?v=leiloes')
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        links = bsObj.findAll("a", {"class": "item-read"})
        leiloes = []
        for link in links:
            leiloes.append(findPrecosLeilao(link.attrs['href']))

        for leilao in leiloes:
            print("Titulo do Leilao: {}".format(leilao.titulo))

            for board_game in leilao.board_games:
                print("Board Game: {}".format(board_game.nome))
                print("Preço: {}".format(board_game.preco))
                print("Estado: {}".format(board_game.estado))


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
        print("Lendo dados de {} ...".format(url))
        # Criando o leilao
        leilao = Leilao(bsObj.body.h3.get_text(), url)

        # Recuperando os itens do leilao
        itens = bsObj.findAll("div", {"class": "lista-item"})
        for item in itens:
            nome = item.h3.get_text()
            preco = item.find("div", {"class": "media-body"}).getText()
            estado = item.find("div", {"class": "bloco-leilao"}).find("span", {"class": "negrito"}).getText()
            leilao.adiciona_board_games(BoardGame(nome, "", preco, estado))

        print("Quantidade de BoardGames encontrados {}".format(len(leilao.board_games)))
        return leilao
    except AttributeError as e:
        return None


findUrlsLeilao()
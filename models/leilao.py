class Leilao(object):

    def __init__(self, titulo, link):
        self.__titulo = titulo
        self.__link = link
        self.__board_games = []


    @property
    def titulo(self):
        return self.__titulo

    @property
    def link(self):
        return self.__link

    @property
    def board_games(self):
        return self.__board_games

    def adiciona_board_games(self, board_game):
        self.__board_games.append(board_game)
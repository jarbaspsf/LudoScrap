class Leilao(object):

    def __init__(self, titulo, link, descricao, data_fim_leilao, hora_fim_leilao, estado_de_origem, cidade):
        self.__titulo = titulo
        self.__link = link
        self.__descricao = descricao
        self.__data_fim_leilao = data_fim_leilao
        self.__hora_fim_leilao = hora_fim_leilao
        self.__estado_de_origem = estado_de_origem
        self.__cidade = cidade
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

    @property
    def descricao(self):
        return self.__descricao

    @property
    def data_fim_leilao(self):
        return self.__data_fim_leilao

    @property
    def hora_fim_leilao(self):
        return self.__hora_fim_leilao

    @property
    def estado_de_origem(self):
        return self.__estado_de_origem

    @property
    def cidade(self):
        return self.__cidade

    def adiciona_board_games(self, board_game):
        self.__board_games.append(board_game)
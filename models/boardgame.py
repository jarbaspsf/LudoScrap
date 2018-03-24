class BoardGame(object):

    def __init__(self, nome, descricao, preco, estado):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__estado = estado


    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def estado(self):
        return self.__estado


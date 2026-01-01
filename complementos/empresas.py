from complementos.ItensDaLoja.produtos import Produto

class Empresa:
    def __init__(self, nome, dono1, dono2, id = int):
        self._nome = nome
        self._dono1 = dono1
        self._dono2 = dono2
        self._ativo = False
        self._produtos = []
        self._id = id
    @classmethod
    def adicionar_produto(produto):
        if produto isinstance Produto:
            produtos.append(produto)

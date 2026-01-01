class Produto:
    def __init__(self, nome, descricao, preco = int, id = int, id_da_empresa = int):
        self._nome = nome
        self._preco = preco
        self._id = id
        self._id_da_empresa = id_da_empresa
        self._descricao = descricao

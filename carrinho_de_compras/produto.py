class Produto:
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco
    }

    def __repr__(self):
        return f"{self._nome} - R$ {self._preco:.2f}"
    

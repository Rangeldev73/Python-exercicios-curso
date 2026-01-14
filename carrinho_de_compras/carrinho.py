from produto import Produto
import json
class Carrinho:
    def __init__(self):
         self._produtos: list[Produto] = []

    def adicionar_produto(self, produto: Produto):
        self._produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao carrinho.")

    def remover_produto(self, produto: Produto):
        if produto in self._produtos:
            self._produtos.remove(produto)
            print(f"Produto '{produto.nome}' removido do carrinho.")
        else:
            print("Produto não encontrado no carrinho.")
    
    def listar_produtos(self):
        if not self._produtos:
            print("Carrinho vazio.")
        else:
            print(f'Total de produtos: {len(self._produtos)}')
            for produto in self._produtos:
                print(f'{produto.nome} | {produto.preco}')
    
    def limpar_carrinho(self):
        if self._produtos:
            self._produtos.clear()
            print("Carrinho limpo com sucesso.")
        else:
            print("Carrinho vazio.")
        
    def mostrar_total(self):
        total = sum(produto.preco for produto in self._produtos)
        print(f"\nTotal a pagar: R$ {total:.2f}")

    def salvar_em_json(self, arquivo="carrinho.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(
            [produto.to_dict() for produto in self._produtos],
            f,
            ensure_ascii=False,
            indent=4
        )

        print("Carrinho salvo com sucesso.")

    def carregar_de_json(self, arquivo="carrinho.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            self._produtos = [
            Produto(item["nome"], item["preco"])
            for item in dados
        ]

            print("Carrinho carregado com sucesso.")

        except FileNotFoundError:
            print("Arquivo não encontrado. Carrinho iniciado vazio.")
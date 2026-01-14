from produto import Produto
from carrinho import Carrinho

carrinho = Carrinho()

while True:
    print("\n=== CARRINHO DE COMPRAS ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Mostrar total")
    print("5 - Limpar carrinho")
    print("6 - Sair")
    print("7 - Salvar carrinho")
    print("8 - Carregar carrinho")



    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        produto = Produto(nome, preco)
        carrinho.adicionar_produto(produto)

    elif opcao == "2":
        nome = input("Nome do produto para remover: ")
        produto_para_remover = None

        for produto in carrinho._produtos:
            if produto.nome == nome:
                produto_para_remover = produto
                break

        if produto_para_remover:
            carrinho.remover_produto(produto_para_remover)
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        carrinho.listar_produtos()

    elif opcao == "4":
        carrinho.mostrar_total()

    elif opcao == '5':
        carrinho.limpar_carrinho()

    elif opcao == "6":
        print("Saindo...")
        break

    elif opcao == "7":
        carrinho.salvar_em_json()

    elif opcao == "8":
        carrinho.carregar_de_json()

    else:
        print("Opção inválida.")
from listatarefa import LT
from tarefa import Tarefa

def menu():
    lista = LT()
    lista.carregar_de_json()

    while True:
        print("\n--- MENU ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Editar Tarefa")
        print("6. Salvar Lista")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descr = input("Descrição da tarefa: ")
            tarefa = Tarefa(descr)
            lista.adicionar_tarefa(tarefa)
        elif opcao == "2":
            lista.listar_tarefa()
        elif opcao == "3":
            try:
                indice = int(input("Digite o índice da tarefa que deseja concluir: "))
                lista.concluir_tarefa(indice)
            except ValueError:
                print("Erro: Digite um número inteiro.")
        elif opcao == "4":
            try:
                indice = int(input("Digite o índice da tarefa que deseja remover: "))
                lista.remover_tarefa(indice)
            except ValueError:
                print("Erro: Digite um número inteiro.")
        elif opcao == "5":
            try:
                indice = int(input("Digite o índice da tarefa que deseja editar: "))
                descr_nova = str(input("Digite a nova descrição: "))
                lista.editar_tarefa(indice, descr_nova)
            except ValueError:
                print("Erro: Digite um número inteiro.")
        elif opcao == "6":
            lista.salvar_em_json() 
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
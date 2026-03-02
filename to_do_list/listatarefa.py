from tarefa import Tarefa
import json 
class LT:
    def __init__(self, ):
        self._tarefas: list[Tarefa] = []

    def adicionar_tarefa(self, tarefa:Tarefa):
        self._tarefas.append(tarefa)
        print(f"Tarefa {tarefa} adicionada a lista")

    def listar_tarefa(self):
        if not self._tarefas:
            print("Lista vazia")
        else:
            print(f"Total de tarefas: {len(self._tarefas)}")
            for i,tarefa in enumerate(self._tarefas):
                print(f"{i} - {tarefa}")

    def remover_tarefa(self, indice: int): 
        if 0 <= indice < len(self._tarefas):
            removida = self._tarefas.pop(indice)
            print(f"Tarefa '{removida.descr}' removida.")
        else:
            print("Erro: Índice inexistente.")

    def concluir_tarefa(self, indice: int): 
        if 0 <= indice < len(self._tarefas):
            self._tarefas[indice].concluir()
            print("Tarefa concluída.")
        else:
            print("Índice inválido.")

    def editar_tarefa(self, indice: int, nova_descr: str):
        if indice < 0 or indice >= len(self._tarefas):
            print ( "Índice inválido." )
        else:
            tarefa = self._tarefas[indice]
            tarefa.editar_descr( nova_descr)
            print( "Tarefa editada com sucesso.") 

    def salvar_em_json(self, arquivo="listadetarefas.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(
            [tarefa.to_dict() for tarefa in self._tarefas],
            f,
            ensure_ascii=False,
            indent=4
        )

        print("Lista salva com sucesso.")

    def carregar_de_json(self, arquivo="listadetarefas.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            self._tarefas = []

            for item in dados:
                tarefa = Tarefa(item["descr"])
                if item["status"] is True:
                    tarefa.concluir()
                self._tarefas.append(tarefa)

            print("Lista carregada com sucesso.")

        except FileNotFoundError:
            print("Arquivo não encontrado. Lista iniciada vazia.")

    
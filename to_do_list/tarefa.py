class Tarefa:
    def __init__(self, descr):
        self._descr = descr
        self._status = False

    @property
    def descr(self):
        return self._descr
    
    @property
    def status(self):
        return self._status

    def editar_descr(self, nova_descr):
        self._descr = nova_descr

    def concluir(self):
        self._status = True
    
    def to_dict(self):
        return {
            "descr": self.descr,
            "status": self.status
    }

    def __repr__(self):
        status = "x" if self.status else " "
        return f'[{status}] {self.descr}'
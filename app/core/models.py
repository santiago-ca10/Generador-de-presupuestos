class Presupuesto:
    def __init__(self, proyecto, horas, valor_hora, termino):
        self.proyecto = proyecto
        self.horas = horas
        self.valor_hora = valor_hora
        self.termino = termino

    @property
    def total(self):
        return self.horas * self.valor_hora

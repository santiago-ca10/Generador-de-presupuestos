from datetime import datetime
import uuid

class Presupuesto:
    def __init__(
        self,
        proyecto,
        horas,
        valor_hora,
        termino,
        cliente_nombre,
        cliente_empresa="",
        cliente_email="",
        descripcion=""
    ):
        self.id = str(uuid.uuid4())[:8]
        self.fecha = datetime.now().strftime("%d/%m/%Y")

        self.proyecto = proyecto
        self.horas = horas
        self.valor_hora = valor_hora
        self.termino = termino

        self.cliente_nombre = cliente_nombre
        self.cliente_empresa = cliente_empresa
        self.cliente_email = cliente_email
        self.descripcion = descripcion

    @property
    def subtotal(self):
        return self.horas * self.valor_hora

    @property
    def iva(self):
        return self.subtotal * 0.19

    @property
    def total(self):
        return self.subtotal + self.iva

    def to_dict(self):
        return self.__dict__
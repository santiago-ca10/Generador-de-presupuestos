from app.core.models import Presupuesto
from app.core.pdf_service import PDFService

def run():
    try:
        proyecto = input("Proyecto: ")
        horas = float(input("Horas: "))
        valor_hora = float(input("Valor hora (USD): "))
        termino = int(input("Duración (meses): "))

        presupuesto = Presupuesto(proyecto, horas, valor_hora, termino)

        servicio = PDFService()
        servicio.generar(presupuesto)

        print("✅ PDF generado correctamente")

    except ValueError:
        print("❌ Error en los datos")

if __name__ == "__main__":
    run()
from fpdf import FPDF

class PDFService:
    def generar(self, presupuesto: object, filename="presupuesto.pdf"):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Presupuesto de Proyecto", ln=True)

        pdf.ln(10)

        pdf.set_font("Arial", size=12)

        pdf.cell(0, 10, f"Proyecto: {presupuesto.proyecto}", ln=True)
        pdf.cell(0, 10, f"Horas estimadas: {presupuesto.horas}", ln=True)
        pdf.cell(0, 10, f"Valor por hora: ${presupuesto.valor_hora:,}", ln=True)
        pdf.cell(0, 10, f"Duración: {presupuesto.termino} meses", ln=True)

        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"TOTAL: ${presupuesto.total:,}", ln=True)

        pdf.output(filename)
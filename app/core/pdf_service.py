from fpdf import FPDF
from datetime import datetime

class PDFService:
    def generar(self, p, ruta):
        pdf = FPDF()
        pdf.add_page()

        # HEADER
        pdf.set_font("Arial", "B", 20)
        pdf.cell(0, 10, "PRESUPUESTO", ln=True, align="C")

        pdf.ln(5)

        # Línea
        pdf.set_draw_color(100, 100, 100)
        pdf.line(10, 25, 200, 25)

        pdf.ln(10)

        # INFO PROYECTO
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "DETALLES DEL PROYECTO", ln=True)

        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"Proyecto: {p.proyecto}", ln=True)
        pdf.cell(0, 8, f"Horas estimadas: {p.horas}", ln=True)

        pdf.ln(5)

        # TABLA (🔥 esto lo hace ver PRO)
        pdf.set_font("Arial", "B", 11)

        pdf.cell(80, 8, "Concepto", border=1)
        pdf.cell(40, 8, "Cantidad", border=1)
        pdf.cell(70, 8, "Valor", border=1, ln=True)

        pdf.set_font("Arial", size=11)

        pdf.cell(80, 8, "Horas de trabajo", border=1)
        pdf.cell(40, 8, str(p.horas), border=1)
        pdf.cell(70, 8, f"${p.valor_hora:,}", border=1, ln=True)

        pdf.ln(5)

        # TOTAL
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"TOTAL: ${p.total:,}", ln=True, align="R")
        
        pdf.cell(0, 8, f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", ln=True)
        #pdf.cell(0, 8, f"Empresa: {config['company']}", ln=True)

        pdf.output(ruta)
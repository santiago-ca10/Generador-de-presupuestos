from fpdf import FPDF

class PDFService:
    def generar(self, p, ruta):
        pdf = FPDF()
        pdf.add_page()

        # HEADER
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Presupuesto #{p.id}", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"Fecha: {p.fecha}", ln=True)

        pdf.ln(5)

        # CLIENTE
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, "Cliente", ln=True)

        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"Nombre: {p.cliente_nombre}", ln=True)
        pdf.cell(0, 8, f"Empresa: {p.cliente_empresa}", ln=True)
        pdf.cell(0, 8, f"Email: {p.cliente_email}", ln=True)

        pdf.ln(5)

        # PROYECTO
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, "Proyecto", ln=True)

        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"Nombre: {p.proyecto}", ln=True)
        pdf.cell(0, 8, f"Horas: {p.horas}", ln=True)
        pdf.cell(0, 8, f"Valor por hora: ${p.valor_hora:,.0f}", ln=True)
        pdf.cell(0, 8, f"Duración: {p.termino} meses", ln=True)

        pdf.ln(5)

        # DESCRIPCIÓN
        pdf.cell(0, 8, f"Descripción: {p.descripcion}", ln=True)

        pdf.ln(5)

        # TOTALES
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"Subtotal: ${p.subtotal:,.0f}", ln=True)
        pdf.cell(0, 8, f"IVA (19%): ${p.iva:,.0f}", ln=True)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"TOTAL: ${p.total:,.0f}", ln=True)

        pdf.output(ruta)
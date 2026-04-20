import customtkinter as ctk
from tkinter import filedialog, messagebox

from app.core.models import Presupuesto
from app.core.pdf_service import PDFService


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Generador de Presupuestos")
        self.geometry("400x600")

        self.create_widgets()

    def create_widgets(self):

        # CLIENTE
        self.entry_cliente = ctk.CTkEntry(self, placeholder_text="Cliente")
        self.entry_cliente.pack(pady=5)

        self.entry_empresa = ctk.CTkEntry(self, placeholder_text="Empresa")
        self.entry_empresa.pack(pady=5)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack(pady=5)

        # PROYECTO
        self.entry_proyecto = ctk.CTkEntry(self, placeholder_text="Proyecto")
        self.entry_proyecto.pack(pady=5)

        self.entry_horas = ctk.CTkEntry(self, placeholder_text="Horas")
        self.entry_horas.pack(pady=5)

        self.entry_valor = ctk.CTkEntry(self, placeholder_text="Valor por hora")
        self.entry_valor.pack(pady=5)

        self.entry_termino = ctk.CTkEntry(self, placeholder_text="Duración (meses)")
        self.entry_termino.pack(pady=5)

        self.entry_descripcion = ctk.CTkEntry(self, placeholder_text="Descripción")
        self.entry_descripcion.pack(pady=5)

        # BOTÓN
        self.btn_generar = ctk.CTkButton(
            self,
            text="Generar y Guardar PDF",
            command=self.generar_pdf
        )
        self.btn_generar.pack(pady=20)

    def generar_pdf(self):
        try:
            presupuesto = Presupuesto(
                proyecto=self.entry_proyecto.get(),
                horas=float(self.entry_horas.get()),
                valor_hora=float(self.entry_valor.get()),
                termino=int(self.entry_termino.get()),
                cliente_nombre=self.entry_cliente.get(),
                cliente_empresa=self.entry_empresa.get(),
                cliente_email=self.entry_email.get(),
                descripcion=self.entry_descripcion.get()
            )

            ruta = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                title="Guardar presupuesto"
            )

            if not ruta:
                return

            PDFService().generar(presupuesto, ruta)

            messagebox.showinfo("Éxito", "PDF generado correctamente")

        except ValueError:
            messagebox.showerror("Error", "Revisa los datos ingresados")
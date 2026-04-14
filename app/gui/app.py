import tkinter as tk
from tkinter import filedialog, messagebox

from app.core.models import Presupuesto
from app.core.pdf_service import PDFService


def generar_pdf():
    try:
        presupuesto = Presupuesto(
            entry_proyecto.get(),
            float(entry_horas.get()),
            float(entry_valor.get()),
            int(entry_termino.get())
        )

        # Ventana para guardar archivo
        ruta = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Guardar presupuesto como"
        )

        if not ruta:
            return

        servicio = PDFService()
        servicio.generar(presupuesto, ruta)

        messagebox.showinfo("Éxito", "PDF generado correctamente")

    except ValueError:
        messagebox.showerror("Error", "Datos inválidos")


# Ventana principal
root = tk.Tk()
root.title("Generador de Presupuestos")
root.geometry("300x250")

# Inputs
tk.Label(root, text="Proyecto").pack()
entry_proyecto = tk.Entry(root)
entry_proyecto.pack()

tk.Label(root, text="Horas").pack()
entry_horas = tk.Entry(root)
entry_horas.pack()

tk.Label(root, text="Valor por hora").pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

tk.Label(root, text="Duración (meses)").pack()
entry_termino = tk.Entry(root)
entry_termino.pack()

# Botón
tk.Button(root, text="Generar y Guardar PDF", command=generar_pdf).pack(pady=10)

root.mainloop()
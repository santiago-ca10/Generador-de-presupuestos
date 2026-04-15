import customtkinter as ctk
from app.core.i18n import get_texts
from app.gui.settings_window import SettingsWindow

texts = get_texts()

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(texts["title"])
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        self.entry_proyecto = ctk.CTkEntry(self, placeholder_text=texts["proyecto"])
        self.entry_proyecto.pack(pady=10)

        self.entry_horas = ctk.CTkEntry(self, placeholder_text=texts["horas"])
        self.entry_horas.pack(pady=10)

        self.entry_valor = ctk.CTkEntry(self, placeholder_text=texts["valor_hora"])
        self.entry_valor.pack(pady=10)

        self.entry_termino = ctk.CTkEntry(self, placeholder_text=texts["termino"])
        self.entry_termino.pack(pady=10)

        self.btn_generar = ctk.CTkButton(self, text=texts["generar"])
        self.btn_generar.pack(pady=20)

        self.btn_settings = ctk.CTkButton(self, text="⚙️", command=self.open_settings)
        self.btn_settings.pack(pady=10)

    def open_settings(self):
        SettingsWindow(self)
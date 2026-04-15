import customtkinter as ctk
from app.core.config import load_config, save_config

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Configuración")
        self.geometry("300x250")

        self.config_data = load_config()

        # Idioma
        self.lang_option = ctk.CTkOptionMenu(
            self, values=["es", "en"]
        )
        self.lang_option.set(self.config_data["language"])
        self.lang_option.pack(pady=10)

        # Tema
        self.theme_option = ctk.CTkOptionMenu(
            self, values=["dark", "light"]
        )
        self.theme_option.set(self.config_data["theme"])
        self.theme_option.pack(pady=10)

        # Guardar
        btn_save = ctk.CTkButton(self, text="Guardar", command=self.save)
        btn_save.pack(pady=20)

    def save(self):
        self.config_data["language"] = self.lang_option.get()
        self.config_data["theme"] = self.theme_option.get()

        save_config(self.config_data)
        self.destroy()
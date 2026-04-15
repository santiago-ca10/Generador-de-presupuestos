import customtkinter as ctk
from app.core.config import load_config
from app.gui.main_window import MainWindow

config = load_config()

ctk.set_appearance_mode(config["theme"])

app = MainWindow()
app.mainloop()
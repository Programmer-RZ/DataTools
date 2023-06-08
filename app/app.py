import customtkinter as ctk

from navigation import NavigationFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DataTools")
        self.geometry("1000x700")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation = NavigationFrame(self)
        self.navigation.grid(row=0, column=0, padx=10, pady=10, sticky="EWNS")
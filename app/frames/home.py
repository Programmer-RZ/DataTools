from typing import Optional, Tuple, Union
import customtkinter as ctk

class Home(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)


        self.title = ctk.CTkLabel(self, text="DataTools", font=ctk.CTkFont(family="Times New Roman", size=50, weight="bold"))
        self.title.grid(row=0, column=0, padx=30, pady=30, sticky="W")

        self.subtitle = ctk.CTkLabel(self, text="Welcome", font=ctk.CTkFont(family="Times New Roman", size=30, slant="italic"))
        self.subtitle.grid(row=1, column=0, padx=30, sticky="W")
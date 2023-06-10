import customtkinter as ctk

class Tools(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        self.title = ctk.CTkLabel(self, text="Tools", font=ctk.CTkFont(family="Times New Roman", size=60, slant="italic"))
        self.title.grid(row=0, column=0, padx=30, pady=30, sticky="NW")



        self.description = ctk.CTkFrame(self)

        self.dlabel = ctk.CTkLabel(self.description, text="Description", font=ctk.CTkFont(size=20, weight="bold"))
        self.dlabel.grid(row=0, column=0, padx=20, pady=20)

        self.description.grid(row=1, column=1, padx=30, pady=30, sticky="EWNS")



        self.available = ctk.CTkFrame(self)

        self.alabel = ctk.CTkLabel(self.available, text="Available Tools", font=ctk.CTkFont(size=20, weight="bold"))
        self.alabel.grid(row=0, column=0, padx=20, pady=20)

        self.available.grid(row=1, column=0, padx=30, pady=30, sticky="EWNS")
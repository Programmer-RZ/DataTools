import customtkinter as ctk

class Home(ctk.CTkFrame):
    def __init__(self, window, font):
        super().__init__(window)

        self.font = font

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        self.title = ctk.CTkLabel(self, text="Home", font=ctk.CTkFont(self.font, size=60, slant="italic"))
        self.title.grid(row=0, column=0, padx=30, pady=30, sticky="NW")



        self.get_started = ctk.CTkFrame(self)

        self.gslabel = ctk.CTkLabel(self.get_started, text="Get Started", font=ctk.CTkFont(size=20, weight="bold"))
        self.gslabel.grid(row=0, column=0, padx=20, pady=20)

        self.get_started.grid(row=1, column=1, padx=30, pady=30, sticky="EWNS")



        self.recent = ctk.CTkFrame(self)

        self.rlabel = ctk.CTkLabel(self.recent, text="Recent tools", font=ctk.CTkFont(size=20, weight="bold"))
        self.rlabel.grid(row=0, column=0, padx=20, pady=20)

        self.recent.grid(row=1, column=0, padx=30, pady=30, sticky="EWNS")

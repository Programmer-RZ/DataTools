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

        self.description.grid_columnconfigure(0, weight=1)
        self.description.grid_rowconfigure(1, weight=1)

        self.textbox = ctk.CTkTextbox(self.description)
        self.textbox.grid(row=1, column=0, padx=20, pady=20, sticky="EWNS")

        self.description.grid(row=1, column=1, padx=30, pady=30, sticky="EWNS")



        self.available = ctk.CTkFrame(self)
        self.available.grid_columnconfigure(0, weight=1)
        self.available.grid_rowconfigure(1, weight=1)

        self.availableLabel = ctk.CTkLabel(self.available, text="Available Tools", font=ctk.CTkFont(size=20, weight="bold"))
        self.availableLabel.grid(row=0, column=0, padx=20, pady=20)

        self.availToolsFrame = ctk.CTkFrame(self.available)

        with open("../tools/alltools.txt", "r") as tools:
            for t in tools.readlines():
                ctk.CTkButton(self.availToolsFrame, height=40, border_spacing=10, 
                                         text=t,
                                         fg_color = "transparent",
                                         text_color=("gray10", "gray90"), 
                                         hover_color=("gray70", "gray30"),
                                         font=ctk.CTkFont(size=20),
                                         command=lambda : self.setDescription(t)).grid(padx=20, pady=20)
        
        self.availToolsFrame.grid(row=1, column=0, padx=20, pady=20, sticky="EWNS")

        self.available.grid(row=1, column=0, padx=30, pady=30, sticky="EWNS")
    
    def setDescription(self, name):
        with open(f"../tools/{name}/README.md", "r") as readme:
            for l, text in enumerate(readme.readlines()):
                self.textbox.insert(str(l+1)+".0", text)
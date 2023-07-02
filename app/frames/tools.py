import customtkinter as ctk

import subprocess

class Tools(ctk.CTkFrame):
    def __init__(self, window, font):
        super().__init__(window)

        self.font = font
        self.currentTool = None

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        self.title = ctk.CTkLabel(self, text="Tools", font=ctk.CTkFont(self.font, size=60, slant="italic"))
        self.title.grid(row=0, column=0, padx=30, pady=30, sticky="NW")


        # details frame
        # when user click on tool
        # show the details here
        self.details = ctk.CTkFrame(self)
        self.details.grid_columnconfigure(0, weight=1)
        self.details.grid_rowconfigure(1, weight=1)


        # label
        label = ctk.CTkLabel(self.details, text="Details", font=ctk.CTkFont(self.font, size=20, weight="bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        # details textbox
        self.dtextbox = ctk.CTkTextbox(self.details, font=ctk.CTkFont(self.font, size=16))
        self.dtextbox.grid(row=1, column=0, padx=20, pady=20, sticky="EWNS")
        # make textbox read only
        self.dtextbox.configure(state="disabled")

        self.runbutton = ctk.CTkButton(self.details, height=40, border_spacing=10, 
                                         text="Run tool",
                                         font=ctk.CTkFont(self.font, size=20),
                                         command=self.runTool)
        self.runbutton.grid(row=2, column=0, padx=20, pady=20, sticky="EWNS")


        self.details.grid(row=1, column=1, padx=30, pady=30, sticky="EWNS")



        # menu of all tools
        self.menu = ctk.CTkFrame(self)
        self.menu.grid_columnconfigure(0, weight=1)
        self.menu.grid_rowconfigure(1, weight=1)

        # label
        label = ctk.CTkLabel(self.menu, text="Available Tools", font=ctk.CTkFont(self.font, size=20, weight="bold"))
        label.grid(row=0, column=0, padx=20, pady=20)


        self.menuTools = ctk.CTkFrame(self.menu)
        self.menuTools.grid_columnconfigure(0, weight=1)

        # open file with all the tools name
        with open("../tools/alltools.txt", "r") as tools:
            for t in tools.read().split(","):
                # create temporary button
                b = ctk.CTkButton(self.menuTools, border_spacing=10, 
                                         text=t,
                                         font=ctk.CTkFont(self.font, size=20),
                                         command=lambda : self.setdetails(t)
                                         )
                b.grid(pady=10, sticky="EW")
        
        self.menuTools.grid(row=1, column=0, padx=20, pady=20, sticky="EWNS")


        self.menu.grid(row=1, column=0, padx=30, pady=30, sticky="EWNS")
    
    def setdetails(self, name):
        self.currentTool = name

        self.dtextbox.configure(state="normal")

        self.dtextbox.delete("1.0", ctk.END)
        with open(f"../tools/{name}/README.md", "r") as readme:
            for l, text in enumerate(readme.readlines()):
                self.dtextbox.insert(str(l+1)+".0", text)
        
        self.dtextbox.configure(state="disabled")
    
    def runTool(self):
        if self.currentTool:
            subprocess.Popen(["python", "main.py"], cwd=f"../tools/{self.currentTool}/src")

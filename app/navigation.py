import customtkinter as ctk
import os

from PIL import Image

class NavigationFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)

        # title

        self.title = ctk.CTkLabel(self, 
            text="DataTools", 
            font=ctk.CTkFont(family="Times New Roman", size=40, weight="bold")
        )
        self.title.grid(row=0, column=0, padx=20, pady=20)

        # buttons
        self.home_button = ctk.CTkButton(self, height=40, border_spacing=10, 
                                         text="Home",
                                         fg_color = "transparent",
                                         text_color=("gray10", "gray90"), 
                                         hover_color=("gray70", "gray30"),
                                         anchor="W",
                                         font=ctk.CTkFont(family="Times New Roman", size=20),
                                         command=lambda : self.switchto("home", window)
        )
        self.home_button.grid(row=1, column=0, sticky="EW")
    
    def switchto(self, name, mainwindow):
        if name == "home":
            mainwindow.currentFrame = mainwindow.home
        
        mainwindow.currentFrame.grid(row=0, column=1, padx=10, pady=10, sticky="EWNS")


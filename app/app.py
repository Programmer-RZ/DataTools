import customtkinter as ctk

from navigation import NavigationFrame

from frames.empty import Empty
from frames.home import Home

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DataTools")
        self.geometry("800x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # frames
        self.empty = Empty(self)
        self.home = Home(self)


        self.currentFrame = self.empty
        self.currentFrame.grid(row=0, column=1, padx=10, pady=10, sticky="EWNS")


        self.navigation = NavigationFrame(self)
        self.navigation.grid(row=0, column=0, padx=10, pady=10, sticky="EWNS")
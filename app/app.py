import customtkinter as ctk

from navigation import NavigationFrame

from frames.home import Home
from frames.tools import Tools

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DataTools")
        self.iconbitmap("../res/logo.ico")

        width = self.winfo_screenwidth() * 0.9
        height = self.winfo_screenheight() * 0.9
        self.geometry("%dx%d+%d+%d" % (width, height, 0, 0))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # frames
        self.home = Home(self)
        self.tools = Tools(self)


        self.currentFrame = self.home
        self.currentFrame.grid(row=0, column=1, padx=10, pady=10, sticky="EWNS")


        self.navigation = NavigationFrame(self)
        self.navigation.grid(row=0, column=0, padx=10, pady=10, sticky="EWNS")
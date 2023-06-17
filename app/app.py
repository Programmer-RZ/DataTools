import customtkinter as ctk

from navigation import NavigationFrame

from frames.tools import Tools

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DataTools")

        width = self.winfo_screenwidth() * 0.9
        height = self.winfo_screenheight() * 0.9
        self.geometry("%dx%d+%d+%d" % (width, height, 0, 0))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # frames
        self.font = "Cascadia Mono"
        self.tools = Tools(self, self.font)


        self.currentFrame = self.tools
        self.currentFrame.grid(row=0, column=1, padx=10, pady=10, sticky="EWNS")


        self.navigation = NavigationFrame(self, self.font)
        self.navigation.grid(row=0, column=0, padx=10, pady=10, sticky="EWNS")
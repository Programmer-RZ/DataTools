import customtkinter as ctk

from PIL import Image

class NavigationFrame(ctk.CTkFrame):
    def __init__(self, window, font):
        super().__init__(window)

        self.window = window
        self.font = font


        # title
        self.title = ctk.CTkLabel(self, 
            text="DataTools", 
            font=ctk.CTkFont(self.font, size=40, weight="bold")
        )
        self.title.grid(row=0, column=0, padx=20, pady=20)


        # buttons
        self.tools_button = ctk.CTkButton(self, height=40, border_spacing=10, 
                                         text="Tools",
                                         fg_color = "transparent",
                                         text_color=("gray10", "gray90"), 
                                         hover_color=("gray70", "gray30"),
                                         font=ctk.CTkFont(self.font, size=20),
                                         command=lambda : self.switchto("tools")
        )
        self.tools_button.grid(row=2, column=0, sticky="EW")
        
    
    def switchto(self, name):
        self.window.currentFrame.grid_forget()

        if name == "tools":
            self.window.currentFrame = self.window.tools
        
        self.window.currentFrame.grid(row=0, column=1, padx=10, pady=10, sticky="EWNS")


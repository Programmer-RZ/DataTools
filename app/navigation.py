from typing import Optional, Tuple, Union
import customtkinter as ctk

from PIL import Image

class NavigationFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)

        self.home_image = ctk.CTkImage(
            light_image=Image.open("../res/home.png"),
            dark_image=Image.open("../res/home.png"),
            size=(20, 20)
        )
        self.home_button = ctk.CTkButton(self, height=40, border_spacing=10, 
                                         text="Home",
                                         fg_color = "transparent",
                                         image=self.home_image,
                                         anchor="W"
                                         )


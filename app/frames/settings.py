import customtkinter as ctk

class Settings(ctk.CTkFrame):
    def __init__(self, window, font):
        super().__init__(window)

        self.font = font

        self.appearance_button = ctk.CTkOptionMenu(self, height=40, values=["Dark", "Light", "System"],
                  font=ctk.CTkFont(self.font, size=20),
                          command=lambda new_mode : ctk.set_appearance_mode(new_mode)
                          )
        self.appearance_button.grid(row=3, column=0, padx=20, pady=20, sticky="EWS")
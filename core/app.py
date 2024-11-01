import customtkinter as ctk

class App:

    def __init__(self):
        self.root = ctk.CTk()

        # self.service_storage = service_storage
        self.geometry = self.root.geometry("600x400")
        self.title = self.root.title("Tomato timer")

        # add widgets to app
        self.button = ctk.CTkButton(self.root, text='Нажми меня!', command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)
        self.label = ctk.CTkLabel(self.root, text="CTkLabel", fg_color="transparent")
        self.label.grid(row=0, column=1, padx=20, pady=10)
        # add methods to app

    def button_click(self):
        self.label.configure(text='новый текст')





from modules.app import App
import customtkinter


def main():

    root = customtkinter.CTk()
    app = App(root)
    app.root.geometry("600x400")
    app.root.mainloop()


if __name__ == "__main__":
    main()







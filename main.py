from core.app import App
import customtkinter
import modules.storage
import modules.timer as timer

def main():


    app = App()
    # app.root.geometry("600x400")
    # app.root.title("Tomato timer")
    # # timer = modules.timer.Timer()
    app.root.mainloop()
    app.service_storage.save() # вот такое сохранение норма?


if __name__ == "__main__":
    main()
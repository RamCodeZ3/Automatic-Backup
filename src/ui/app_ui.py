import customtkinter
from ui.dashboard.dashboard import DashBoard

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.title("Primera ejecución")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.geometry("1000x550")

        self.dashboard_frame = DashBoard(self)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()

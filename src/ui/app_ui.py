import customtkinter
from ui.dashboard.dashboard import DashBoard
from ui.form_backup.form_backup import FormBackup


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.title("Administracion de Backup")
        self.geometry("1000x550")

        # Configuración del grid principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # TabView principal
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Crear pestañas
        self.tabview.add("Dashboard")
        self.tabview.add("Backup")

        # Configurar grid en cada tab
        self.tabview.tab("Dashboard").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Dashboard").grid_columnconfigure(0, weight=1)

        self.tabview.tab("Backup").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Backup").grid_columnconfigure(0, weight=1)

        self.dashboard_frame = DashBoard(self.tabview.tab("Dashboard"))
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")

        self.form_backup_frame = FormBackup(self.tabview.tab("Backup"))
        self.form_backup_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()

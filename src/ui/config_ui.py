import customtkinter as ctk


def run_ui():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Primera ejecución")
    app.geometry("300x150")

    label = ctk.CTkLabel(app, text="Pantalla de prueba")
    label.pack(pady=20)

    def finish():
        app.destroy()

    button = ctk.CTkButton(app, text="Continuar", command=finish)
    button.pack(pady=10)

    app.mainloop()

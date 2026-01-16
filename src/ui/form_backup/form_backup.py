import customtkinter
from tkinter import filedialog
from model.backup_model import BackupModel
from service.database_service import DatabaseService


class FormBackup(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Grid principal
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=0)

        self.label_name = customtkinter.CTkLabel(self, text="Nombre")
        self.label_name.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0))

        self.input_name = customtkinter.CTkEntry(
            self,
            placeholder_text="Nombre de la copia de seguridad"
        )
        self.input_name.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(5, 15)
        )

        self.input_source = customtkinter.CTkEntry(
            self,
            placeholder_text="Seleccionar archivo o carpeta"
        )
        self.input_source.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=(10, 5),
            pady=10
        )

        self.btn_source = customtkinter.CTkButton(
            self,
            text="Buscar",
            command=self.select_source
        )
        self.btn_source.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=(5, 10),
            pady=10
        )

        self.input_dest = customtkinter.CTkEntry(
            self,
            placeholder_text="Seleccionar destino"
        )
        self.input_dest.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=(10, 5),
            pady=10
        )

        self.btn_dest = customtkinter.CTkButton(
            self,
            text="Buscar",
            command=self.select_dest
        )
        self.btn_dest.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=(5, 10),
            pady=10
        )

        self.label_type = customtkinter.CTkLabel(self, text="Tipo de backup")
        self.label_type.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10,
            pady=(15, 5)
        )

        self.option_type = customtkinter.CTkOptionMenu(
            self,
            values=["monthly", "weekly", "daily"]
        )
        self.option_type.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10
        )

        self.btn_create = customtkinter.CTkButton(
            self,
            text="Crear",
            height=40,
            command=self.create_backup
        )
        self.btn_create.grid(
            row=6,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(20, 10)
        )

    def select_source(self):
        path = filedialog.askopenfilename() or filedialog.askdirectory()
        if path:
            self.input_source.delete(0, "end")
            self.input_source.insert(0, path)

    def select_dest(self):
        path = filedialog.askdirectory()
        if path:
            self.input_dest.delete(0, "end")
            self.input_dest.insert(0, path)

    def create_backup(self):
        service = DatabaseService()
        backup = BackupModel(
            name=self.input_name.get(),
            backup_path=self.input_source.get(),
            destination_path=self.input_dest.get(),
            frequency=self.option_type.get(),
            history_enabled=False,
            time='12:00:00'
        )
        
        service.add_backup(backup)

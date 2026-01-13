import customtkinter
import os
from service.database_service import DatabaseService
from PIL import Image

# Paths
IMAGE_BACKUP = os.path.abspath("image/backup-svgrepo-com.png")
IMAGE_TRASH = os.path.abspath("image/trash-blank-alt-svgrepo-com.png")


class BackupFrame(customtkinter.CTkFrame):
    def __init__(self, master, name: str, path: str,  **kwargs):
        super().__init__(master, **kwargs)

        # Grid config
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        image = Image.open(IMAGE_BACKUP)

        self.image = customtkinter.CTkImage(
            light_image=image,
            dark_image=image,
            size=(40, 40)
        )

        self.image_label = customtkinter.CTkLabel(
            self,
            image=self.image,
            text=""
        )
        self.image_label.grid(
            row=0,
            column=0,
            rowspan=2,
            padx=15,
            sticky="nsew"
        )

        self.title_label = customtkinter.CTkLabel(
            self, 
            text=name,
        )
        self.title_label.grid(
            row=0,
            column=1,
            sticky="w"
        )

        self.subtitle_label = customtkinter.CTkLabel(self, text=path)
        self.subtitle_label.grid(
            row=1,
            column=1,
            sticky="w"
        )

        icon_trash = Image.open(IMAGE_TRASH)

        image_trash = customtkinter.CTkImage(
            light_image=icon_trash,
            dark_image=icon_trash,
            size=(20, 20)
        )

        self.delete_button = customtkinter.CTkButton(
            self,
            text="",
            image=image_trash,
            width=32,
            fg_color="transparent",
            hover_color="#BB0000",
            text_color="white"
        )
        self.delete_button.grid(
            row=0,
            column=2,
            rowspan=2,
            padx=15,
            sticky="nsew"
        )


class ListBackupsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        db = DatabaseService()
        backups = db.get_all_backups()

        self.columnconfigure(0, weight=1)

        for index, b in enumerate(backups):
            backup_frame = BackupFrame(
                master=self,
                name=b["name"],
                path=b["backup_path"]
            )

            backup_frame.grid(
                row=index,
                column=0,
                sticky="ew",
                padx=10,
                pady=5
            )



class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.columnconfigure(0, weight=1)

        self.create_backup_btn = customtkinter.CTkButton(
            self,
            text="Crear copia de seguridad"
        )
        self.create_backup_btn.grid(
            row=0,
            column=0,
            padx=20,
            pady=15,
            sticky="e"
        )


class DashBoard(customtkinter.CTkFrame):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
        # Grid config
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=0)
            self.rowconfigure(1, weight=1)

            # Header
            self.header_frame = HeaderFrame(self)
            self.header_frame.grid(
                row=0,
                column=0,
                sticky="ew"
            )

            # Backups
            self.backups_frame = ListBackupsFrame(self)
            self.backups_frame.grid(
                row=1,
                column=0,
                padx=20,
                pady=20,
                sticky="nsew",
            )
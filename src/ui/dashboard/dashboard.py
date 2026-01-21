import customtkinter
import os
from service.database_service import DatabaseService
from model.backup_model import BackupModel
from PIL import Image

# Paths
IMAGE_BACKUP = os.path.abspath("image/backup-svgrepo-com.png")
IMAGE_TRASH = os.path.abspath("image/trash-blank-alt-svgrepo-com.png")

service = DatabaseService()

def updateView():
     return service.get_all_backups()

class DashBoard(customtkinter.CTkFrame):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            # Grid config
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=0)

            # Backups
            self.backups_frame = ListBackupsFrame(self)
            self.backups_frame.grid(
                row=1,
                column=0,
                padx=20,
                pady=20,
                sticky="nsew",
            )


class BackupFrame(customtkinter.CTkFrame):
    def __init__(
        self,
        master,
        name: str,
        path: str,
        backup_id: int,
        on_delete=None,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        self.backup_id = backup_id
        self.on_delete = on_delete

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

        self.image_label = customtkinter.CTkLabel(self, image=self.image, text="")
        self.image_label.grid(row=0, column=0, rowspan=2, padx=15, sticky="nsew")

        self.title_label = customtkinter.CTkLabel(self, text=name)
        self.title_label.grid(row=0, column=1, sticky="w")

        self.subtitle_label = customtkinter.CTkLabel(self, text=path)
        self.subtitle_label.grid(row=1, column=1, sticky="w")

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
            command=self.delete_backup
        )
        self.delete_button.grid(
            row=0,
            column=2,
            rowspan=2,
            padx=15,
            sticky="nsew"
        )

    def delete_backup(self):
        service.delete_backup_by_id(self.backup_id)
        if self.on_delete:
            self.on_delete()


class ListBackupsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.refresh()

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()

        backups = updateView()

        if not backups:
            customtkinter.CTkLabel(
                self,
                text="No hay backups configurados",
                text_color="gray"
            ).grid(pady=20)
            return

        for index, b in enumerate(backups):
            BackupFrame(
                master=self,
                name=b["name"],
                path=b["backup_path"],
                backup_id=b["id"],
                on_delete=self.refresh
            ).grid(
                row=index,
                column=0,
                sticky="ew",
                padx=10,
                pady=5
            )

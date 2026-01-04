import os
import shutil
from dotenv import load_dotenv
from service.google_drive import GoogleDrive
from datetime import datetime


load_dotenv()
ID_FOLDER = os.getenv('ID_FOLDER')
CREDENTIAL = os.getenv('JSON_KEY_FILE')


class Backup:
    def __init__(self):
        self.path = None
    
    def local_backup(self, origin: str, destination: str):
        try:
            now = datetime.now()
            backup = rf'{destination}\backup-{now.strftime("%d-%m-%Y_%H-%M-%S")}'
            
            shutil.make_archive(backup, 'zip', origin)
            
            print("Se realizo la copia de seguridad con exito")
        
        except Exception as e:
            print("Hubo un error haciendo la copia de seguridad: ", e)
    
    def google_drive_backup(self, origin):
        try:
            now = datetime.now()
            backup = rf'{os.path.expanduser("~")}\Documents\backup-{now.strftime("%d-%m-%Y_%H-%M-%S")}'
            
            shutil.make_archive(backup, 'zip', origin)
            drive = GoogleDrive(CREDENTIAL)
            drive.upload_file(backup + ".zip", ID_FOLDER)

        except Exception as e:
            print("Hubo un error haciendo la copia de seguridad: ", e)
        
        finally:
            if os.path.exists(backup + ".zip"):
                os.remove(backup + ".zip")
        


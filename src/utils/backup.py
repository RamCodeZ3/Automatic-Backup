import os
import shutil


class Backup:
    def __init__(self):
        self.path = None
    
    async def local_backup(self, origin: str, destination: str):
        try:
            files = os.listdir(path=origin)

            for f in files:
                origin_path = os.path.join(origin, f)
                destination_path = os.path.join(destination, f)

                if os.path.isfile(origin_path):
                    shutil.copy2(origin_path, destination_path)
            
            print("Se realizo la copia de seguridad con exito")
        
        except Exception as e:
            print("Hubo un error haciendo la copia de seguridad: ", e)
    
    async def drive_backup(self, origin):
        try:
            files = os.listdir(path=origin)
            # logic for upload the backup at drive

        except Exception as e:
            print("Hubo un error haciendo la copia de seguridad: ", e)
        

b = Backup()
b.local_backup("C:\\Users\\HP ELITEBOOK 840 G5\\Pictures\\PNG", "C:\\Users\\HP ELITEBOOK 840 G5\\Desktop\\backup")
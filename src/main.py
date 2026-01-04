from utils.backup import Backup


if __name__ == "__main__":
    
    b = Backup()
    b.local_backup('C:\\Users\\HP ELITEBOOK 840 G5\\Pictures\\PNG', 'C:\\Users\\HP ELITEBOOK 840 G5\\Desktop\\backup')
    b.google_drive_backup("C:\\Users\\HP ELITEBOOK 840 G5\\Pictures\\PNG") 
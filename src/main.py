from utils.backup import Backup
from service.config_service import ConfigService


if __name__ == "__main__":
    
    b = Backup()
    c = ConfigService()
    
    if c.get_key_value('backupType') == 'local':
        b.local_backup('C:\\Users\\HP ELITEBOOK 840 G5\\Pictures\\PNG', 'C:\\Users\\HP ELITEBOOK 840 G5\\Desktop\\backup')
    
    elif c.get_key_value('backupType') == 'drive':
        b.google_drive_backup("C:\\Users\\HP ELITEBOOK 840 G5\\Pictures\\PNG") 
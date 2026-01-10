from utils.backup import Backup
from service.database_service import DatabaseService
from model.backup_model import BackupModel
from ui.app_ui import App


if __name__ == "__main__":
    db = DatabaseService()
    rows = db.get_all_backups()
    print(dict(rows[0]))

    app = App()
    app.mainloop()
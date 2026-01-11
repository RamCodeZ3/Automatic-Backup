from pydantic import BaseModel
from typing import Optional


class HistoryBackupModel(BaseModel):
    history_backup_id: Optional[int] = None
    backup_id: int
    backup_name: str
    created_at: Optional[str] = None

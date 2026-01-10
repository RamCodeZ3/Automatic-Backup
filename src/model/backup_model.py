from pydantic import BaseModel
from typing import Optional


class BackupModel(BaseModel):
    backup_id: Optional[int] = None
    name: str
    backup_path: str
    destination_path: str
    frequency: str
    time: str
    day_of_week: Optional[str] = None
    day_of_month: Optional[str] = None
    history_enabled: bool

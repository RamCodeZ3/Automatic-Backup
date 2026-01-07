from pydantic import BaseModel
from typing import Optional


class Schedule(BaseModel):
    frequency: str
    time: str
    day_of_week: Optional[str] = None


class History(BaseModel):
    enabled: bool
    max_copies: int


class BackupModel(BaseModel):
    backup_id: str
    name: str
    backup_path: str
    destination_path: str
    schedule: Schedule
    history: History

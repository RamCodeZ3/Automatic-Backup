import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


class GoogleDrive:
    def __init__(self, credentials):
        self.credentials = credentials
        self.service = self._create_service()

    def _create_service(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials,
            scopes=['https://www.googleapis.com/auth/drive']
        )
        service = build('drive', 'v3', credentials=credentials)

        return service
    
    def upload_file(self, file_path, folder_id):
        file_name = os.path.basename(file_path)
        media = MediaFileUpload(file_path)

        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True
        ).execute()


from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
import io
from googleapiclient.http import MediaIoBaseUpload

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'keys.json'  # If using service account authentication
CREDENTIALS_FILE = 'credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)

def upload_document(file_path, file_name):
    file_metadata = {'name': file_name}
    media = MediaIoBaseUpload(io.FileIO(file_path, 'rb'), mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID:', file.get('id'))

def get_file():
    file_id = '1oe4VxggDUKNUHRCtvSLD5pJTcBV46p5g'
    file = service.files().get(fileId=file_id, fields='id, name, mimeType, size, modifiedTime').execute()
    print('File Name:', file.get('name'))
    print('File MIME Type:', file.get('mimeType'))
    print('File Size:', file.get('size'))
    print('Last Modified Time:', file.get('modifiedTime'))

# upload_document('path_to_your_document.docx', 'Document_Title.docx')

def check_file_exists(service, file_id):
    try:
        file = service.files().get(fileId=file_id, fields='id').execute()
        return True  # File exists
    except Exception as e:
        if 'File not found' in str(e):
            return False  # File not found
        else:
            print('An error occurred:', e)
            return None  # Error occurred

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autenticar com as credenciais do Google Drive API
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Abre o navegador para autenticar

# Inicializar o cliente do Google Drive
drive = GoogleDrive(gauth)

# ID da pasta compartilhada que você deseja verificar
folder_id = '1075FfCBwlM4m_NHZinhpH7jbPsNhIU6l'

# Função para calcular o tamanho de uma pasta no Google Drive
def get_folder_size(folder_id):
    folder = drive.CreateFile({'id': folder_id})
    folder.FetchMetadata(fields='fileSize')
    size = int(folder['fileSize'])
    return size

folder_size = get_folder_size(folder_id)
print(f"Tamanho da pasta compartilhada: {folder_size} bytes")

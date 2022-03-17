import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dir, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open (local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.BD_FHrNsT-zhRk64RAVCHewJ8ZMwL5WkXt2yawF9dolIWCpJ43AbX4EO6yJr7P577r0irX1nCFZIVH_Z-uvp0qkodvcKn3PNBdqIZZwChxcEPxw2gsrjgCa56U_JdrRSCSOTY-n9rECy'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    file_to = input("Enter the full path to upload to dropbox:")

    transferData.upload_file(file_from, file_to)

    print("The file has been moved.")

main()
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.AidXYyQpdfOvR6pQwKq2qc9_HQwzwoeKW9YIDW-5Bei8nPPiC9aEZHNrdoV2jJwi8iy5iuEiJZuWO06QDAEixvXGAXLwhb-rEvOsf8Lt34OLsf3AF5uQqL8ArxRWCQjX3-ZVmRc'
    transferData = TransferData(access_token)
    file_from = input("Enter file path")
    file_to = input("Enter full path to upload dropbox")
    transferData.upload_file(file_from,file_to)
    print("file moved")

main()
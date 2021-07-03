import dropbox

class TransferData:
    def __init__(self, access_token):
          self.access_token = access_token 
    def uploadFiles(self, file_to, file_from): 
        dbx = dropbox.Dropbox(self.access_token) 
        print("AJ") 
        with open(file_from, 'rb') as f: 
         dbx.files_upload(f.read(), file_to) 

def main(): 
        access_token = "0DNWXwlFR2cAAAAAAAAAAe-nE-ssqiO9wpmwKuOdzhySSc6UV5A-t89drsBQCaqR" 
        transfer = TransferData(access_token) 
        file_from = input("Enter the file location : ") 
        file_to = "/main.txt" 
        transfer.uploadFiles(file_to, file_from) 

main()
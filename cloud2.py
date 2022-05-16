import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)  
        file = open(file_from, 'rb')
        dbx.files_upload(file.read(), file_to)

def main():
    access_token = 'sl.BHtswIxryx8fJM2lOfWmLpyrK1xQtIlZHBVX1bYw9gqwuWiyUhsGSdtwbzIBhWp1_O_rHJoZwIXvvwBKr4n0FUmQLdsUrw8B4JxHhgX50QYBUanlAk6zTb9ZKY7N01WbtK43Do4Id3w'
    transfer_data = TransferData(access_token)

    file_from = "C:/Users/HP/Desktop/C-101/test.txt"
    file_to = '/Test/test.txt  "'  # The full path to upload the file to, including the file name

    transfer_data.upload_file(file_from, file_to)
    print("Files has been moved")

main()
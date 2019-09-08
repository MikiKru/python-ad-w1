from datetime import datetime
from os import listdir, path, chdir


class FileOperation:
    def __init__(self):
        self.direct_path = input("wprowadź adres bezpośredni (np. 'C:\\xxx' aktualna lokalizacja .): ")
        self.direct_path = self.direct_path.replace("\\","\\\\")
        chdir(self.direct_path)
        self.getDirectoryContent()

    def getDirectoryContent(self):
        print("| %30s | %10s | %25s | %25s |" % ("FILENAME", "SIZE", "CREATED TIME", "MODIFIED TIME"))
        for content in listdir("."):
            print("| %30s | %10.2f | %25s | %25s |"
                  % (content,
                     path.getsize(content)/(10**6),
                     datetime.fromtimestamp(path.getctime(content)).strftime("%d.%m.%Y %H:%M:%S"),
                     datetime.fromtimestamp(path.getmtime(content)).strftime("%d.%m.%Y %H:%M:%S"))
                  )
FileOperation()
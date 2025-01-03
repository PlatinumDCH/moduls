from abc import ABC

class Logger(ABC):
    @classmethod
    def log(self, message):
        pass

class ConsolLogger(Logger):
    def log(self, message):
        print(message)

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        with open(self.filename, 'w') as file:
            file.write(message)

        


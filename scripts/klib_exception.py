# KLIB - exception
# wykys 2021

class NotExistException(Exception):
    def __init__(self, path):
        self.error_text = f'{path} is not exist!'

    def __str__(self):
        return self.error_text


class InvalidFileFormatException(Exception):
    def __init__(self, path):
        self.error_text = f'{path} has an invalid file format!'

    def __str__(self):
        return self.error_text

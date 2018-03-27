import os
import tempfile


class FileReader:
    _path = None

    def __init__(self, file_name):
        self._path = os.path.join(tempfile.gettempdir(), file_name)

    def read(self):
        try:
            with open(self._path) as f:
                return f.read()
        except IOError:
            return ''


reader = FileReader("example.txt")

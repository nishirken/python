import tempfile
import os


class File:
    def __init__(self, path):
        self.path = path

    def __add__(self, other):
        final_string = None
        str_path = os.path.join(tempfile.gettempdir(), 'new_file')
        with open(self.path, 'r') as f:
            final_string = f.read()

        with open(other.path, 'r') as f1:
            in_file = f1.read()
            final_string += in_file

        with open(str_path, 'w') as f2:
            f2.write(final_string)

        return File(str_path)

    def __iter__(self):
        with open(self.path, 'r') as f:
            string = f.read()
            for x in string.split('\n'):
                yield x

    def __str__(self):
        return self.path

    def write(self, string):
        with open(self.path, 'w') as f:
            f.write(string)

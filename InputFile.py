from AbstractFile import AbstractFile


class InputFile(AbstractFile):
    """Concreate class.
    Used to create a text input file object"""

    def _open(self):
        self.file = open(self.name)

    def read(self):
        self._open()
        ctx = self.file.read()
        self._close()
        return ctx

    def _close(self):
        self.file.close()

from OutputFileTXT import OutputFileTXT
from OutputFileCSV import OutputFileCSV


class OutputFileFactory:
    """Use Factory pattern to design which Output class to construct"""

    def __init__(self, name: str, ext: str):
        self.name = name
        self.ext = ext

    def getOutputClass(self):
        if (self.ext == ".txt"):
            return OutputFileTXT(self.name)
        elif (self.ext == ".csv"):
            return OutputFileCSV(self.name)

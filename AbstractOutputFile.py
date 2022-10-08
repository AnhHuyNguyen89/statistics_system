from AbstractFile import AbstractFile, abstractmethod


class AbstractOutputFile(AbstractFile):
    """Using Open-Closed Principle.
    Base class OutputFile is closed
    but its children can extend
    to support more output types."""

    @abstractmethod
    def write(self, in_name: str, dict: dict[str, int], in_word_count: int):
        pass

    def _open(self):
        self.file = open(self.name, "a")

    def _close(self):
        self.file.close()

    def clear(self):
        self.file = open(self.name, "w")
        self.file.close()

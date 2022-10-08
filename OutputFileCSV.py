from AbstractOutputFile import AbstractOutputFile


class OutputFileCSV(AbstractOutputFile):
    """Concreate class.
    Use this to create a CSV output file object"""

    def write(self, in_name: str, dict: dict[str, int], in_word_count: int):
        self._open()
        lst = list[str]()
        for kvp in dict:
            lst.append(f"{kvp},{dict[kvp]}")
        lst = ','.join(lst)
        self.file.write(f"{in_name},{in_word_count},{lst}\n")
        self._close()

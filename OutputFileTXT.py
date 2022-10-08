from AbstractOutputFile import AbstractOutputFile


class OutputFileTXT(AbstractOutputFile):
    """Concreate class.
    Use this to create a TXT output file object"""

    def write(self, in_name: str, dict: dict[str, int], in_word_count: int):
        self._open()
        lst = list[str]()
        for kvp in dict:
            lst.append(f"{kvp} ({dict[kvp]})")
        lst = ', '.join(lst)
        self.file.write(
            f"File {in_name} contains {in_word_count} words. Frequent words are: {lst}\n")
        self._close()

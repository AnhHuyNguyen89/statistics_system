class Summarize:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.dict: dict[str, int] = {}
        self.ignores: list[str] = []

    def ignore(self, word: str):
        """Ignore a word string.
        Must be called before summarized"""
        self.ignores.append(word)
        return self

    def summarize(self):
        for token in self.tokens:
            if token not in self.ignores:
                if token not in self.dict:
                    self.dict[token] = 1
                else:
                    self.dict[token] += 1
        return self

    def getDict(self):
        return self.dict

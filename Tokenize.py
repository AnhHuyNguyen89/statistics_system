from abc import ABC, abstractmethod


class Tokenize(ABC):
    """Open-Closed Principle.
    Base class Tokenize is closed
    but can be derived to support more ways
    of splitting string into tokens
    either by spaces or other delimiters"""

    def __init__(self, ctx: str):
        self.ctx = ctx
        self.tokens = list[str]()

    @abstractmethod
    def tokenize(self):
        return self

    def getTokenList(self):
        return self.tokens

    def getWordCount(self):
        return len(self.tokens)

    def getResults(self):
        return self.getTokenList(), self.getWordCount()

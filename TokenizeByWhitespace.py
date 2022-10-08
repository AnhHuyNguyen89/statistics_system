from Tokenize import Tokenize


class TokenizeByWhitespace(Tokenize):
    def tokenize(self):
        self.tokens = self.ctx.split()
        return self

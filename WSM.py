from InputFile import InputFile
from TokenizeByWhitespace import TokenizeByWhitespace
from Summarize import Summarize
from DictBuilder import DictBuilder
from OutputFileFactory import OutputFileFactory


class WordStatsManager:
    def __init__(self, top_n: int, in_files: tuple, out_files: dict[str, str]):
        self.top_n = top_n
        self.in_files = in_files
        self.out_files = out_files

    def process(self):
        # Empty all output files
        for name, ext in self.out_files.items():
            OutputFileFactory(name, ext).getOutputClass().clear()
        # Iterate through each input files
        for in_file in self.in_files:
            # Get content of input file
            content = InputFile(in_file).read()
            # Extract token list and word count
            tokens, word_count = TokenizeByWhitespace(
                content).tokenize().getResults()
            # Get the initial dictionary
            summary = Summarize(tokens).summarize().getDict()
            # Get a new dictionary through user's request
            trimmed = DictBuilder(summary).sortDescending(
            ).keepOnlyFirstPairs(self.top_n).getDict()
            # Export result to each output files
            for k, v in self.out_files.items():
                OutputFileFactory(k, v).getOutputClass().write(
                    in_file, trimmed, word_count)

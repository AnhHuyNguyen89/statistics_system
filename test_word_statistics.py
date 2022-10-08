import pytest
import WSM as src
import OutputFileTXT
import OutputFileCSV

# ----------------------------------------------------------------Parameters zone--------------------------------------------------------------
in_file = "in1.txt"
tokens, in_word_count = src.TokenizeByWhitespace(
    src.InputFile(in_file).read()).tokenize().getResults()
dict = src.DictBuilder(src.Summarize(
    tokens).summarize().getDict()).sortDescending().getDict()
ctx = """a a a a a 
b b b b 
c c c 
d d e f g h i j kk 
kk
"""
txt = """File in1.txt contains 22 words. Frequent words are: a (5), b (4), c (3), d (2), kk (2), e (1), f (1), g (1), h (1), i (1), j (1)
"""
csv = """in1.txt,22,a,5,b,4,c,3,d,2,kk,2,e,1,f,1,g,1,h,1,i,1,j,1
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------


def test_getTokens():
    tkl = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c',
           'c', 'd', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'kk', 'kk']
    assert src.TokenizeByWhitespace(ctx).tokenize().getTokenList() == tkl


def test_getWordCount():
    assert src.TokenizeByWhitespace(ctx).tokenize().getWordCount() == 22


def test_getDict():
    dict = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1,
            'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'kk': 2}
    assert src.Summarize(src.TokenizeByWhitespace(
        ctx).tokenize().getTokenList()).summarize().getDict() == dict


def test_sortDict():
    dict = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'kk': 2,
            'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}
    assert src.DictBuilder(src.Summarize(src.TokenizeByWhitespace(
        ctx).tokenize().getTokenList()).summarize().getDict()).getDict() == dict


def test_trimDict():
    dict = {'a': 5, 'b': 4, 'c': 3}
    assert src.DictBuilder(src.Summarize(src.TokenizeByWhitespace(
        ctx).tokenize().getTokenList()).summarize().getDict()).keepOnlyFirstPairs(3).getDict() == dict


def test_getFileContent():
    print(repr(src.InputFile(in_file).read()))
    print(repr(ctx))
    assert src.InputFile(in_file).read() == ctx


def test_writeFileContent():
    OutputFileTXT.OutputFileTXT("out.txt").clear()
    OutputFileCSV.OutputFileCSV("out.csv").clear()
    OutputFileTXT.OutputFileTXT("out.txt").write(in_file, dict, in_word_count)
    OutputFileCSV.OutputFileCSV("out.csv").write(in_file, dict, in_word_count)

    assert (src.InputFile("out.txt").read() == txt) and (
        src.InputFile("out.csv").read() == csv)


def test_fileFactory():
    OutputFileTXT.OutputFileTXT("out.txt").clear()
    OutputFileCSV.OutputFileCSV("out.csv").clear()
    src.OutputFileFactory("out.txt", ".txt").getOutputClass().write(
        in_file, dict, in_word_count)
    src.OutputFileFactory("out.csv", ".csv").getOutputClass().write(
        in_file, dict, in_word_count)
    assert (src.InputFile("out.txt").read() == txt) and (
        src.InputFile("out.csv").read() == csv)


pytest.main(["-x", "test_word_statistics.py", "-v"])

# test_getFileContent()
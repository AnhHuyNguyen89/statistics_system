class DictBuilder:
    """Using Single-Responsibility Principle.
    Use this class to specifically
    modify a dictionary instead of 
    cluttering Summarize class"""

    def __init__(self, olddict):
        # Deep copy entire dictionary instead of referencing same memory object
        self.newdict: dict[str, int] = dict(olddict)

    """Also using Builder pattern 
    to cater the dictionary into user's request
    instead of relying on constructor parameters"""

    def sortAscending(self):
        self.newdict = dict(
            sorted(self.newdict.items(), key=lambda item: item[1]))
        return self

    def sortDescending(self):
        self.newdict = dict(
            sorted(self.newdict.items(), key=lambda item: item[1], reverse=True))
        return self

    def keepOnlyFirstPairs(self, top_n=1):
        self.newdict = {k: self.newdict[k]
                        for k in list(self.newdict)[:top_n]}
        return self

    def getDict(self):
        return self.newdict

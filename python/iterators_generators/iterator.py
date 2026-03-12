class LogFileIterator:

    def __init__(self, fname):
        self.file = open(fname)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()

        if not line: 
            self.file.close()
            raise StopIteration

        return line

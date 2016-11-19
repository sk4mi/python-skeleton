import argparse

class Options:

    def __init__(self):
        self.__init__parser()

    def __init__parser(self):
        usage = 'bin/project'
        self.parser = argparse.ArgumentParser(usage=usage)
        self.parser = argparse.ArgumentParser(description="skeleton python project")
        self.parser.add_argument("-v", "--verbose", help="increase verbosity level", action="store_true")
        self.parser.add_argument("-d", "--debug", help="output debug information", action="store_true")
    def parse(self, args=None):
        return self.parser.parse_args(args)

import pathlib
import os

class Util:
    """Utilities class."""

    @staticmethod
    def parse_file_array(file):
        return Util.read_file_lines(file) 

    @staticmethod
    def parse_file_dictionary(file):
        dictionary = {}
        lines = Util.read_file_lines(file)
        for line in lines:
            parts = line.split(":")
            dictionary[parts[0]] = parts[1]
        return dictionary

    @staticmethod
    def read_file_lines(file):
        with open(os.fspath(pathlib.Path(__file__).parent.parent.resolve()) + f"/{file}", "r") as f:
            lines = [ l[:-1] for l in f.readlines() ]
        return lines



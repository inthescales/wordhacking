import collections
import getopt
import re
import sys

# Helpers ---------------------------------------------------------------------

class Entry():
    """Data structure representing an entry in the CMUDict data."""
    def __init__(self, term, number, codes):
        self.term = term
        self.number = number
        self.codes = codes

def parse_line(line):
    """Parse a single line of CMUDict and return it as an Entry model"""

    if line.startswith(";;;"):
        return None

    result = re.search("(.+?)(\\((\\d+)\\))? +(.*)", line)

    term = str(result.group(1)).replace("\"", "\\\"")
    number = result.group(3)
    codes = result.group(4).split(" ")

    return Entry(term, number, codes)

# Process file ----------------------------------------------------------------

def as_dict(path):
    """
    Read the CMUDict data as a dictionary mapping from a term string to a list
    of arrays of code strings.
    """

    result_dict = collections.defaultdict(list)
    with open(path, mode='r', encoding='latin-1') as in_file:
        for line in in_file:
            entry = parse_line(line)

            # Ignore lines that don't contain a term
            if entry == None:
                continue

            result_dict[entry.term].append(entry.codes)

    return result_dict

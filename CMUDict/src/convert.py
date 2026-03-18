import getopt
import re
import sys

from enum import IntEnum

import gen_am as gen_am
from overrides import override_for

# Output types ----------------------------------------------------------------

class OutputFormat:
    """
    Data structure containing strings and string builders for outputting data
    in a specified format.
    """
    def __init__(self, head, line, separator, tail):
        self.head = head
        self.line = line
        self.separator = separator
        self.tail = tail

# JSON output format
output_json = OutputFormat(
    head="{",
    line=lambda term, phonemes: f'\t"{term}": ["{'", "'.join(phonemes)}"]',
    separator=",",
    tail="}"
)

# Phoneme formats -------------------------------------------------------------

class PhonemeFormat(IntEnum):
    """Enum representing the desired phoneme format."""
    ARPABET = 0,
    IPA = 1

# Read arguments --------------------------------------------------------------

opts, params = getopt.getopt(sys.argv[1:], "", [])

# Path of the CMUDict data file
cmudict_path = params[0]

# Output format
output_format = output_json

# Phoneme format
phoneme_format = PhonemeFormat.IPA

# Helpers ---------------------------------------------------------------------

class Entry():
    """Data structure representing an entry in the CMUDict data."""
    def __init__(self, term, number, codes):
        self.term = term
        self.number = number
        self.codes = codes

def parse_line(line):
    if line.startswith(";;;"):
        return None

    """Parse a single line of CMUDict and return it as an Entry model"""
    result = re.search("(.+?)(\\((\\d+)\\))? +(.*)", line)

    term = str(result.group(1)).replace("\"", "\\\"")
    number = result.group(3)
    codes = result.group(4).split(" ")

    return Entry(term, number, codes)

# Process file ----------------------------------------------------------------

with open(cmudict_path, mode='r', encoding='latin-1') as in_file:

    print(output_format.head)

    firstline = True
    for line in in_file:
        entry = parse_line(line)

        # Ignore lines that don't contain a term
        if entry == None:
            continue

        # Skip alternate pronunciations
        if entry.number != None:
            continue

        # Override certain pronunciations
        override_codes = override_for(entry.term.lower())
        if override_codes != None:
            arpabet_codes = override_codes
        else:
            arpabet_codes = entry.codes

        # Convert phoneme format
        if phoneme_format == PhonemeFormat.IPA:
            phonemes = [ipa for code in arpabet_codes for ipa in gen_am.from_arpa(code, True)]
        else:
            phonemes = arpabet_codes

        if firstline:
            firstline = False
        else:
            print(output_format.separator)

        print(output_format.line(entry.term, phonemes), end="")
    
    print("\n" + output_format.tail)

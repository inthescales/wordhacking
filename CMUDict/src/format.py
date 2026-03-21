from enum import IntEnum

# Output types ----------------------------------------------------------------

class OutputFormat:
    """
    Data structure containing strings and string builders for outputting data
    in a specified format.
    """
    def __init__(self, head, line, multiline, compact_multiline, separator, tail):
        self.head = head
        self.line = line
        self.multiline = multiline
        self.compact_multiline = compact_multiline
        self.separator = separator
        self.tail = tail

# JSON output format
output_json = OutputFormat(
    head="{\n",
    line=lambda term, phonemes: f'\t"{term}": ["{'", "'.join(phonemes)}"]',
    multiline=lambda term, entries: f'\t"{term}": [\n' \
        + ',\n'.join(['\t\t[' + ", ".join([phonemes for phonemes in entry]) + "]" for entry in entries]) \
        + '\n\t]',
    compact_multiline=lambda term, phonemes: f'\t"{term}": [["{'", "'.join(phonemes)}"]]',
    separator=",\n",
    tail="}"
)

# Main ------------------------------------------------------------------------

def json(pronounce_dict):
    """Format the given pronunciation dict as JSON."""
    return to(pronounce_dict, output_json)

def to(pronounce_dict, output_format):
    """Format the given pronunciation dict in the given format."""

    output = output_format.head

    firstline = True
    for (term, entries) in pronounce_dict.items():
        if firstline:
            firstline = False
        else:
            output += output_format.separator

        if type(entries[0]) == list:
            if len(entries) > 1:
                output += output_format.multiline(term, entries)
            else:
                output += output_format.compact_multiline(term, entries[0])
        else:
            output += output_format.line(term, entries)

    output += output_format.tail

    return output

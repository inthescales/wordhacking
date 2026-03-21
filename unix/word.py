import os

# Known file paths for the Unix words file
file_paths = [
	"/usr/share/dict/words",
	"/usr/dict/words"
]

# Persistent set data structure containing the word list
word_set = None

# Setup Helpers ---------------------------------------------------------------

def _find_file():
	"""
	Check the known file paths for the Unix words file, returning the first
	that exists, or None if none is found.
	"""

	for path in file_paths:
		if os.path.exists(path):
			return path

	return None

def _read_words():
	"""
	Read the words file, populating the persistent set with its contents
	"""
	global file_paths, word_set

	if word_set is not None:
		return

	word_set = set()

	path = _find_file()

	if path is None:
		raise Exception("Unable to find Unix words file.")

	with open(path, "r") as words_file:
		for line in words_file:
			word = line.strip()
			
			word_set.add(word)

# Access ----------------------------------------------------------------------

def contains(word, case_sensitive=True):
	"""Returns True if the Unix words file contains the given word."""
	global word_set

	_read_words()

	if case_sensitive:
		return word in word_set
	else:
		return (word.lower() in word_set) or (word.title() in word_set)

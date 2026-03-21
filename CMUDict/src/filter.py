import unix.word

from enum import IntEnum

class Presets:
	contains_punctuation = lambda self, key, value: all([char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for char in key])
	in_unix_words = lambda self, key, value: unix.word.contains(key, case_sensitive=False)

presets = Presets()

def on(pronounce_dict, accept):
	"""
	Returns the given pronunciation dict after filtering it by the accept function.
	"""
	
	return {key: value for key, value in pronounce_dict.items() if accept(key, value)}

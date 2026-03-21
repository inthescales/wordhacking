from enum import IntEnum

class Presets:
	contains_punctuation = lambda self, key, value: all([char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for char in key])

presets = Presets()

def on(pronounce_dict, accept):
	return {key: value for key, value in pronounce_dict.items() if accept(key, value)}

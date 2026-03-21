# Helpers ---------------------------------------------------------------------

def parse_code(code):
	"""Parse the sound code and any stress indicator from an ARPABET code."""
	if code[-1].isdigit():
		return (code[:-1], int(code[-1]))
	else:
		return (code, None)

def reduce_unstressed(phoneme, stress):
	"""
	CMUDict's use of ARPABET doesn't distinguish between /ʌ/ and /ə/, or
	between /ɝ/ and /ɚ/.

	Convert these two reduced schwa forms if the accompanying stress value is
	0 (unstressed), or return the original phoneme unchanged if this does
	not apply.

	Assumes unstressed vowel merger (/ɨ/ not distinct from /ə/).
	"""
	if stress != 0:
		return phoneme

	match phoneme:
		case "AH":
			return "ə"
		case "ER":
			return "ɚ"

	return phoneme

def expand_rhotic(phoneme):
	"""
	Expands a rhotic vowel phoneme into a vowel followed by 'ɹ'.
	Returns non-rhotic-vowel phonemes unchanged.
	"""

	match phoneme:
		case "ɚ":
			return ["ə", "ɹ"]
		case "ɝ":
			return ["ɛ", "ɹ"]

	return phoneme

# Convert ARPABET -> IPA ------------------------------------------------------

def arpabet_to_ipa(code, reduced_schwas=True, rhotic_vowels=True):
	"""
	Convert a two-letter ARPABet code to IPA.
	Returns a list of IPA strings, with diphthongs included together in a
	single string.
	"""
	phonemes = {
		"AA": "ɑ",
		"AE": "æ",
		"AH": "ʌ",
		"AO": "ɔ",
		"AW": "aʊ",
		"AX": "ə",
		"AXR": "ɚ",
		"AY": "aɪ",
		"EH": "ɛ",
		"ER": "ɝ",
		"EY": "eɪ",
		"IH": "ɪ",
		"IX": "ɨ",
		"IY": "i",
		"OW": "oʊ",
		"OY": "ɔɪ",
		"UH": "ʊ",
		"UW": "u",
		"UX": "ʉ",
		"B": "b",
		"CH": "tʃ",
		"D": "d",
		"DH": "ð",
		"DX": "ɾ",
		"EL": "l̩",
		"EM": "m̩",
		"EN": "n̩",
		"F": "f",
		"G": "g",
		"HH": "h",
		"JH": "dʒ",
		"K": "k",
		"L": "l",
		"M": "m",
		"N": "n",
		"NG": "ŋ",
		"NX": "ɾ̃",
		"P": "p",
		"Q": "ʔ",
		"R": "ɹ",
		"S": "s",
		"SH": "ʃ",
		"T": "t",
		"TH": "θ",
		"V": "v",
		"W": "w",
		"WH": "ʍ",
		"Y": "j",
		"Z": "z",
		"ZH": "ʒ"
	}

	(sound, stress) = parse_code(code)
	
	if not sound in phonemes:
		raise Exception(f"Invalid ARPABET code '{sound}'")

	ipa = phonemes[sound]

	if reduced_schwas:
		ipa = reduce_unstressed(ipa, stress)

	if not rhotic_vowels:
		ipa = expand_rhotic(ipa)

	return [ipa] if type(ipa) is not list else ipa

def to_ipa(pronounce_dict, rhotic_vowels=True):
	result_dict = {}

	for (term, items) in pronounce_dict.items():
		if type(items[0]) is list:
			result_dict[term] = [[ipa_code for code in variant for ipa_code in arpabet_to_ipa(code, rhotic_vowels=rhotic_vowels)] for variant in items]
		else:
		    result_dict[term] = [ipa_code for code in items for ipa_code in arpabet_to_ipa(code, rhotic_vowels=rhotic_vowels)]

	return result_dict

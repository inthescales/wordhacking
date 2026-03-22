from abc import ABC
from enum import IntEnum

class PlaceOfArticulation(IntEnum):
	bilabial = 0
	labiodental = 1
	dental = 2
	alveolar = 3
	postalveolar = 4
	retroflex = 5
	palatal = 6
	velar = 7
	uvular = 8
	pharyngeal = 9
	glottal = 10
	labiovelar = 11

class MannerOfArticulation(IntEnum):
	plosive = 0
	nasal = 1
	trill = 2
	tap = 3
	fricative = 4
	affricate = 5
	lateral_fricative = 6
	approximant = 7
	lateral_approximant = 8

class Height(IntEnum):
	high = 0
	near_high = 1
	high_mid = 2
	mid = 3
	low_mid = 4
	near_low = 5
	low = 6

class Backness(IntEnum):
	back = 0
	central = 1
	front = 2

PoA = PlaceOfArticulation
MoA = MannerOfArticulation

vowel_chart = {
	Height.high:		{ Backness.front: ["i", "y"],   Backness.central: ["ɨ", "ʉ"],   Backness.back: ["ɯ", "u"] },
	Height.near_high:	{ Backness.front: ["ɪ", "ʏ"],   Backness.central: [None, None], Backness.back: [None, "ʊ"] },
	Height.high_mid:	{ Backness.front: ["e", "ø"],   Backness.central: ["ɘ", "ɵ"],   Backness.back: ["ɤ", "o"] },
	Height.mid:			{ Backness.front: [None, None], Backness.central: ["ə", None],  Backness.back: [None, None] },
	Height.low_mid:		{ Backness.front: ["ɛ", "œ"],   Backness.central: ["ɜ", "ɞ"],   Backness.back: ["ʌ", "ɔ"] },
	Height.near_low:	{ Backness.front: ["æ", None],  Backness.central: ["ɐ", "ɐ"],   Backness.back: [None, None] },
	Height.low:			{ Backness.front: ["a", "Œ"],   Backness.central: [None, None], Backness.back: ["ɑ", "ɒ"] }
}

consonant_chart = {
	MoA.plosive:   			 { PoA.bilabial: ["p", "b"],   PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: ["t", "d"],   PoA.postalveolar: [None, None], PoA.retroflex: ["ʈ", "ɖ"],   PoA.palatal: ["c", "ɟ"],   PoA.velar: ["k", "g"],   PoA.uvular: ["q", "ɢ"],   PoA.pharyngeal: ["ʡ", None],  PoA.glottal: ["ʔ", None],  PoA.labiovelar: [None, None] },
	MoA.nasal:     			 { PoA.bilabial: [None, "m"],  PoA.labiodental: [None, "ɱ"],  PoA.dental: [None, None], PoA.alveolar: [None, "n"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɳ"],  PoA.palatal: [None, "ɲ"],  PoA.velar: [None, "ŋ"],  PoA.uvular: [None, "ɴ"],  PoA.pharyngeal: [None, None], PoA.glottal: [None, None], PoA.labiovelar: [None, None] },
	MoA.trill:	   			 { PoA.bilabial: [None, "ʙ"],  PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: [None, "r"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, None], PoA.palatal: [None, None], PoA.velar: [None, None], PoA.uvular: [None, "ʀ"],  PoA.pharyngeal: [None, None], PoA.glottal: [None, None], PoA.labiovelar: [None, None] },
	MoA.tap:	   			 { PoA.bilabial: [None, None], PoA.labiodental: [None, "ⱱ"],  PoA.dental: [None, None], PoA.alveolar: [None, "ɾ"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɽ"],  PoA.palatal: [None, None], PoA.velar: [None, None], PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None], PoA.labiovelar: [None, None] },
	MoA.fricative: 		     { PoA.bilabial: ["ɸ", "β"],   PoA.labiodental: ["f", "v"],   PoA.dental: ["θ", "ð"],   PoA.alveolar: ["s", "z"],   PoA.postalveolar: ["ʃ", "ʒ"],   PoA.retroflex: ["ʂ", "ʐ"],   PoA.palatal: ["ɕ", "ʑ"],   PoA.velar: ["x", "ɣ"],   PoA.uvular: ["χ", "ʁ"],   PoA.pharyngeal: ["ħ", "ʕ"],   PoA.glottal: ["h", "ɦ"],   PoA.labiovelar: [None, None] },
	MoA.affricate: 		     { PoA.bilabial: [None, None], PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: ["ts", "dz"], PoA.postalveolar: ["tʃ", "dʒ"], PoA.retroflex: ["tʂ", "dʐ"], PoA.palatal: ["tɕ", "dʑ"], PoA.velar: ["kx", "gɣ"], PoA.uvular: ["qχ", "ɢʁ"], PoA.pharyngeal: [None, None], PoA.glottal: [None, None], PoA.labiovelar: [None, None] },
	MoA.lateral_fricative:   { PoA.bilabial: [None, None], PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: ["ɬ", "ɮ"],   PoA.postalveolar: [None, None], PoA.retroflex: [None, None], PoA.palatal: [None, None], PoA.velar: [None, None], PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None], PoA.labiovelar: [None, None] },
	MoA.approximant:	     { PoA.bilabial: [None, None], PoA.labiodental: [None, "ʋ"],  PoA.dental: [None, None], PoA.alveolar: [None, "ɹ"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɻ"],  PoA.palatal: [None, "j"],  PoA.velar: [None, "ɰ"],  PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None], PoA.labiovelar: ["ʍ", "w"] },
	MoA.lateral_approximant: { PoA.bilabial: [None, None], PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: [None, "l"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɭ"],  PoA.palatal: [None, "ʎ"],  PoA.velar: [None, "ʟ"],  PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None], PoA.labiovelar: [None, None] }
}

class Phoneme(ABC):
	@classmethod
	def sym(Self, symbol: str):
		global vowel_chart, consonant_chart

		is_long = False
		if "ː" in symbol:
			is_long = True
			symbol = symbol.replace("ː", "")

		for (height, row) in vowel_chart.items():
			for (backness, pair) in row.items():
				for rounded in [0, 1]:
					if pair[rounded] == symbol:
						return VowelPhoneme(height, backness, bool(rounded))

		for (manner, row) in consonant_chart.items():
			for (place, pair) in row.items():
				for voiced in [0, 1]:
					if pair[voiced] == symbol:
						return ConsonantPhoneme(place, manner, bool(voiced))

		raise Exception(f"No recognized phoneme with symbol '{symbol}'")

	@property
	def is_vowel(self):
		return isinstance(self, VowelPhoneme)

	@property
	def is_consonant(self):
		return isinstance(self, ConsonantPhoneme)

	@property
	def is_front(self):
		return self.is_vowel and self.backness == Backness.front

	@property
	def is_central(self):
		return self.is_vowel and self.backness == Backness.central

	@property
	def is_back(self):
		return self.is_vowel and self.backness == Backness.back

	@property
	def is_high(self):
		return self.is_vowel and self.height == Height.high

	@property
	def is_near_high(self):
		return self.is_vowel and self.height == Height.near_high

	@property
	def is_high_mid(self):
		return self.is_vowel and self.height == Height.high_mid

	@property
	def is_mid(self):
		return self.is_vowel and self.height == Height.mid

	@property
	def is_low_mid(self):
		return self.is_vowel and self.height == Height.low_mid

	@property
	def is_near_low(self):
		return self.is_vowel and self.height == Height.near_low

	@property
	def is_low(self):
		return self.is_vowel and self.height == Height.low

	@property
	def is_rounded(self):
		return self.is_vowel and self.rounded

	@property
	def is_long(self):
		return self.is_vowel and self.long

	@property
	def is_bilabial(self):
		return self.is_consonant and self.place == PoA.bilabial

	@property
	def is_labiodental(self):
		return self.is_consonant and self.place == PoA.labiodental

	@property
	def is_dental(self):
		return self.is_consonant and self.place == PoA.dental

	@property
	def is_alveolar(self):
		return self.is_consonant and self.place == PoA.alveolar

	@property
	def is_postalveolar(self):
		return self.is_consonant and self.place == PoA.postalveolar

	@property
	def is_retroflex(self):
		return self.is_consonant and self.place == PoA.retroflex

	@property
	def is_palatal(self):
		return self.is_consonant and self.place == PoA.palatal

	@property
	def is_velar(self):
		return self.is_consonant and self.place == PoA.velar

	@property
	def is_uvular(self):
		return self.is_consonant and self.place == PoA.uvular

	@property
	def is_pharyngeal(self):
		return self.is_consonant and self.place == PoA.pharyngeal

	@property
	def is_glottal(self):
		return self.is_consonant and self.place == PoA.glottal

	@property
	def is_plosive(self):
		return self.is_consonant and self.manner == MoA.plosive

	@property
	def is_nasal(self):
		return self.is_consonant and self.manner == MoA.nasal

	@property
	def is_trill(self):
		return self.is_consonant and self.manner == MoA.trill

	@property
	def is_tap(self):
		return self.is_consonant and self.manner == MoA.tap

	@property
	def is_flap(self):
		return self.is_consonant and self.manner == MoA.tap

	@property
	def is_fricative(self):
		return self.is_consonant and self.manner in [MoA.fricative, MoA.lateral_fricative]

	@property
	def is_affricate(self):
		return self.is_consonant and self.manner == MoA.affricate

	@property
	def is_approximant(self):
		return self.is_consonant and self.manner in [MoA.approximant, MoA.lateral_approximant]

	@property
	def is_lateral(self):
		return self.is_consonant and self.manner in [MoA.lateral_fricative, MoA.lateral_approximant]

	@property
	def is_voiced(self):
		return self.is_consonant and self.voiced

class VowelPhoneme(Phoneme):
	def __init__(self, height: Height, backness: Backness, rounded: bool, long: bool = False):
		self.height = height
		self.backness = backness
		self.rounded = rounded
		self.long = long

		if self.ipa == None:
			raise Exception(f"Unrecognized vowel phoneme: {height}, {backness}, {rounded}")

	@property
	def ipa(self, suprasegmentals=False):
		global vowel_chart

		symbol = vowel_chart[self.height][self.backness][0 if not self.rounded else 1]

		if self.long and suprasegmentals:
			symbol += "ː"

		return symbol

class ConsonantPhoneme(Phoneme):
	def __init__(self, place: PlaceOfArticulation, manner: MannerOfArticulation, voiced: bool):
		self.place = place
		self.manner = manner
		self.voiced = voiced

		if self.ipa == None:
			raise Exception(f"Unrecognized consonant phoneme: {place}, {manner}, {voiced}")

	@property
	def ipa(self, suprasegmentals=False):
		global consonant_chart

		return consonant_chart[self.manner][self.place][0 if not self.voiced else 1]

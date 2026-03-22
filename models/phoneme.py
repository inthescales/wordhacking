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
	MoA.plosive:   			 { PoA.bilabial: ["p", "b"],   PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: ["t", "d"],   PoA.postalveolar: [None, None], PoA.retroflex: ["ʈ", "ɖ"],   PoA.palatal: ["c", "ɟ"],   PoA.velar: ["k", "g"],   PoA.uvular: ["q", "ɢ"],   PoA.pharyngeal: ["ʡ", None],  PoA.glottal: ["ʔ", None]},
	MoA.nasal:     			 { PoA.bilabial: [None, "m"],  PoA.labiodental: [None, "ɱ"],  PoA.dental: [None, None], PoA.alveolar: [None, "n"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɳ"],  PoA.palatal: [None, "ɲ"],  PoA.velar: [None, "ŋ"],  PoA.uvular: [None, "ɴ"],  PoA.pharyngeal: [None, None], PoA.glottal: [None, None]},
	MoA.trill:	   			 { PoA.bilabial: [None, "ʙ"],  PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: [None, "r"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, None], PoA.palatal: [None, None], PoA.velar: [None, None], PoA.uvular: [None, "ʀ"],  PoA.pharyngeal: [None, None], PoA.glottal: [None, None]},
	MoA.tap:	   			 { PoA.bilabial: [None, None], PoA.labiodental: [None, "ⱱ"],  PoA.dental: [None, None], PoA.alveolar: [None, "ɾ"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɽ"],  PoA.palatal: [None, None], PoA.velar: [None, None], PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None]},
	MoA.fricative: 		     { PoA.bilabial: ["ɸ", "β"],   PoA.labiodental: ["f", "v"],   PoA.dental: ["θ", "ð"],   PoA.alveolar: ["s", "z"],   PoA.postalveolar: ["ʃ", "ʒ"],   PoA.retroflex: ["ʂ", "ʐ"],   PoA.palatal: ["ɕ", "ʑ"],   PoA.velar: ["x", "ɣ"],   PoA.uvular: ["χ", "ʁ"],   PoA.pharyngeal: ["ħ", "ʕ"],   PoA.glottal: ["h", "ɦ"]},
	MoA.affricate: 		     { PoA.bilabial: [None, None], PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: ["ts", "dz"], PoA.postalveolar: ["tʃ", "dʒ"], PoA.retroflex: ["tʂ", "dʐ"], PoA.palatal: ["tɕ", "dʑ"], PoA.velar: ["kx", "gɣ"], PoA.uvular: ["qχ", "ɢʁ"], PoA.pharyngeal: ["ħ", "ʕ"],   PoA.glottal: ["h", "ɦ"]},
	MoA.lateral_fricative:   { PoA.bilabial: [None, None], PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: ["ɬ", "ɮ"],   PoA.postalveolar: [None, None], PoA.retroflex: [None, None], PoA.palatal: [None, None], PoA.velar: [None, None], PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None]},
	MoA.approximant:	     { PoA.bilabial: [None, None], PoA.labiodental: [None, "ʋ"],  PoA.dental: [None, None], PoA.alveolar: [None, "ɹ"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɻ"],  PoA.palatal: [None, "j"],  PoA.velar: [None, "ɰ"],  PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None]},
	MoA.lateral_approximant: { PoA.bilabial: [None, None], PoA.labiodental: [None, None], PoA.dental: [None, None], PoA.alveolar: [None, "l"],  PoA.postalveolar: [None, None], PoA.retroflex: [None, "ɭ"],  PoA.palatal: [None, "ʎ"],  PoA.velar: [None, "ʟ"],  PoA.uvular: [None, None], PoA.pharyngeal: [None, None], PoA.glottal: [None, None]},
}

class Phoneme(ABC):
	@classmethod
	def sym(Self, symbol: str):
		global vowel_chart, consonant_chart

		for (height, row) in vowel_chart.items():
			for (backness, pair) in row.items():
				for rounded in [0, 1]:
					if pair[rounded] == symbol:
						return VowelPhoneme(height, backness, rounded)

		for (manner, row) in consonant_chart.items():
			for (place, pair) in row.items():
				for voiced in [0, 1]:
					if pair[voiced] == symbol:
						return ConsonantPhoneme(place, manner, voiced)

		raise Exception(f"No recognized phoneme with symbol '{symbol}'")

class VowelPhoneme(Phoneme):
	def __init__(self, height: Height, backness: Backness, rounded: bool):
		self.height = height
		self.backness = backness
		self.rounded = rounded

		if self.ipa == None:
			raise Exception(f"Unrecognized vowel phoneme: {height}, {backness}, {rounded}")

	@property
	def ipa(self):
		global vowel_chart

		return vowel_chart[self.height][self.backness][0 if not self.rounded else 1]

class ConsonantPhoneme(Phoneme):
	def __init__(self, place: PlaceOfArticulation, manner: MannerOfArticulation, voiced: bool):
		self.place = place
		self.manner = manner
		self.voiced = voiced

		if self.ipa == None:
			raise Exception(f"Unrecognized consonant phoneme: {place}, {manner}, {voiced}")

	@property
	def ipa(self):
		global consonant_chart

		return consonant_chart[self.manner][self.place][0 if not self.voiced else 1]

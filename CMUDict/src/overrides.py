def override_for(word):
	"""Returns an overriding phonemic form for the given word, if there is one."""

	# CMUDict's ordering of varying pronunciations is unclear.
	# These forms are ones that I prefer.
	overrides = {
		"a": ["EY1"],
		"and": ["AE1", "N", "D"],
		"with": ["W", "IH0", "TH"]
	}

	if word in overrides:
		return overrides[word]

	return None	

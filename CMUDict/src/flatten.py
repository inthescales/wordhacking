from CMUDict.src.overrides import override_for

def first(pronounce_dict, use_overrides=True):
    """
    Flattens the given pronunciation map, discarding all but the first
    pronunciation for each term.
    """

    result_dict = {}
    for (term, items) in pronounce_dict.items():
        chosen = items[0]

        if use_overrides:
            # Override certain pronunciations
            override_form = override_for(term.lower())
            if override_form != None:
                chosen = override_form

        result_dict[term] = chosen

    return result_dict

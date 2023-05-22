from card import Card

def convert_string_to_cards_list(s):
	# Multiple card handling.
	if ", " in s:
		split_by_comma = s.split(", ")
		split_by_space = [card.split(" ") for card in split_by_comma]
		return [Card(card_value, card_suite) for card_value, card_suite in split_by_space]

	# Single card handling.
	else:
		split_by_space = s.split(" ")
		card_value, card_suite = split_by_space
		return [Card(card_value, card_suite)]
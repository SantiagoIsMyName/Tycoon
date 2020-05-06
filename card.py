import constants

class Card:
	def __init__(self, val, suit):
		assert val in constants.NORMAL_ORDERING
		assert suit in constants.CARD_SUITS
		self.val = val
		self.suit = suit

	def __eq__(self, other):
		return isinstance(other, Card) and self.val == other.val and self.suit == other.suit
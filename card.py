import constants

class Card:
	def __init__(self, val, suit):
		assert val > 0 and val <= constants.MAX_CARD_VALUE
		self.val = int(val)
		self.suit = suit
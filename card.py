import constants

class Card:
	def __init__(self, val, suit):
		assert val in constants.NORMAL_ORDERING
		assert suit in constants.CARD_SUITS
		self.val = val
		self.suit = suit

	def __eq__(self, other):
		return isinstance(other, Card) and self.val == other.val and self.suit == other.suit

	def __lt__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")

		self_val_to_compare = constants.NORMAL_COMPARATOR[self.val]
		other_val_to_compare = constants.NORMAL_COMPARATOR[other.val]
		if self_val_to_compare != other_val_to_compare:
			return self_val_to_compare < other_val_to_compare
		else:
			return self.suit < other.suit

	def __le__(self, other):
		return self.__eq__(other) or self.__lt__(other)

	def __gt__(self, other):
		return not self.__lt__(other)

	def __ge__(self, other):
		return self.__eq__(other) or self.__gt__(other)

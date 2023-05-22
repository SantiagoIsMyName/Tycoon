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
		return self_val_to_compare < other_val_to_compare

	def __le__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")

		self_val_to_compare = constants.NORMAL_COMPARATOR[self.val]
		other_val_to_compare = constants.NORMAL_COMPARATOR[other.val]
		return self_val_to_compare <= other_val_to_compare

	def __gt__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")

		self_val_to_compare = constants.NORMAL_COMPARATOR[self.val]
		other_val_to_compare = constants.NORMAL_COMPARATOR[other.val]
		return self_val_to_compare > other_val_to_compare

	def __ge__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")
			
		self_val_to_compare = constants.NORMAL_COMPARATOR[self.val]
		other_val_to_compare = constants.NORMAL_COMPARATOR[other.val]
		return self_val_to_compare >= other_val_to_compare

from constants import NORMAL_ORDERING, CARD_SUITS, NORMAL_COMPARATOR

class Card:
	def __init__(self, val, suit):
		assert val in NORMAL_ORDERING
		assert suit in CARD_SUITS
		self.val = val
		self.suit = suit

	def __str__(self):
		return f"{self.val} {self.suit}"

	def __hash__(self):
		return hash((self.val, self.suit))

	def __eq__(self, other):
		return isinstance(other, Card) and self.val == other.val and self.suit == other.suit

	def __lt__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")

		self_val_to_compare = NORMAL_COMPARATOR[self.val]
		other_val_to_compare = NORMAL_COMPARATOR[other.val]
		return self_val_to_compare < other_val_to_compare

	def __le__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")

		self_val_to_compare = NORMAL_COMPARATOR[self.val]
		other_val_to_compare = NORMAL_COMPARATOR[other.val]
		return self_val_to_compare <= other_val_to_compare

	def __gt__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")

		self_val_to_compare = NORMAL_COMPARATOR[self.val]
		other_val_to_compare = NORMAL_COMPARATOR[other.val]
		return self_val_to_compare > other_val_to_compare

	def __ge__(self, other):
		if not isinstance(other, Card):
			raise NameError("Comparing Card to non-card object")
			
		self_val_to_compare = NORMAL_COMPARATOR[self.val]
		other_val_to_compare = NORMAL_COMPARATOR[other.val]
		return self_val_to_compare >= other_val_to_compare

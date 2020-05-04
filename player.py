class Player:
	def __init__(self, name):
		self.name = name
		self.cards = []

	def add_card(self, card):
		self.cards.append(card)
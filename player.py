from constants import NORMAL_COMPARATOR

class Player:
	def __init__(self, name):
		self.name = str(name)
		self.cards = []

	def add_card(self, card):
		self.cards.append(card)

	def play_card(self, current_card):
		if current_card is None: 
			card_to_play = min(self.cards, key = lambda card: NORMAL_COMPARATOR[card.val])
		else: 
			card_to_play = next((card for card in self.cards if NORMAL_COMPARATOR[card.val] > NORMAL_COMPARATOR[current_card.val]), None)
		if card_to_play:
			self.cards.remove(card_to_play)
		return card_to_play

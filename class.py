import random
import constants

class Card:
	def __init__(self, val, suit):
		assert val > 0 and val <= constants.MAX_CARD_VALUE
		self.val = int(val)
		self.suit = suit

class Player:
	def __init__(self, name):
		self.name = name
		self.cards = []

	def add_card(self, card):
		self.cards.append(card)

class Game:
	def __init__(self):
		self.create_shuffled_deck()
		self.players = []

	def create_shuffled_deck(self):
		self.cards = []
		for suit in constant.CARD_SUITS:
			for val in range(1, constants.MAX_CARD_VALUE + 1):
				self.cards.append(Card(val, suit))
		random.shuffle(self.cards)

	def add_player(self, player):
		self.players.append(player)

	def distribute_cards(self):
		num_of_players = len(self.players)
		i = 0
		for card in self.cards:
			turn = i % num_of_players
			self.players[turn].add_card(card)
			i += 1


g = Game()
g.add_player(Player("a"))
g.add_player(Player("b"))
g.add_player(Player("c"))
g.add_player(Player("d"))

g.distribute_cards()

for p in g.players:
	print(len(p.cards))

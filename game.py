import random

import constants
import player
import card

class Game:
	def __init__(self):
		self.create_shuffled_deck()
		self.players = []

	def create_shuffled_deck(self):
		self.cards = []
		for suit in constants.CARD_SUITS:
			for val in range(1, constants.MAX_CARD_VALUE + 1):
				self.cards.append(card.Card(val, suit))
		random.shuffle(self.cards)

	def add_player(self, player):
		self.players.append(player)

	def distribute_cards(self):
		num_of_players = len(self.players)
		i = 0
		for c in self.cards:
			turn = i % num_of_players
			self.players[turn].add_card(c)
			i += 1

	def start_round(self):
		self.top_of_deck = None
		three_of_clubs = card.Card(3, constants.CLUBS)
		starting_player = None
		for p in self.players:
			if three_of_clubs in p.cards:
				starting_player = p
		if starting_player is None: raise NameError("No 3 of clubs found")

		print("The starting player is " + starting_player.name)

		#Wait for player to pick card to play
		#await starting_player.use_card()
		#self.play_card(starting_player, card)


	def play_card(self, player, c):
		if self.top_of_deck is None or self.top_of_deck.val < c.val:
			self.top_of_deck = c





g = Game()
g.add_player(player.Player("a"))
g.add_player(player.Player("b"))
g.add_player(player.Player("c"))
g.add_player(player.Player("d"))

g.distribute_cards()
g.start_round()
from player import Player
from card import Card
import random
import constants

class Game:
	def __init__(self):
		self.create_shuffled_deck()
		self.players = []

	def create_shuffled_deck(self):
		self.cards = []
		for suit in constants.CARD_SUITS:
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

	def play_game(self):
		starting_player_index = self.start_round()
		current_player_index = starting_player_index
		while (not all(len(player.cards) == 0 for player in self.players)):
			current_player_index = (current_player_index + 1) % len(self.players)
			print(current_player_index)
			if current_player_index == 0:
				break

	def start_round(self):
		self.top_of_deck = None
		three_of_clubs = Card(3, constants.CLUBS)
		try: starting_player_index, starting_player = next((i, player) for i, player in enumerate(self.players) if three_of_clubs in player.cards)
		except: raise NameError("No 3 of clubs found")
		print("The starting player is " + starting_player.name + " at index " + str(starting_player_index))
		return starting_player_index

	def play_card(self, player, card):
		if self.top_of_deck is None or self.top_of_deck.val < card.val:
			self.top_of_deck = card


g = Game()
g.add_player(Player("a"))
g.add_player(Player("b"))
g.add_player(Player("c"))
g.add_player(Player("d"))

g.distribute_cards()
g.play_game()
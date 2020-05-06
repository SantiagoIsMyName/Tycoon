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
		final_rankings = []
		starting_player_index = self.start_round()
		current_player_index = starting_player_index
		last_played_index = -1
		while (len(self.players) > 1):
			current_player = self.players[current_player_index]
			if len(current_player.cards) == 0:
				final_rankings.append(current_player)
				self.players.remove(current_player)
				last_played_index = last_played_index % len(self.players)
			else: 
				if last_played_index == current_player_index:
					self.top_of_deck = None

				card_to_play = current_player.play_card(self.top_of_deck)
				if card_to_play:
					self.top_of_deck = card_to_play
					last_played_index = current_player_index
			current_player_index = (current_player_index + 1) % len(self.players)
		return final_rankings + self.players

	def start_round(self):
		self.top_of_deck = None
		three_of_clubs = Card(3, constants.CLUBS)
		try: starting_player_index, starting_player = next((i, player) for i, player in enumerate(self.players) if three_of_clubs in player.cards)
		except: raise NameError("No 3 of clubs found")
		#print("The starting player is " + starting_player.name + " at index " + str(starting_player_index))
		return starting_player_index


g = Game()
g.add_player(Player("a"))
g.add_player(Player("b"))
g.add_player(Player("c"))
g.add_player(Player("d"))

g.distribute_cards()
rankings = g.play_game()
for player in rankings:
	print(player.name)
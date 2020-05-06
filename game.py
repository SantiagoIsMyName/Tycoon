from player import Player
from card import Card

import random
import constants

THREE_OF_CLUBS = Card(3, constants.CLUBS)

def create_shuffled_deck():
	cards = [Card(val, suit) for val in constants.NORMAL_ORDERING for suit in constants.CARD_SUITS]
	random.shuffle(cards)
	return cards

def starting_player_index(players):
	try: starting_player_index = next(i for i, player in enumerate(players) if THREE_OF_CLUBS in player.cards)
	except: raise NameError("No 3 of clubs found")
	return starting_player_index


class Game:
	def __init__(self):
		self.players = []

	def add_player(self, player):
		self.players.append(player)

	def distribute_cards(self):
		cards = create_shuffled_deck()
		num_of_players = len(self.players)
		i = 0

		# Deal cards by cycling through each player and giving them a card until are cards are dealed
		for card in cards:
			turn = i % num_of_players
			self.players[turn].add_card(card)
			i += 1

	def play_game(self):
		self.distribute_cards()

		top_of_pile = None
		final_rankings = []
		current_player_index = starting_player_index(self.players)
		last_played_index = -1

		while (len(self.players) > 1):
			current_player = self.players[current_player_index]

			# If it's the last played person's turn again (as in everyone else passes), the pile gets cleared
			if last_played_index == current_player_index:
				top_of_pile = None

			card_to_play = current_player.play_card(top_of_pile)

			# If the player decided to play a card, it replaces the top card
			if card_to_play:
				top_of_pile = card_to_play
				last_played_index = current_player_index

				# If the current player has just played their last card, they are added to the rankings and no longer play
				if len(current_player.cards) == 0:
					final_rankings.append(current_player)
					self.players.remove(current_player)
					last_played_index = last_played_index % len(self.players)

				# Eight stop: Player who plays an 8 clears the pile, starts a new one
				if card_to_play.val == 8:
					top_of_pile = None
					continue



			current_player_index = (current_player_index + 1) % len(self.players)

		return final_rankings + self.players


g = Game()
g.add_player(Player("a"))
g.add_player(Player("b"))
g.add_player(Player("c"))
g.add_player(Player("d"))

rankings = g.play_game()
for player in rankings:
	print(player.name)
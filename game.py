from player import Player
from card import Card

import random
import constants

THREE_OF_CLUBS = Card("3", constants.CLUBS)

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
		# If any players have any remaining cards after a round, clear them.
		for p in self.players:
			p.clear_cards()

		cards = create_shuffled_deck()
		num_of_players = len(self.players)
		i = 0

		# Deal cards by cycling through each player and giving them a card until are cards are dealed
		for card in cards:
			turn = i % num_of_players
			self.players[turn].add_card(card)
			i += 1

		for p in self.players:
			p.cards = sorted(p.cards, key = lambda card: (constants.NORMAL_COMPARATOR[card.val], card.suit))

	def play_game_with_rounds(self, rounds_to_play):
		number_of_rounds_played = 0
		final_rankings = {p.name : 0 for p in self.players}

		while number_of_rounds_played < rounds_to_play:
			self.distribute_cards()

			top_of_pile = None
			is_revolution = False

			current_rankings = []
			current_player_index = starting_player_index(self.players)
			last_played_index = -1

			while (len(current_rankings) < len(self.players) - 1):
				current_player = self.players[current_player_index]

				# If it's the last played person's turn again (as in everyone else passes), the pile gets cleared
				if last_played_index == current_player_index:
					top_of_pile = None

				#If player is already done, skip them.
				if current_player in current_rankings:
					current_player_index = (current_player_index + 1) % len(self.players)
					continue

				cards_to_play = current_player.play_cards(top_of_pile, is_revolution)

				# Revolution state handling
				if cards_to_play != None and len(cards_to_play) == 4:
					is_revolution = not is_revolution
					if is_revolution:
						print("REVOLUTION!")
					else:
						print("COUNTER-REVOLUTION!")

				# If the player decided to play a card, it replaces the top card
				if cards_to_play:
					top_of_pile = cards_to_play
					last_played_index = current_player_index

					# If the current player has just played their last card, they are added to the rankings and no longer play
					if len(current_player.cards) == 0:
						current_rankings.append(current_player)
						print("Player " + current_player.name + " has used all their cards!")
						print("____________________")

					# Eight stop: Player who plays an 8 clears the pile, starts a new one, continue is so we don't increment current_player_index
					if all(c.val == "8" for c in cards_to_play):
						top_of_pile = None
						continue


				current_player_index = (current_player_index + 1) % len(self.players)

			# Add last player (didn't use all cards, so not in current_rankings)
			for player in self.players:
				if player not in current_rankings:
					current_rankings.append(player)
					break

			# Calculate ranking points
			max_win_points = 30
			for i, player in enumerate(current_rankings):
				final_rankings[player.name] += (max_win_points - 10 * i)

			# Current scores
			print("Round over!")
			print("____________________")
			print("Current rankings:")
			leaderboard = sorted(final_rankings.items(), key = lambda x: x[1], reverse = True)
			for name, score in leaderboard:
				print(name + " scored " + str(score))

			number_of_rounds_played += 1
			print("____________________")

		print("GAME OVER!")
		return final_rankings


g = Game()
g.add_player(Player("A"))
g.add_player(Player("B"))
g.add_player(Player("C"))
g.add_player(Player("D"))

rankings = g.play_game_with_rounds(2)


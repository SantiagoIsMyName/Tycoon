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

def convert_string_to_cards_list(s):
	if ", " in s:
		split_by_comma = s.split(", ")
		split_by_space = [card.split(" ") for card in split_by_comma]
		cards_list = [Card(card_value, card_suite) for card_value, card_suite in split_by_space]
	else:
		split_by_space = s.split(" ")
		card_value, card_suite = split_by_space
		cards_list = [Card(card_value, card_suite)]
	return cards_list


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

	def round_handling(self, previous_round_results):
		top_of_pile = None
		is_revolution = False

		prior_tycoon = previous_round_results[0] if previous_round_results else None
		prior_tycoon_lost = False

		round_results = []
		remaining_players = self.players[::]
		current_player_index = starting_player_index(self.players)
		last_played_index = -1

		player_was_removed = False

		while remaining_players:
			current_player = remaining_players[current_player_index]

			# If it's the last played person's turn again (as in everyone else passes), the pile gets cleared
			if last_played_index == current_player_index and not player_was_removed:
				top_of_pile = None

			#If player is already done, skip them.
			if current_player in round_results:
				current_player_index = (current_player_index + 1) % len(remaining_players)
				continue

			cards_to_play = current_player.play_cards(top_of_pile, is_revolution)

			# Revolution state handling
			if cards_to_play != None and len(cards_to_play) == 4:
				is_revolution = not is_revolution
				if is_revolution:
					print("REVOLUTION!")
				else:
					print("COUNTER-REVOLUTION!")

			player_was_removed = False
			# If the player decided to play a card, it replaces the top card
			if cards_to_play:
				top_of_pile = cards_to_play
				last_played_index = current_player_index

				# If the current player has just played their last card, they are added to the rankings and no longer play
				if len(current_player.cards) == 0:
					round_results.append(current_player)
					remaining_players.remove(current_player)
					last_played_index = (last_played_index) % len(remaining_players)
					print(f"Player {current_player.name} has used all their cards!")
					print("____________________")

					# If prior tycoon doesn't come in first, they auto lose and get placed to Beggar
					if prior_tycoon and len(round_results) == 1:
						if prior_tycoon != current_player:
							prior_tycoon_lost = True
							remaining_players.remove(prior_tycoon)
							last_played_index = (last_played_index) % len(remaining_players)
							print(f"Player {prior_tycoon.name} has gone from Tycoon to Beggar!")
							print("____________________")

					if len(remaining_players) == 1:
						last_player = remaining_players[0]
						round_results.append(last_player)
						remaining_players.remove(last_player)
						continue

					player_was_removed = True


				# Eight stop: Player who plays an 8 clears the pile, starts a new one, continue is so we don't increment current_player_index
				if all(c.val == "8" for c in cards_to_play):
					top_of_pile = None
					continue

			# If a player was removed, we don't need to increment the current index.
			if player_was_removed:
				current_player_index = (current_player_index) % len(remaining_players)
			else:
				current_player_index = (current_player_index + 1) % len(remaining_players)

		if prior_tycoon_lost:
			round_results.append(prior_tycoon)

		return round_results

	def card_swapping(self, round_results):
		n = len(self.players)
		for i in [0, 1]:
			winner = round_results[i]
			loser = round_results[-1-i]

			winner_title = "Tycoon" if i == 0 else "Rich"
			loser_title = "Beggar" if i == 0 else "Poor"
			print(f"{winner_title} (Player {winner.name}) cards: " + str([str(c.val) + " " + str(c.suit) for c in winner.cards]))
			print(f"{loser_title} (Player {loser.name}) cards: " + str([str(c.val) + " " + str(c.suit) for c in loser.cards]))

			num_to_exchange = "two" if i == 0 else "one"
			while True:
				winner_gain = input(f"{winner_title} types {num_to_exchange} card(s) to take from {loser_title}. \n")
				loser_gain = input(f"{winner_title} types {num_to_exchange} card(s) to discard to {loser_title}. \n")
				winner_list = convert_string_to_cards_list(winner_gain)
				loser_list = convert_string_to_cards_list(loser_gain)

				# Check lengths of inputs are correct
				if i == 0:
					lengths_match = len(winner_list) == 2 and len(loser_list) == 2
				else:
					lengths_match = len(winner_list) == 1 and len(loser_list) == 1

				# Check that all inputed cards are indeed in each player's hands
				loser_has_cards = all([c in loser.cards for c in winner_list])
				winner_has_cards = all([c in winner.cards for c in loser_list])

				# If lenghts are correct and all cards are present, exit
				if lengths_match and loser_has_cards and winner_has_cards:
					break
				else:
					print("Error. The suggested swap is invalid. Try again.")

			for c in winner_list:
				winner.add_card(c)
				loser.remove_card(c)

			for c in loser_list:
				winner.remove_card(c)
				loser.add_card(c)
			print("____________________")

		for p in self.players:
			p.cards = sorted(p.cards, key = lambda card: (constants.NORMAL_COMPARATOR[card.val], card.suit))


	def process_round_results(self, round_results, score_map):
		# Calculate ranking points
		max_win_points = 30
		for i, player in enumerate(round_results):
			score_map[player.name] += (max_win_points - 10 * i)

		# Current scores
		print("Round over!")
		print("____________________")
		print("Current rankings:")
		self.leaderboard = sorted(score_map.items(), key = lambda x: x[1], reverse = True)
		for name, score in self.leaderboard:
			print(name + " scored " + str(score))
		print("____________________")
		return score_map


	def play_game_with_rounds(self, rounds_to_play):
		number_of_rounds_played = 0
		score_map = {p.name : 0 for p in self.players}
		round_map = {}
		while number_of_rounds_played < rounds_to_play:
			self.distribute_cards()

			previous_round_results = round_map.get(number_of_rounds_played - 1, None)
			if previous_round_results:
				self.card_swapping(previous_round_results)

			round_results = self.round_handling(previous_round_results)
			score_map = self.process_round_results(round_results, score_map)
			round_map = {number_of_rounds_played : round_results}
			number_of_rounds_played += 1

		print("GAME OVER!")
		return self.leaderboard


rounds_requested = int(input("How many rounds would you like to play? \n"))
print("____________________")
g = Game()
for i in range(1, 5):
	player_name = input(f"What is Player {i}'s name? \n")
	g.add_player(Player(player_name))
print("____________________")
rankings = g.play_game_with_rounds(rounds_requested)


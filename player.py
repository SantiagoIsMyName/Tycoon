from constants import NORMAL_COMPARATOR
from helper import convert_string_to_cards_list

class Player:
	def __init__(self, name):
		self.name = str(name)
		self.cards = []

	def add_card(self, card):
		self.cards.append(card)

	def remove_card(self, card):
		if card in self.cards:
			self.cards.remove(card)

	def clear_cards(self):
		self.cards = []

	def play_cards(self, top_cards, is_revolution):
		# Display relevant information
		print("Current player: " + self.name)
		if top_cards != None:
			print("Current top card(s): " + str([str(c.val) + " " + str(c.suit) for c in top_cards]))
		else:
			print("No top card. This is the start of a new stack")
		print("Card(s) available: " + str([c.val + " " + c.suit for c in self.cards]))

		cards_to_play = None
		# Keep looping until a valid card is selected or the player passes
		while cards_to_play == None:
			typed_input = input("Type a card to play or type p to pass. If playing more than one card, split by commas and a space. \n")

			# Pass logic
			if typed_input == 'p' or typed_input == "":
				break

			# Card selecting verifying logic
			else:
				cards_to_play = convert_string_to_cards_list(typed_input)

				# Check that all cards are indeed in the player's hand, try again otherwise.
				all_cards_in_hand = all([c in self.cards for c in cards_to_play])
				if not all_cards_in_hand:
					print("One of the cards typed does not exist in this player's hand. Try again.")
					cards_to_play = None
					continue

				# Check if all cards that were typed are of the same val, try again otherwise.
				new_card_val = cards_to_play[0].val if cards_to_play else None
				all_cards_same_val = all([c.val == new_card_val for c in cards_to_play])
				if not all_cards_same_val:
					print("Not all of the cards typed have the same value. Try again.")
					cards_to_play = None
					continue

				# Check all cards are unique and non-repeating.
				if len(cards_to_play) != len(set(cards_to_play)):
					print("One of the cards typed is repeated. Try again.")
					cards_to_play = None
					continue

				# If top cards, check len of typed cards vs len of top cards + check all typed cards trump new cards.
				if top_cards:
					# Check that len of top cards matches the len of cards typed, try again otherwise.
					if len(cards_to_play) != len(top_cards):
						print("The number of cards typed does not match the number of cards on the top. Try again.")
						cards_to_play = None
						continue

					# Check that each new card trump the top card's value, try again otherwise.
					for new_card, top_card in zip(cards_to_play, top_cards):
						if not is_revolution and top_card >= new_card:
							print("One of the cards typed is not greater than the top card's value. Try again.")
							cards_to_play = None
							break
						if is_revolution and top_card <= new_card:
							print("One of the cards typed is not smaller than the top card's value. Try again.")
							cards_to_play = None
							break


		# If you have a card to play, remove it from your hand
		if cards_to_play:
			for c in cards_to_play:
				self.cards.remove(c)

		print("____________________")

		return cards_to_play

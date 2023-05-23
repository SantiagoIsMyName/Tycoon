from game import Game
from helper import print_a_line
from player import Player

rounds_requested = int(input("How many rounds would you like to play? \n"))
print_a_line()
g = Game()
for i in range(1, 5):
	player_name = input(f"What is Player {i}'s name? \n")
	g.add_player(Player(player_name))
print_a_line()
rankings = g.play_game_with_rounds(rounds_requested)
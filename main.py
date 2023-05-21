from game import Game

rounds_requested = int(input("How many rounds would you like to play? \n"))
print("____________________")
g = Game()
for i in range(1, 5):
	player_name = input(f"What is Player {i}'s name? \n")
	g.add_player(Player(player_name))
print("____________________")
rankings = g.play_game_with_rounds(rounds_requested)
CLUBS = "Clubs"
DIAMONDS = "Diamonds"
HEARTS = "Hearts"
SPADES = "Spades"
CARD_SUITS = [CLUBS, DIAMONDS, HEARTS, SPADES]

NORMAL_ORDERING = range(3, 11) + ["J", "Q", "K", "A", 2]
NORMAL_COMPARATOR = {3:0, 4:1, 5:2, 6:3, 7:4, 8:5, 9:6, 10:7, "J":8, "Q":9, "K":10, "A":11, 2:12}
# Tycoon
Persona 5 : Royal has a card game that you can play with the other Phantom Thieves called Tycoon when in the Phantom Den, which I enjoyed enough to want to program the rules for fun.

**Note: This code currently doesn't work and is a work in progress.**

# The general rules of Tycoon are:
- Card value ordering is 3 < 4 < 5 ... < 10 < J < Q < K < A < 2 < Joker*.
- The player who has the 3 of Clubs plays first and must play it (by itself or as a group of 3s).
- Afterwards, the next player can only play same value cards that are of greater value than the last played card in the same group size as they were played. Example: If someone plays two 4s, the next player can only play if they have any of two 5s, two 6s, ... etc. Another play would be any card >4 along with a Joker, but more on that later.
- If the player cannot play anything, they must pass. A player may also pass whenever they desire even if they have something they could play.
- If everyone passes, the deck is ended and the last player to play starts a new deck. A new deck can be started with any card.

# Specific situation rules:
- When an 8 is played, the current deck is cut short and starts over. The player who played the 8 then starts a new pile playing whichever card they want.
- The Joker can be used in place for any card. For example, two 5s would lose to a 9 and a Joker played together because the Joker plays the role of a 9 in this situation. A 10 and a Joker also is valid with the Joker playing the role of a 10.
- The Joker by itself also has the highest value of all cards with one exception: the 3 of Spades. The pile ends if a Joker loses to a 3 of Spades with the player who played the 3 of Spades starting a new pile.
- If a group of 4 cards is played all at once, this initiates a Revolution which means the card ordering is flipped such that 3 is the strongest card and 2 is the weakest card. 
- A Counter-Revolution is when a group of 4 cards is played all at once after a Revolution has occured, resulting in the ordering returning back to the norm.

# After-match Results:
- 1st place is Tycoon, 2nd is Rich, 3rd is Poor, and 4th is Beggar. If more than 4 players are present, then the second to last player is Poor, and the last player is Beggar.
- At the start of the next game, the Tycoon gives away any two of their dealt cards to the Beggar, and the Beggar gives away their two highest value cards to the Tycoon. The Rich and the Poor do the same except with one card instead of two.
- If the Tycoon doesn't get 1st in the next round, they automatically become the Beggar for the next round.

# Check-list for Completion
- [x] Add randomized card distribution.
- [x] Ensure the player with the 3 of Clubs plays first.
- [x] Implement the general card ordering hierarchy.
- [x] Create basic single card round logic.
- [x]	Implement the 8 stop rule.
- [x] Add logic for multi-card round handling.
- [] Add the Joker card handling.
- [x] Add the Revolution/Counter Revolution handling whenever 4 of a Kind are played at once.
- [x] Display the end of round rankings.
- [] Implement the card swapping after the rankings are determined.
- [] Force the Tycoon to last in ranking if they don't win the subsequent round.



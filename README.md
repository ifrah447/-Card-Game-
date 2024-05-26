# -Card-Game-
This Python script simulates a simple card game between two players over six rounds. Each player enters a card in each round, and the cards have associated values stored in a dictionary. The player with the higher card value in a round earns points
Card Values Dictionary:

A dictionary named cards contains the card names as keys (e.g., 'AH', 'JH') and their corresponding values as values (e.g., 100, 90).
Initialization:

The round variable is initialized to 0, representing the current round of the game.
Two variables, score_p1 and score_p2, are initialized to 0 to keep track of the scores of player 1 and player 2, respectively.
Game Loop:

A while loop runs until 6 valid rounds are completed. The round variable increments by 1 at the start of each iteration.
Players are prompted to enter their cards using input() functions.
Card Validation and Scoring:

After both players enter their cards, the code checks if the entered cards are valid by looking them up in the cards dictionary.
If both cards are valid:
The card values are compared.
The player with the higher card value earns 10 points.
If the card values are equal, no points are awarded.
If one or both cards are invalid, an error message is displayed, and the round is not counted.
Score Display:

After completing 6 valid rounds, the final scores of both players are displayed.

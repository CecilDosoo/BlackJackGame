# BlackJackGame

- Developed a Python program based on the Blackjack card game, featuring a simplified version that uses multiple functions to ensure smooth gameplay.

- The new_card function generates cards from a deck where Kings, Queens, and Jacks are valued at 10, and Aces start at 11 but can be adjusted to 1 if the user's total exceeds 21. This function returns a randomly selected card.

- The cards_tally function takes the player's cards, represented as a list, sums their values, and returns the total as an integer.

- The compare function evaluates the totals of both the user and the computer, determining the winner based on the higher total. If the user exceeds 21, they lose, regardless of the computer's total.

- The game operates based on the user's decisions to draw more cards or stop. Both the computer and the user draw two cards initially. However, the user can only see the computer's first card and must decide to draw or hold based on their own cards and the visible card of the computer.

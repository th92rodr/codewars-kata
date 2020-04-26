'''
Blackjack Scorer

Complete the function that determines the score of a hand in the card game 
Blackjack (aka 21).

The function receives an array of strings that represent each card in the 
hand ("2", "3", ..., "10", "J", "Q", "K" or "A") and should return the score 
of the hand (integer).

Scoring rules:

Number cards count as their face value (2 through 10).
Jack, Queen and King count as 10.
An Ace can be counted as either 1 or 11.

Return the highest score of the cards that is less than or equal to 21.
If there is no score less than or equal to 21 return the smallest score more than 21.

'''

def blackjack_score(hand):
    score = 0
    number_of_aces = 0
    for card in hand:
        if card.isdigit():
            score += int(card)
        else:
            if card is 'J' or card is 'Q' or card is 'K':
                score += 10
            elif card is 'A':
                number_of_aces += 1

    if number_of_aces:
        # if there is more than one Ace only one of them can get counted as 11
        # and the rest of them as 1
        if number_of_aces > 1:
            # one Ace counted as 11 and the rest as 1
            if score + 11 + number_of_aces - 1 <= 21:
                score += 11 + number_of_aces - 1
            # all Aces counted as 1
            else:
                score += number_of_aces

        # there is only one Ace
        else:
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
    return score


print('[A]\t\t', blackjack_score(['A']))
print('[A, J]\t\t', blackjack_score(['A', 'J']))
print('[5, 3, 7]\t', blackjack_score(['5', '3', '7']))
print('[5, 4, 3, 2, A, K]\t', blackjack_score(['5', '4', '3', '2', 'A', 'K']))
print('[A, 10, A]\t', blackjack_score(['A', '10', 'A']))
print('[A, 10, A]\t', blackjack_score(['A', 'A', 'A']))
print('[A, 2, A]\t', blackjack_score(['A', '2', 'A']))
print('[A, A]\t\t', blackjack_score(['A', 'A']))

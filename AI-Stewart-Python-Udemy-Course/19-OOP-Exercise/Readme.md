Wikipedia Link for the Game to Implement
https://en.wikipedia.org/wiki/War_(card_game)

**List as Stack**  
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

**List as Queue**  
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

**Gameplay**

Children playing War
The objective of the game is to win all the cards.
The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals 
the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards 
played and moves them to their stack. Aces are high, and suits are ignored.[2]

If the two cards played are of equal value, then there is a "war".[2] Both players place the next three 
cards face down and then another card face-up. The owner of the higher face-up card wins the war and adds 
all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the 
battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is 
higher than their opponent's.[2]

Most descriptions of War are unclear about what happens if a player runs out of cards during a war.[2] 
In some variants, that player immediately loses. In others, the player may play the last card in their 
deck as their face-up card for the remainder of the war or replay the game from the beginning.[2]

Game designer Greg Costikyan has observed that since there are no choices in the game, and all outcomes
 are random, it cannot be considered a game by some definitions.[3] However, the rules often do not 
 specify in which order the cards should be returned to the deck. If they are returned in a non-random 
 order, the decision of putting one card before another after a victory can change the overall outcome 
 of the game.[4] The effects of such decisions are more visible with smaller size decks as it is easier 
 for a player to card count; however the decisions can still affect gameplay if taken in standard decks.

```python
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
```
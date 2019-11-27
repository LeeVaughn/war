from random import shuffle

class Card:
  suits = ["spades", "hearts", "diamonds", "clubs"]
  # first two items are None so that index matches card value
  values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

  def __init__(self, value, suit):
    # suits and values should be integers
    self.value = value
    self.suit = suit

  # determines if card is less than opponent's card
  def __lt__(self, other):
    if self.value < other.value:
      return True
    if self.value == other.value:
      if self.suit < other.suit:
        return True
      else:
        return False
    return False

  # determines if card is greater than opponent's card
  def __gt__(self, other):
    if self.value > other.value:
      return True
    if self.value == other.value:
      if self.suit > other.suit:
        return True
      else:
        return False
    return False

  # returns the value and suit of the Card object
  def __repr__(self):
    return self.values[self.value] + " of " + self.suits[self.suit]

class Deck:
  def __init__(self):
    self.cards = []
    # creates a list of cards, first loop is for each card rank, second loop is for each card suit
    for i in range(2, 15):
      for j in range(4):
        self.cards.append(Card(i, j))
    shuffle(self.cards)

  # removes and returns a card from the cards list
  def rm_card(self):
    if len(self.cards) == 0:
      return
    return self.cards.pop()

  def Player:
    def __init__(self, name):
      self.wins = 0
      self.card = None
      self.name = name

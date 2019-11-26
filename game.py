class Card:
  suits: ["spades", "hearts", "diamonds", "clubs"]
  # first two items are None so that index matches card value
  values: [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

  def __init__(self, value, suit):
    """suits and values should be integers"""
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

  def __repr__(self):
    return self.values[self.value] + " of " + self.suits[self.suit]

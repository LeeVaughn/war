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

class Player:
  def __init__(self, name):
    self.wins = 0
    self.card = None
    self.name = name

class Game:
  def __init__(self):
    # starts game by getting player names, creating Deck object, and creating players
    name1 = input("Player 1 name ")
    name2 = input("Player 2 name ")
    self.deck = Deck()
    self.p1 = Player(name1)
    self.p2 = Player(name2)

  # prints the winner of each round of the game
  def wins(self, winner):
    w = "{} wins this round"
    w = w.format(winner)
    print(w)

  # prints the results the outcome of each round of card draws
  def draw(self, p1n, p1c, p2n, p2c):
    d = "{} drew {} while {} drew {}"
    d = d.format(p1n, p1c, p2n, p2c)
    print(d)

  # starts the game
  def play_game(self):
    cards = self.deck.cards
    print("Beginning War!")
    # continue the game as long as there are at least two or more cards left in the deck
    while len(cards) >= 2:
      m = "Press q to quit or any " + "key to play!"
      response = input(m)
      if response == "q":
        break
      p1c = self.deck.rm_card()
      p2c = self.deck.rm_card()
      p1n = self.p1.name
      p2n = self.p2.name
      self.draw(p1n, p1c, p2n, p2c)
      if p1c > p2c:
        self.p1.wins += 1
        self.wins(self.p1.name)
      else:
        self.p2.wins += 1
        self.wins(self.p2.name)

    win = self.winner(self.p1, self.p2)

    # print result of the game
    print("War is over. {} wins".format(win))

  # returns the player who won the most rounds
  def winner(self, p1, p2):
    if p1.wins > p2.wins:
      return p1.name
    if p1.wins < p2.wins:
      return p2.name
    return "It was a tie!"

game =Game()
game.play_game()

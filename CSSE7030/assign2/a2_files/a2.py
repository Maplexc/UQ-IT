#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Xin Chen 45189915"

# Write your classes here
class Card(object):
    """ card in the uno game"""
    def __init__(self, number, colour):
        """ Construct card with number and colour as its attributes

        Parameters:
            number (int): number value of the card
            colour: card colour
        """
        self._number = number
        self._colour = colour

    def get_number(self):
        """(int) Returns the number of Card"""
        return self._number

    def get_colour(self):
        """(CardColour) Returns the colour of Card"""
        return self._colour

    def set_number(self, number):
        """ Set the number value of the card
        
        Parameter:
            number (int): number value of card
        """
        self._number = number

    def set_colour(self, colour):
        """ Set the colour of the card
        
        Parameter:
            colour (CardColour): card colour
        """
        self._colour = colour

    def get_pickup_amount(self):
        """ Return the pickup amount of Card as 0"""
        return 0

    def matches(self, card):
        """ Determines if the next card to be placed on the pile matches this card

        Parameter:
            card (Card)
        Return True, if the cards have same colour or number
        and if the first card in putdown pile is pickup4card
        """
        if self.get_number() == card.get_number() or self.get_colour() == card.get_colour():
            return True
        elif type(card) == Pickup4Card:
            return True
        return False
    
    def play(self, player, game):
        """ Perform a special card (skipcard, reversecard, pickup2card, pickup4card) action

        Parameters:
            player (Player)
            game (a2_support.UnoGame)
        """
        self._player = player
        self._game = game

    def __str__(self):
        """ Returns the string representation of this card"""
        return "Card({}, {})".format(self.get_number(), self.get_colour())

    def __repr__(self):
        """ Returns the string representation of this card"""
        return self.__str__()
        # return "Card({}, {})".format(self.get_number(), self.get_colour())


class SkipCard(Card):
    """ SkipCard in the uno game"""
    def matches(self, card):
        """ Determines if the next card to be placed on the pile matches this card

        Parameter:
            card (Card)
        Return True, if the cards have the same colour
        """
        if self.get_colour() == card.get_colour():
            return True
        return False
    
    def play(self, player, game):
        """ Skip the next player

        Parameters:
            player (Player)
            game (a2_support.UnoGame)
        """
        super().play(player, game)
        self._game.skip()

    def __str__(self):
        return "SkipCard({}, {})".format(self.get_number(), self.get_colour())

    def __repr__(self):
        return "SkipCard({}, {})".format(self.get_number(), self.get_colour())

class ReverseCard(Card):
    """ ReverseCard in the uno game"""
    def matches(self, card):
        """ Determines if the next card to be placed on the pile matches this card

        Parameter:
            card (Card)
        Return True, if the cards have the same colour
        """
        return self.get_colour() == card.get_colour() # better way
    
##        if self.get_colour() == card.get_colour():
##            return True
##        return False
##    
    def play(self, player, game):
        """ Reverse the direction of the game

        Parameters:
            player (Player)
            game (a2_support.UnoGame)
        """
        super().play(player, game)
        self._game.reverse()
        
    def __str__(self):
        return "ReverseCard({}, {})".format(self.get_number(), self.get_colour())

    def __repr__(self):
        return "ReverseCard({}, {})".format(self.get_number(), self.get_colour())

class Pickup2Card(Card):
    """ Pickup2Card in the uno game"""
    def matches(self, card):
        """ Determines if the next card to be placed on the pile matches this card

        Parameter:
            card (Card)
        Return True, if the cards have the same colour
        """
        if self.get_colour() == card.get_colour():
            return True
        return False
    
    def get_pickup_amount(self):
        """ Return the pickup amount of Pickup2Card as 2"""
        return 2

    def play(self, player, game):
        """ Next player pick up 2 cards

        Parameters:
            player (Player)
            game (a2_support.UnoGame)
        """
        super().play(player,game)
        next_player_deck = self._game.get_turns().peak().get_deck()
        pickup_amount = self.get_pickup_amount()
        cards = self._game.pickup_pile.pick(pickup_amount)
        next_player_deck.add_cards(cards)

    def __str__(self):
        return "Pickup2Card({}, {})".format(self.get_number(), self.get_colour())

    def __repr__(self):
        return "Pickup2Card({}, {})".format(self.get_number(), self.get_colour())

class Pickup4Card(Card):
    """ Pickup4Card in the uno game"""
    def matches(self, card):
        """ Matches with any card

        Parameter:
            card (Card)
        Return True
        """
        return True
    
    def get_pickup_amount(self):
        """ Return the pickup amount of Pickup4Card as 4"""
        return 4

    def play(self, player, game):
        """ Next player pick up 4 cards

        Parameters:
            player (Player)
            game (a2_support.UnoGame)
        """
        super().play(player,game)
        next_player_deck = self._game.get_turns().peak().get_deck()
        pickup_amount = self.get_pickup_amount()
        cards = self._game.pickup_pile.pick(pickup_amount)
        next_player_deck.add_cards(cards)
    
    def __str__(self):
        return "Pickup4Card({}, {})".format(self.get_number(), self.get_colour())

    def __repr__(self):
        return "Pickup4Card({}, {})".format(self.get_number(), self.get_colour())
    

class Deck(object):
    """ A collection of ordered Uno cards"""
    def __init__(self, starting_cards=None):
        """ Construct card with starting_cards"""
        self._starting_cards = starting_cards
        if self._starting_cards is None:
            self._starting_cards = []
        
    def get_cards(self):
        """ Return a list of cards in the deck"""
        return self._starting_cards

    def get_amount(self):
        """ Returns the amount of cards in a deck"""
        return len(self._starting_cards)

    def shuffle(self):
        """ Shuffle the order of the cards in the deck"""
        random.shuffle(self._starting_cards)

    def pick(self, amount=1):
        """ Take the first 'amount' of cards off the deck and return them

        Parameter:
            amount (int): the amount of cards
        """
        pick_cards = []
        for i in range (1, amount+1):
            if len(self._starting_cards) == 0:
                return pick_cards
            pick_cards.append(self._starting_cards.pop(-1))
        return pick_cards

    def add_card(self, card):
        """ Place a card on top of the deck

        Parameter:
            card (Card)
        """
        self._starting_cards.append(card)

    def add_cards(self, cards):
        """ Place a list of cards on top of the deck

        Parameter:
            cards (list<Card>): list of Card
        """
        self._starting_cards.extend(cards)

    def top(self):
        """ Peaks at the card on top of the deck and returns it or None if the deck is empty"""
        if self.get_amount() != 0:
            return self._starting_cards[-1]
        else:
            return None


class Player(object):
    """ Players in a game of uno"""
    def __init__(self, name):
        """ Construct a player with name"""
        self._name = name
        self._player_deck = Deck()

    def get_name(self):
        """ Return the name of the player"""
        return self._name

    def get_deck(self):
        """ Return the players deck of cards"""
        return self._player_deck

    def is_playable(self):
        """ Raises a NotImplementedError on the base Player class"""
        raise NotImplementedError

    def has_won(self):
        """ Returns True iff the player has an empty deck and has therefore won"""
        if self.get_deck().get_amount() == 0:
            return True
        else:
            return False

    def pick_card(self, putdown_pile):
        """ Selects a card to play from the players current deck
            Raises a NotImplementedError on the base Player class"""
        raise NotImplementedError
        
class HumanPlayer(Player):
    """ Human players in a game of uno"""
    def __init__(self,name):
        """ Construct a human player with name"""
        super().__init__(name)

    def is_playable(self):
        """ Return True iff the players moves aren't automatic"""
        return True

    def pick_card(self, putdown_pile):
        """ Selects a card to play from the players current deck
            Return None for non-automated players"""
        return None

class ComputerPlayer(Player):
    """ Computer player in a game of uno"""
    def __init__(self,name):
        """ Construct a computer player with name"""
        super().__init__(name)

    def is_playable(self):
        """ Computer player is not playable"""
        return False
    
    def pick_card(self, putdown_pile):
        """ Selects a card to play from the players current deck
            Return None when a card cannot be played
            Return a card, if find a card can be played, and remove that card from that player's deck
        """
        available = []
        computer_deck = self._player_deck.get_cards()
        num = len(computer_deck)
        putdown_cards = putdown_pile.get_cards()
        top_card = putdown_cards[-1]
        for i in range(0, num):
            if computer_deck[i].matches(top_card):
                available.append(computer_deck[i])      
        random.shuffle(available)
        if len(available) != 0:
            computer_deck.remove(available[0])
            return available[0]
        else:
            return None




def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()

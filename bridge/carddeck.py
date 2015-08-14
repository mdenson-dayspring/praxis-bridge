# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:14:51 2015

@author: mdenson
"""
import random

suits = ['s', 'h', 'c', 'd']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank+suit)
    
    def __len__(self):
        return len(self.cards)
        
    def shuffle(self):
        random.shuffle(self.cards)        
        random.shuffle(self.cards)        
        random.shuffle(self.cards)        
        
    def dealcard(self):
        return self.cards.pop()

class Hand(object):
    def __init__(self):
        self.cards = []
         
    def add(self, card):
        self.cards.append(card)
        
handnames = ['East', 'South', 'West', 'North']

class Bridge(object):
    def __init__(self, deck):
        deck.shuffle()
        deck.shuffle()
        self.hands = {}
        for hn in handnames:
            self.hands[hn] = Hand()
        
        self.deal(deck)
        
    def deal(self, deck):
        while len(deck)>0:
            for hn in handnames:
                self.hands[hn].add(deck.dealcard())
        

if __name__ == "__main__":
    import sys
    d = Deck()
    b = Bridge(d)
    print(b.hands['North'].cards)
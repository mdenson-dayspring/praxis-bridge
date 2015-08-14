# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:14:51 2015

@author: mdenson
"""
import random

suits = ['♠', '♡', '♢', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

class Deck(object):
    def __init__(self):
        self.cards = []
        self.cards = [i for i in range(54)]
    
    def __len__(self):
        return len(self.cards)
        
    def removeJokers(self):
        self.cards.remove(53)
        self.cards.remove(52)
        
    def shuffle(self):
        random.shuffle(self.cards)        
        random.shuffle(self.cards)        
        random.shuffle(self.cards)        
        
    def dealcard(self):
        return self.cards.pop()
        
    def twoChar(self, card):
        if card > 51:
            return 'JK'
        return ranks[card >> 2] + suits[card & 0x3]

class Hand(object):
    def __init__(self):
        self.cards = []
         
    def add(self, card):
        self.cards.append(card)
        
    def sort(self):
        self.cards.sort(reverse=True)

class BridgeHand(Hand):
    def sort(self):
        self.cards.sort()
        
handnames = ['East', 'South', 'West', 'North']

class Bridge(object):
    def __init__(self, deck):
        deck.removeJokers()
        deck.shuffle()
        self.hands = {}
        for hn in handnames:
            self.hands[hn] = BridgeHand()
        
        self.deal(deck)
        
        for n, h in self.hands.items():
            h.sort()
        
    def deal(self, deck):
        while len(deck)>0:
            for hn in handnames:
                self.hands[hn].add(deck.dealcard())
        

if __name__ == "__main__":
    import sys
    d = Deck()
    print([d.twoChar(s) for s in d.cards])
    b = Bridge(d)
    for hn in handnames:
        print(hn + ' ',)
        print([d.twoChar(s) for s in b.hands[hn].cards])
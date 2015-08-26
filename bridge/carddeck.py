# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:14:51 2015

@author: mdenson
"""
import random
import functools

suits = ['♣', '♢', '♡', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

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

def bridgeCompare(x,y):
    cmp = (y & 0x3) - (x & 0x3) 
    if cmp == 0:
        cmp = (y>>2) - (x>>2)
    return cmp
    
class BridgeHand(Hand):
    def sort(self):
        self.cards.sort(key=functools.cmp_to_key(bridgeCompare))
        
    def toString(self, leftStrings, hand):
        retString = []
        for n, l in enumerate(leftStrings):
            if n == 0:
                retString.append(l + hand.upper())
            else:
                suit = suits[4-n]
                cards = [c for c in self.cards if (c & 0x3) == n-1]
                retString.append(l + suit)
                for c in cards:
                    retString[n] += ' ' + ranks[c >> 2]
        return retString
        
handnames = ['East', 'South', 'West', 'North']

class Bridge(object):
    def __init__(self, deck):
        deck.removeJokers()
        deck.shuffle()
        deck.shuffle()
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

    def printGame(self):
        middle = ['                    '] * 5
        left = [''] * 5

        hand = 'North'
        outStrings = b.hands[hand].toString(middle, hand)
        for s in outStrings:
            print(s)

        hand = 'West'
        west = []
        for w in b.hands[hand].toString(left, hand):
            west.append((w + middle[0] + middle[0])[:-len(w)])
        hand = 'East'
        outStrings = b.hands[hand].toString(west, hand)
        for s in outStrings:
            print(s)
        
        hand = 'South'
        outStrings = b.hands[hand].toString(middle, hand)
        for s in outStrings:
            print(s)

        

if __name__ == "__main__":
    import sys
    d = Deck()
    b = Bridge(d)
    b.printGame()

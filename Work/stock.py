# %%
#!usr/bin/env python3
# # stock.py
#
# Exercise 4.1

class Stock: 
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares*self.price
    
    def sell(self, shares):
        self.shares -= shares
        
# %%

# report.py
#
# Exercise 2.4

"""
open a given portfolio file and read it into a list of tuples

"""

import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row != []:
                prices[row[0]] = float(row[1])
    return prices

# list of objects ("symbol", shares, price)
portfolio = read_portfolio('Data/portfolio.csv')

# object of prices
prices = read_prices('Data/prices.csv')


gain_or_loss = 0

for stock in portfolio:
    paid = stock["price"]*stock["shares"]
    worth = prices[stock["name"]]*stock["shares"]
    gain_or_loss += worth - paid

print(gain_or_loss)
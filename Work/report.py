# %%
# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    '''Computes the total cost of a portfolio from a CSV file.
    filename: the name of the CSV file'''
    portfolio = []
    # if len(sys.argv) >= 2:
    #     filename = sys.argv[1]
    # else:
    #     filename = 'Data/portfolio.csv'

    with open(filename) as f:
        rows = csv.reader(f)  
        next(rows) # Skip headers
        for row in rows: 
            try:
                holding = {
                    'name' : row[0],
                    'shares' : int(row[1]), 
                    'price' : float(row[2])
                }
                portfolio.append(holding)
            except ValueError:
                print(f"Error processing line: {row}")
                continue  # Skip lines with errors

    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for rowno, row in enumerate(rows, start=1):
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue
            except ValueError:
                print(f'Row {rowno}: Coudln\'t convert: {row} ')
    return prices


def prt_report():
    spc = 10
    headers = ('Name', 'Shares', 'Price', 'Change')
    seperator = '-'*spc
    
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % (seperator,seperator,seperator,seperator))

    
    for name, share, price, change in show_portfolio():
        try:
            print('%10s %10d %10s %10.2f' % (name, share, '$%0.2f' % price, change))
        except TypeError:
            print("continue")

def show_portfolio():
    return make_report('Data/portfolio.csv','Data/prices.csv')


def make_report(portfolioName, pricesName):
    ls = []
    prices = read_prices('Data/prices.csv')
    portfolio = read_portfolio('Data/portfolio.csv')
    for s in portfolio:
        ls.append((s['name'], s['shares'], prices[s['name']], prices[s['name']]-s['price']))
    return ls

        

   
#print(read_portfolio('Data/portfolio.csv'))
# %%

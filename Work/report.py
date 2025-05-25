# %%
#!/user/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv
from stock import Stock
import tableformat

def read_portfolio(filename):
    '''Computes the total cost of a portfolio from a CSV file.
    filename: the name of the CSV file Data/portfolio.csv'''
    portfolio = None
    with open(filename) as lines:
        portdicts = parse_csv(lines,select=['name','shares','price'],types=[str,int,float])
        portfolio =[Stock(d['name'], d['shares'],d['price']) for d in portdicts]
    return portfolio

def read_prices(filename):
    ''' Read the current prices of shares from Data/prices.csv'''
    prices = None
    with open(filename) as lines: 
        prices = parse_csv(lines,has_headers=False,types=[str,float])
    return dict(prices)

def make_report(portfolio, prices):
    '''Construct the report to be printed'''
    ls = []
    for s in portfolio:
        ls.append((s.name, s.shares, prices[s.name], prices[s.name]-s.price))
    return ls

def portfolio_report(portfolioFile='Data/portfolio.csv', pricesFile='Data/prices.csv', output_format="txt"):
    ''' Print a report showing stock holdings. This will consist of Name, shares, purchase price, gain/loss'''
    # Output the report
    portfolio = read_portfolio(portfolioFile)
    prices = read_prices(pricesFile)
    
    #Create the report data
    report = make_report(portfolio, prices)

    # Print the report
    formatter = tableformat.create_formatter(output_format)
    print_report(report, formatter)

def print_report(reportdata, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name,shares,price, change in reportdata:
        rowdata = [name, str(shares),f'{price:0.2f}',f'{change:0.2f}']
        formatter.row(rowdata)

def main(argv):
    ''' Must supply 3 arguments in order. Portolio filename, Prices filename, output type.'''
    portfolio_report(argv[1],argv[2],argv[3])

if __name__=='__main__':
    import sys
    main(sys.argv)
# %%

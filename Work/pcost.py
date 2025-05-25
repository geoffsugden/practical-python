# %%
#!/user/bin/env python3
#  # pcost.py
#
# Exercise 1.27
import report

def portfolio_cost(filename):
    """
    Calculate the total cost of the portfolio from a CSV file.
    
    Args:
        fpath (str): The path to the CSV file containing portfolio data.
        
    Returns:
        float: The total cost of the portfolio.
    """
    totalcost = 0
    portfolio = report.read_portfolio(filename)
    for stock in portfolio:
        totalcost += stock.shares * stock.price

    return totalcost

def main(argv):
    print(portfolio_cost(sys.argv[1]))

if __name__=='__main__':
    import sys
    main(sys.argv)
# %%

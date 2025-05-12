# %%
# # pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(fpath):
    """
    Calculate the total cost of the portfolio from a CSV file.
    
    Args:
        fpath (str): The path to the CSV file containing portfolio data.
        
    Returns:
        float: The total cost of the portfolio.
    """
    totalcost = 0
    with open(fpath) as f:
        rows = csv.reader(f)  
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers,row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                totalcost += nshares * price 
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")
                continue  # Skip lines with errors

    return totalcost

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'

# cost = portfolio_cost(filename)
# print(f"Total cost of the portfolio: {cost:.2f}")

# %%

# %%
#!/usr/bin/env python3
# # fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter = ',',silence_errors=True):
    '''
    Parse a CSV file into a list of records. Assumes that the file contains headers unless otherwise specified.
    '''

    if select and not has_headers: 
         raise RuntimeError("Select argument requires headers")
    
    rows = csv.reader(lines, delimiter=delimiter)
                
    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows,1):
        try:
            if not row: # Skip rows with no data
                continue

            #filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices]

            # apply type conversion to the row                
            if types:
                row = [func(val) for func,val in zip(types, row)]

            # Make a dictionary or tuple 
            if headers:
                record = dict(zip(headers, row))
            else: 
                    record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'Row {rowno}: Couldn\'t convert {row}')
                print(f'Row {rowno}: Reason {e}')
    return records
        
# %%

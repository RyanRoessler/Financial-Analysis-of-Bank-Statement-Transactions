import pandas as pd
from typing import Union, IO
from datetime import datetime
from tabulate import tabulate


def show_statements(cc_statement: Union[str, IO], dc_statement: Union[str, IO]) -> None:
    """
    This function will display a credit and debit bank statement as Pandas dataframes
    Look through the dataframes to find a type of purchase to analyze
    Then, use filter_financial()
    """
    
    # Convert the CSV files to pandas dataframes
    dfcc = pd.read_csv(cc_statement)
    dfdc = pd.read_csv(dc_statement)
    
    
    # Display the date ranges
    # Ensure the 'Date' columns are of datetime type
    dfcc['Date'] = pd.to_datetime(dfcc['Date'], errors='coerce')
    dfdc['Date'] = pd.to_datetime(dfdc['Date'], errors='coerce')
    
    # Get total number of days for each statement 
    dates_cc = dfcc['Date']
    dates_dc = dfdc['Date']
    
    # Get first and last days
        #.strftime() excludes the time (00:00:00)
    first_day_cc = dates_cc.min().strftime('%Y-%m-%d')
    last_day_cc = dates_cc.max().strftime('%Y-%m-%d')
    
    first_day_dc = dates_dc.min().strftime('%Y-%m-%d')
    last_day_dc = dates_dc.max().strftime('%Y-%m-%d')


    # Compact tabular format using tabulate
    print(f'Credit Card Statement ({first_day_cc} - {last_day_cc}):\n')
    print(tabulate(dfcc, headers='keys', tablefmt='plain', showindex=False))
    print("\n\n")
    print(f'Debit Card Statement ({first_day_dc} - {last_day_dc}):\n')
    print(tabulate(dfdc, headers='keys', tablefmt='plain', showindex=False))
    

def filter_financial(cc_statement: Union[str, IO], dc_statement: Union[str, IO], filter_for: str, exclude: Union[str, None] = None) -> str:
    """
    This function takes two files corresponding to credit and debit card bank statements
        The bank statements should be downloaded as CSV files
    The third argument is a string to filter for (e.g. "DOORDASH", "KING SOOPERS", etc.)
    The fourth argument is an optional string to exclude during filtering (e.g. "FUEL", etc.)
        If you have nothing to exclude, set the exclude arg to "None" or ""
    """
    
    # Convert the CSV files to pandas dataframes
    dfcc = pd.read_csv(cc_statement)
    dfdc = pd.read_csv(dc_statement)
    
    # Ensure the 'Date' columns are of datetime type
    dfcc['Date'] = pd.to_datetime(dfcc['Date'], errors='coerce')
    dfdc['Date'] = pd.to_datetime(dfdc['Date'], errors='coerce')
    
    # Filter dataframes to get Name and Amount columns for both statements
    dfcc = dfcc[['Name', 'Amount', 'Date']]
    dfdc = dfdc[['Name', 'Amount', 'Date']]
    
    # Filter for rows with occurrences of "filter_for" and optionally exclude "exclude"
    # If something to exclude
    if exclude:
        dfcc_filt = dfcc[dfcc['Name'].str.contains(filter_for, case=False) & ~dfcc['Name'].str.contains(exclude, case=False)]
        dfdc_filt = dfdc[dfdc['Name'].str.contains(filter_for, case=False) & ~dfdc['Name'].str.contains(exclude, case=False)]
    # If nothing to exclude
    else:
        dfcc_filt = dfcc[dfcc['Name'].str.contains(filter_for, case=False)]
        dfdc_filt = dfdc[dfdc['Name'].str.contains(filter_for, case=False)]
        
    # Check for duplicates in the filtered data
    dfcc_filt = dfcc_filt.drop_duplicates()
    dfdc_filt = dfdc_filt.drop_duplicates()
    
    
    # Create dictionaries with Name:[name1, name2, ...] and Amount:[amount1, amount2, ...]
        # Initialize Name and Amount keys
        # Access Name and Amount columns from dataframe and append their row values to a single list
    cc_dict = {'Name': dfcc_filt['Name'].tolist(), 'Amount':dfcc_filt['Amount'].tolist()}
    dc_dict = {'Name':dfdc_filt['Name'].tolist(), 'Amount':dfdc_filt['Amount'].tolist()}
    
    # Combine both dictionaries
        # Again, initialize Name and Amount keys, then concatenate their values from both dictionaries
    total_dict = {
        'Name':cc_dict['Name'] + dc_dict['Name'],
        'Amount':cc_dict['Amount'] + dc_dict['Amount']
    }
    
    
    # Get total occurrences of purchase (e.g. grocery trips, doordash order, etc.)
    occurrences = len(total_dict['Name'])
    # print(occurrences)
    
    # Total the amounts
    total_cost = sum(amount for amount in total_dict['Amount'])
    # print(round(total_cost, 2))
    
    # Get average cost per occurrence
    avg_cost = total_cost / occurrences
    # print(round(avg_cost, 2))
    
    
    # Get total number of days from both bank statements, and take the largest range  
    # Use unfiltered dataframe with all dates preserved
    dates_cc = dfcc['Date']
    dates_dc = dfdc['Date']
    
    # Get first and last days
    first_day_cc = dates_cc.min()
    first_day_dc = dates_dc.min()
    last_day_cc = dates_cc.max()
    last_day_dc = dates_dc.max()
    
    # Get minimum first day and maximum last day
    first_day = min(first_day_cc, first_day_dc)
    last_day = max(last_day_cc, last_day_dc)

    # Calculate difference (total days)
    tot_days = (last_day - first_day).days
    
    
    # Get weekly cost
    if occurrences != 52:
        weekly_cost = round((total_cost / 52), 2)
        
    # Get monthly cost
    if occurrences != 12:
        monthly_cost = round((total_cost / 12), 2)
    
    
    # Construct the summary string output
    summary = (
        f'Total days from {first_day.date()} to {last_day.date()}: {tot_days}\n'
        f'Total cost of {filter_for} occurrences: {total_cost:.2f}\n'
        f'Total number of {filter_for} occurrences: {occurrences}\n'
        f'Average cost per {filter_for} occurrence: {avg_cost:.2f}\n'
        f'Average cost per week: {weekly_cost}\n'
        f'Average cost per month: {monthly_cost}'
    )

    return summary
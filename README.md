# Financial Analysis of Bank Statement Transactions

This repository contains the Financial_Functions.py library with two functions inside.
<ul>
  <li>These functions are designed to analyze certain purchase transactions ("Doordash", "King Soopers", etc.) from both a credit and debit bank statement.</li>
  <li>They are designed to take two bank statements (credit and debit), pool them together, and perform a filtered analysis on certain transactions from both statements combined.</li>
</ul>

The first function "show_statements()" takes two bank statements (credit and debit) as CSV files, and displays them in a compact, tabular format.
<ul>
  <li>This function also displays the date range for each statement.</li>
</ul>

The second function "filter_financial()" takes the same two bank statements, a string argument "filter_for", and an optional string argument "exclude".
<ul>
  <li>This function is designed to filter for certain transaction types (e.g. "Doordash", "Amazon", etc.) and return an analysis on those transactions.</li>
  <li>Use of "exclude": Say you want to analyze your King Soopers grocery purchases, but exclude King Soopers Fuel purchases. You can filter for "King Soopers" and exclude "Fuel".</li>
  <li>This function returns the following outputs:
    <ul>
      </li>
      <li>Total number of purchases</li>
      <li>Total cost of all purchases combined</li>
      <li>Average cost per purchase</li>
      <li>Average weekly cost (this is only accurate if the statements span a 1-year period)</li>
      <li>Average monthly cost (this is only accurate if the statements span a 1-year period)</li>
      <li>Largest combined date range of both statements, and the total number of days
        <ul>
          <li>e.g. if your credit card statement spans 2023-June-20 to 2024-June-14 and your debit card statement spans 2023-June-16 to 2024-June-09, the function will use the range 2023-June-16 to 2024-June-14.
          <li>The function would return "Total days from 2023-06-16 to 2024-06-14: 364".</li>
        </ul>
    </ul>
  </li>
</ul>







> 

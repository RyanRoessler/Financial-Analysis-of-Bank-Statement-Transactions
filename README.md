# Analysis of Transactions from Bank Statements

This repository contains the Financial_Functions.py library with two functions inside.
<ul>
  <li>These functions are designed to analyze certain purchase transactions over a 1-year period ("Doordash", "King Soopers", etc.)</li>
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
      <li>Largest combined date range of both statements, and the total number of days
        <ul>
          <li>e.g. if your credit card statement spans 2022-June-20 to 2023-February-12 and your debit card statement spans 2022-August-01 to 2023-March-08, the function will use the range 2022-June-20 to 2023-March-08.</li>
          <li>Depending on the range, the function will display something like 364 days, etc.</li>
        </ul>
      </li>
      <li>Total number of purchase occurrences</li>
      <li>Total cost of all purchases</li>
      <li>Average cost per purchase occurrence</li>
      <li>Average weekly cost</li>
      <li>Average monthly cost</li>
    </ul>
  </li>
</ul>







> 

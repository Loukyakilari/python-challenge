# **python-challenge**

This contains my solution for two python challenges PyBank and PyPoll (Module 3)

    * PyBank challenge is analysis on the financial records of company.
    * PyPoll challenge is analysis on the votes of election result.

## **Setup**

* Inside your local git repository, create a directory for each Python challenge: ***PyBank*** and ***PyPoll***
* For each folder created, add the following:
    * A new file called ***main.py*** which contains the main script to run analysis.
    * A ***Resources*** folder which contains the csv files used for analysis. Make sure to have correct path to read the csv files.
    * An ***analysis*** folder which contains text file that has the results of the analysis.

## **Task List**
### **PyBank Challenge**

In this challenge a set of financial data called budget_data.csv is given. The dataset is composed of two columns: Date and Profit/Losses. Task is to create a Python script that analyzes the records to calculate the following:

* The total number of months in the dataset.
* The net total amount of Profit/Losses over the entire period
* The changes in Profit/Losses over the entire period, and the average of those changes.
* The greatest increase in profits which include date and amount.
* The greatest decrease in profits which include date and amount.

The final script should print the analysis to the terminal and also export a text file with the results.


### **PyPoll Challenge**

In this challenge a set of poll data called election_data.csv is given. The dataset is composed of three columns: Voter ID, County, and Candidate. Task is to create a Python script that analyzes the votes and calculates the following:

* The total number of votes cast.
* A complete list of candidates who received votes.
* The percentage of votes each candidate won.
* The total number of votes each candidate won.
* The winner of the election based on popular vote.

The final script should print the analysis to the terminal and also export a text file with the results.

## **Screenshots**

The results should look similar to the following:

### **PyBank**

Financial Analysis
..................
Total Months: 86
Total: $22564198
Average Change : $ -8311.11
Greatest Increase in Profits: Aug-16  ($1862002)
Greatest decrease in Profits: Feb-14  ($-1825558)

### **PyPoll**

Election Results
.....................................
Total Votes: 369711
.....................................
Charles Casper Stockham : 23.049% (85213)
Diana DeGette : 73.812% (272892)
Raymon Anthony Doane : 3.139% (11606)
.....................................
Winner: Diana DeGette
......................................






    

     






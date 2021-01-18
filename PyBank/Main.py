# Import modules
import os
import csv

# Set path for the csv file in the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables that will be pulled from CSV
total_months = 0
net_profit = 0

# Define lists hold the months and the profit/loss changes
# This is a place to store the values as the for loop goes through the csv
months = []
month_profit_change = []

# Define variables needed for future calculations
average_change = 0
greatest_increase = 0
greatest_decrease = 0

# Open the CSV and make sure that it is being read
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print csvreader to make sure everything is set up correctly
    print(csvreader)

    # Recognize the header row, and know to skip when working with the rest of the rows
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Check to make sure it can read each row of data after the header
    for row in csvreader:
        print(row)


#-------------------------------------------------#
# Print Statements (Test)
# The text print statements and formatting are taken directly from the homework instructions, the values are dependant upon the code running successfully
print(f"Financial Analysis")
print(f"----------------------------")
# Should print the text and then a zero value for now
print(f"total_months {total_months}")
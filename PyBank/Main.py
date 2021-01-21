# Import modules
import os
import csv

# Set path for the csv file in the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables that will be pulled from CSV
total_months = 0
net_profit = 0
month = 0
profit_loss = 0

# Define lists hold the months and the profit/loss changes
# This is a place to store the values as the for loop goes through the csv
month_count = []
month_profit_change = []

# Define variables needed for future calculations
average_change = 0
pl_change = 0
prev_row = 0
greatest_increase = 0
greatest_decrease = 0

# Open the CSV and make sure that it is being read
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print csvreader to make sure everything is set up correctly
    #print(csvreader)

    # Recognize the header row, and know to skip when working with the rest of the rows
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Set for loop to read through each row of the csvreader
    for row in csvreader:
        
        # Define what information is held in each column of each row
        month = (row[0])
        profit_loss = int(row[1])
        

        # Add month value to the month_count list
        # Get total months by getting the length of the month_count list
        # UNSURE IF THIS IS THE BEST WAY TO DO THIS _but it works for now
        month_count.append(month)
        total_months = len(month_count)
        
        # Find the net profit by adding the profit_loss value of column 1 to the net profit running total
        net_profit = net_profit + profit_loss
        #print(net_profit)

        # TEST
        # Calculate the monthly change in profit_loss
        pl_change = profit_loss - prev_row  # This calculation is working, BUT takes the first pl value instead of a zero
        
        month_profit_change.append(pl_change)
        #print(month_profit_change) - NOT appending the values I want
        
        prev_row = int(row[1])
        
        #print(pl_change)
        
        # Calculate the greatest change in increase to the profit_loss column
        if pl_change > greatest_increase:
            greatest_increase = pl_change 
            
        # Calculate the greatest change in decrease to the profit_loss column
        if pl_change < greatest_decrease:
            greatest_decrease = pl_change
        

    # Get the average by dividing the monthly change numbers by the total months count
    average_change = sum(month_profit_change) / (len(month_profit_change))
    print(sum(month_profit_change))
    #print(int(len(month_profit_change)))


#-------------------------------------------------#
# Print Statements (Test)
# The text print statements and formatting are taken directly from the homework instructions, the values are dependant upon the code running successfully
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months {total_months}")
print(f"Total: {net_profit}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")
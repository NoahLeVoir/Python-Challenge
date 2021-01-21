# Import modules
import os
import csv

# Set path for the csv file in the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# PLACEHOLDER
# Will Dim the variables here before the 'with' opens the csv

# Open the CSV and make sure that it is being read
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print csvreader to make sure everything is set up correctly
    print(csvreader)

    # Recognize the header row, and know to skip when working with the rest of the rows
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")








#-------------------------------------------------#
# Print Statements (Test)
# The text print statements and formatting are taken directly from the homework instructions, the values are dependant upon the code running successfully
print("Election Results")
print("-------------------------")
print("Total Votes: ")
print("-------------------------")


#The data we need to retrieve
#1. the total numbere of votes cast
#2. a complete list of candidates who received votes
#3. the perecentage eof votets each candidate won
#4. thet total numbere of votets each candidatte won
#5. the winner of tthe election based on popular vote

# Open the election results and read the file.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
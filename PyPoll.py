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

# 1. Initialize a total vote counter.
total_votes = 0

#Declare a new blank list for the names of the candidates.
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row while we're using this existing loop.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(candidate_votes)

# Print the candidate list.
# print(candidate_options)

# 3. Print the total votes.
# print(total_votes)
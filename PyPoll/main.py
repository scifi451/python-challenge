#main.py in PyPoll

import os
import csv

# set the path
csvpath = os.path.join( 'election_data.csv')

# initialize the variables
total_votes = 0
candidate_option = []
candidate_vote = {}
winning_count = 0

# open the election_data.csv
with open(csvpath, newline="") as csvfile:
   # read the rows
   csvreader=csv.reader(csvfile,delimiter=",")
  #Skips the header row
   csv_header = next(csvreader)
   # loop through the rows and add them to the dictionary if not already there.
   for row in csvreader:
    total_votes = total_votes + 1 
    candidate_name = row[2]
    if candidate_name not in candidate_option:
        candidate_option.append(candidate_name)
        candidate_vote[candidate_name]=0
    candidate_vote[candidate_name]= candidate_vote[candidate_name]+1
    #winning vote count for candidate
    for candidate in candidate_vote:
       votes = candidate_vote.get(candidate)
       vote_percentage = float(votes) / float (total_votes)  * 100

      # find winning vote count and candidate
       if votes > winning_count: 
            winning_count = votes
            winning_candidate = candidate
print(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
print(f"{winning_candidate}")
      #print(row) using this to make sure code works.
      #If Khan  not in dictionary add them to it, if so add to count.

      #If Correy not in dictionary add them to it, if so add to count.

      #If Li not in dictionary add them to it, if so add to count.

      #If O'Tooley not in dictionary add them to it, if so add to count.

      #Get total votes for votes cast

      #complete list of candidates who received votes

      #The percentage of votes each candidate won

#look up how  see if someone is in a dictionary and then add them if not in the dictionary.
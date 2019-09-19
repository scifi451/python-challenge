#main.pay in PyPoll

import os
import csv

# set the path
csvpath = os.path.join( 'election_data_slim.csv')

# initialize the variables
total_votes = 0
total_months = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# open the election_data.csv
with open(csvpath, newline="") as csvfile:
   # read the rows
   csvreader=csv.reader(csvfile,delimiter=",")
  #Skips the header row
   csv_header = next(csvfile)
   # loop through the rows and add them to the dictionary if not already there.
   for row in csvreader:
      #print(row) using this to make sure code works.
      #If Khan  not in dictionary add them to it, if so add to count.

      #If Correy not in dictionary add them to it, if so add to count.

      #If Li not in dictionary add them to it, if so add to count.

      #If O'Tooley not in dictionary add them to it, if so add to count.
      

#look up how  see if someone is in a dictionary and then add them if not in the dictionary.
import csv
import os

# Assign a variable for the file to load and the path.
# file_to_load='Resources_Election_Analysis\election_results.csv'
file_to_load=os.path.join('Resources_Election_ANalysis','election_results.csv')
file_to_save=os.path.join('Resources_Election_ANalysis','election_outcome.txt')

# Open the election results and read the file.
# election_data=open(file_to_load,'r')
election_outcome=open(file_to_save,'w')
#BETTER -->
# use "with" instead of open & close
with open(file_to_load) as election_data:


# To Do: perform analysis.
    print(election_data)

# To Do: Close the file.
# election_data.close()








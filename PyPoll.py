
######################################################
#Add our dependencies (Modules that we're using)
import csv
import os

# Name the data file that we'll be reading from
elec_data='Resources_Election_Analysis/election_results.csv'
# create a new file to write to
elec_outcome='Resources_Election_Analysis\election_outcome.txt'

# initialize the total_voter_counter variable BEFORE opening the file - of type=integer
# & initialize the candidates list variable - list
# && initialize the candidates votes variable - dictionary
# &&& winning variables - candidate, votes, vote_pct
# &&&& CHALLENGE VARIABLES 
total_votes=0
cand_list=[]
cand_votes={}
win_cand=''
win_votes=0
win_pct=0
county_list=[]
county_votes={}
most_votes_county=0
big_county=''

#open the file that we're READING first
with open(elec_data) as election_data:
    
    ###read and analyze the data here

    #1. read the file with the reader function in the csv module
    file_reader=csv.reader(election_data)
    #1z. print the entire file as a test that its reading it correctly
    # for row in file_reader:
    #     print(row)
    
    #2. read the header row
    headers=next(file_reader)
    
    #3. loop through the csv file to find the total_votes
    for row in file_reader:
        total_votes+=1
#3z. print the vote total to check
# print(f'the total number of votes is: {total_votes}')

        #4. (continue to) loop through the csv file to find all candidate names
        cand_name=row[2]
        #4aa. use an if statement to determine uniqueness
        if cand_name not in cand_list:
            #4a. add the candidate name to the list
            cand_list.append(cand_name)
#4z. print the candidate list to check
# print(cand_list)

            #5. (continue to) loop through the csv file & stay in the IF statement...
            #  begin to tally vote count
            cand_votes[cand_name]=0
        #5a. add votes to the vote count for each candidate BUT move out of the if statement...
        # because the if statement was setting the list of all candidates, and setting each one of their counters to zero
        # now we want to have it do a plus+1 every time we see the candidate name, which is not logically part of the if statement
        cand_votes[cand_name]+=1
#5z. print the candidate vote dictionary to check
# print(cand_votes)
#############CHALLENGE WORK STARTS HERE - COUNTY INFORMATION
#####chal_1. VOTER TURNOUT FOR EACH COUNTY
        county_name=row[1]
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name]=0
        county_votes[county_name]+=1

#8.  write results to a .txt file, include a header "Election Results" and total vote count above the candidates info
# we're jumping in @#8 out of order here, because of the way the Module was laid out...
with open(elec_outcome,'w') as resfile:
    election_results=(
        f'\nElection Results\n'
        f'-------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------\n'
        f'\nCounty Votes:\n'
    )
    print(election_results)
    resfile.write(election_results)
#####chal_2. % OF TOTAL_VOTES FROM EACH COUNTY
    for county_name in county_votes:
        cvotes=county_votes[county_name]
        cpct=float(cvotes)/float(total_votes)*100
        each_county=(f'{county_name}: {cpct:,.1f}% ({cvotes:,})\n')
        print(each_county)
        resfile.write(each_county)
#####chal_3. HIGHEST COUNTY TURNOUT
        if cvotes>most_votes_county:
            most_votes_county=cvotes
            big_county=county_name
    county_win_blurb=(
        f'\n-------------------\n'
        f'Largest County Turnout: {big_county}\n'
        f'-------------------\n'
    )
    print(county_win_blurb)
    resfile.write(county_win_blurb)


#####chal_4. PRINT RESULTS IN TERMINAL
#####chal_5. WRITE RESULTS TO TXT FILE
    #6. determine percentage of total votes each candidate got
    # we're over here, flush with the left margin, because we're done with the for-loop
    # AND we're done reading the csv file, completely
    ###
    # loop through the dictionary, and declare votes and vote_pct with formulae
    for cand_name in cand_votes:
        votes=cand_votes[cand_name]
        vote_pct=float(votes)/float(total_votes)*100
        # 6aa. store a line of text for each candidate as each_cand, print & write to the txt file
        each_cand=(f'\n{cand_name}: received {vote_pct:.1f}%  ({votes:,})\n')
        print(each_cand)
        resfile.write(each_cand)
        ###
        #6a. still in the for-loop, check each variable votes vs the winning vote count variable
        # & replace/update all the winning variables if the amount is greater than
        if votes>win_votes:
            win_cand=cand_name
            win_votes=votes
            win_pct=vote_pct
    #7z.  print check
    # print(win_cand)
    # print(win_votes)
    # print(f'{win_pct:.2f}%')
    #7.  print winning candidate with f string & all winning variables & write to txt file
    win_summary=(
        f'\n-------------------\n'
        f'Winner: {win_cand}\n'
        f'Winning Vote Count: {win_votes:,}\n'
        f'Winning Percentage: {win_pct:.2f}%\n'
        f'-------------------'
    )
    print(win_summary)
    resfile.write(win_summary)
















































































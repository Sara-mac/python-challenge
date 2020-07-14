#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os
import csv

#Create path to csv file
datapath = os.path.join('.', 'Resources', 'election_data.csv')
#open file and store it in a variable called csvfile
with open(datapath, newline='') as csvfile:
    pypoll_data = csv.reader(csvfile, delimiter=',')
    header= next (pypoll_data)
   # thisdict = {"voter_id":,"county":,"candidate":}

    candidate = []
    vote_tally = {}

    for x in pypoll_data:

      candidate = x[2]
      if candidate in vote_tally:
        vote_tally[candidate] = 1
      else:
        vote_tally[candidate] = vote_tally[candidate] + 1

print(vote_tally)



 # vote_count = []
  #  votes = 0 
  #  received_candidates = []
 #   candidate = []'''
    #csv_header = next(reader) # Stores Header Row
   
#The total number of votes cast
#print(len(received_candidates))

#A complete list of candidates who received votes


#for received_candidates in range(len(candidate)):
  #  for row in reader:
      
    #for row in reader:
    #key = row[0]
    #result[key] = row[1:]
        #print(row)
        #break 
#print (OrderedDict["Candidate"])
#print (list(set(received_candidates)))
#print (received_candidates)

#Figure out how many votes each candidate recieved:



#The percentage of votes each candidate won
#(Total votes each candidate recieved divided by )

#The total number of votes each candidate won


#The winner of the election based on popular vote.





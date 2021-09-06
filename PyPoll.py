# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of the candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Add our dependancies
import csv
import os

# Assign a variable to load a file from a path
file_to_load= os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")

# Inititalize a total vote counter
total_votes=0

#Candidate options
candidate_options=[]

#Declare empty dictionary
candidate_votes={}

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Winning candidate and Winning count Tracker
    winning_candidate=""
    winning_count=0
    winning_percentage=0

    #Read the header row
    headers=next(file_reader)

    for row in file_reader:
        #Add to the total vote count
        total_votes +=1

        #Print the candidate name from each row
        candidate_name=row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name]=0
        #Add vote to candidate's count
        candidate_votes[candidate_name]+=1
        

    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of the candidate
        votes=candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage=float(votes)/float(total_votes)* 100
        #Print the candidate name and percentage of votes
        print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote.')

    #Determine if the votes are greater than the winning count
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            #If true then set winning_count=votes and winning_percent=vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage
            #Set the winning_candidate equal to the candidate's name
            winning_candidate=candidate_name

           # print out each candidate's name, vote count, and percentage of votes to the terminal
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary=(f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    '-----------------------------\n')
    print(winning_candidate_summary)

# Print the total votes
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)
   
#Using the with statement open the file as a text file.
with open(file_to_save,'w') as txt_file:
    outfile=open(file_to_save,'w')
#write data to file
   
   





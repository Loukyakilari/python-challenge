# Import Modules
import os
import csv

# set path for file
election_path = os.path.join( "Resources","election_data.csv")

# Determine the variables
total_votes=0
current_candidate=[]
candidate_vote={}
unique_candidate_list=[]
winnercount=0 

#Open the csv
with open(election_path,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvreader)
    
    for row in csvreader:
           total_votes += 1
           current_candidate=row[2]
    
           if current_candidate not in unique_candidate_list:
                unique_candidate_list.append(current_candidate)
                candidate_vote[current_candidate]=1
           else:
                candidate_vote[current_candidate]+=1

# Print statements             
print("Election Results")
print(".....................................")        
print(f'Total Votes: {total_votes}')
print(".....................................")
for c in candidate_vote:
    individual_vote=round(candidate_vote[c]*100/(total_votes),3)
    if candidate_vote[c]>winnercount:
        winnercount=candidate_vote[c]
        winner=c
    print(f'{c} : {individual_vote}% ({candidate_vote[c]})')
print(".....................................")   
print(f'Winner: {winner}')
print("......................................")    
    
  

# Export the results to txt file
file_to_output = os.path.join("Analysis", "election_analysis.txt")      
with open(file_to_output,"w") as txt:

    txt.write("Election Results")
    txt.write("\n")
    txt.write(".....................................")
    txt.write("\n")
    txt.write(f'Total Votes: {total_votes}')
    txt.write("\n")
    txt.write(".....................................")
    txt.write("\n")
    for c in candidate_vote:
        individual_vote=round(candidate_vote[c]*100/(total_votes),3)
        if candidate_vote[c]>winnercount:
           winnercount=candidate_vote[c]
           winner=c
        txt.write(f'{c} : {individual_vote}% ({candidate_vote[c]})\n')   
    txt.write(".....................................")
    txt.write("\n")
    txt.write(f'Winner: {winner}')
    txt.write("\n")
    txt.write("......................................")
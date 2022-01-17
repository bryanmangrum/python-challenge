from distutils.errors import LibError
import os
import csv

# set path for file

csvpath = os.path.join("Resources", "election_data.csv")

# set variables
count = 0
candidates = []
unique_candidates = []
Khan_Vote = 0
Correy_Vote = 0
Li_Vote = 0
OTooley_Vote = 0
vote_tally = [Khan_Vote, Correy_Vote, Li_Vote, OTooley_Vote]

# setup to read data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(csvreader)

    for row in csvreader:
       #The total number of votes cast
       count += 1
       #A complete list of candidates who received votes
       candidates.append(row[2])

for name in candidates:
        if name not in unique_candidates:
            unique_candidates.append(name)
#start new if statement
        if name == 'Khan':
            Khan_Vote += 1

        elif name == 'Correy':
            Correy_Vote += 1
        
        elif name == 'Li':
            Li_Vote += 1

        else:
            OTooley_Vote += 1

winning_vote_count = max(vote_tally)
winner = unique_candidates[vote_tally.index(winning_vote_count)]


# print(unique_candidates)
# print(count)    
# print(Khan_Vote)
# print(Correy_Vote)
# print(Li_Vote)
# print(OTooley_Vote)
# print(winner)

print("Election Results")
print("-------------------------")  
print(f"Total Votes: {count}")
print("-------------------------")
print(f"Khan: {round((Khan_Vote/count)*100, 2)}% ({Khan_Vote})")      
print(f"Correy: {round((Correy_Vote/count)*100, 2)}% ({Correy_Vote})")     
print(f"Li: {round((Li_Vote/count)*100, 2)}% ({Li_Vote})")     
print(f"O'Tooley: {round((OTooley_Vote/count)*100, 2)}% ({OTooley_Vote})")
print("-------------------------") 
print(f"Winner: {winner}")  
print("-------------------------")


#export to text file
outpath = os.path.join('analysis', 'pypoll_output.txt')
with open(outpath, "w") as text:
        text.write('Election Results\n')
        text.write('-------------------------\n')
        text.write(f"Total Votes: {count}\n")
        text.write('-------------------------\n')
        text.write(f"Khan: {round((Khan_Vote/count)*100, 2)}% ({Khan_Vote})\n")
        text.write(f"Correy: {round((Correy_Vote/count)*100, 2)}% ({Correy_Vote})\n")
        text.write(f"Li: {round((Li_Vote/count)*100, 2)}% ({Li_Vote})\n")
        text.write(f"O'Tooley: {round((OTooley_Vote/count)*100, 2)}% ({OTooley_Vote})\n")
        text.write('-------------------------\n')
        text.write(f"Winner: {winner} \n")
        text.write('-------------------------\n')




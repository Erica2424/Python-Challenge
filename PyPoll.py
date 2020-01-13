import os
import csv

election_data_csv = os.path.join(".","Resources", "election_data.csv")

total_votes = []
candidate_list= []
candidate =[]
vote_count =[]
vote_percentage =[]

with open (election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)


    for i in csv_reader:
        total_votes.append(i["Voter ID"])
        candidate_list.append(i["Candidate"])

    for b in set(candidate_list):
        candidate.append(b)
        c = candidate_list.count(b)
        vote_count.append(c)
        d = (c/len(candidate_list))*100
        vote_percentage.append(d)

    max_votes = max(vote_count)
    winner = candidate[vote_count.index(max_votes)]

print("Election Results:")
print("Total Votes: " +str(len(total_votes)))
print("Candidates:" + str(vote_count))
print("Total Votes:"+ str(vote_count))
print("Vote Percentages:" + str(vote_percentage))
print(f"Winner:" + {winner})

with open(election_data_csv, "w") as txt_file:
    txt_file.write("Election Results:"+ "\n")
    txt_file.write("Total Votes:" + +str(len(total_votes)) +"\n")
    txt_file.write("Candidates:" + str(vote_count))+ "\n")
    txt_file.write("Vote Percentages:" + str(vote_percentage))+"\n")
    txt_file.write(f"Winner:" + {winner}))+"\n")

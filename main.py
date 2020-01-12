import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")

#total months
months = 0
#net total profit/losses
total = 0
#change in average
change= 0
change_list = []
with open(budget_csv) as data:
    csv_reader= csv.reader(data)
    header=next(csv_reader)
    first_row= next(csv_reader)
    total = total+int(first_row[1])
    months+=1
    previous_row= int(first_row[1])
    for i in csv_reader:
        months+=1
        total = total+int(i[1])
        change= int(i[1])- previous_row
        previous_row = int(i[1])
        change_list.append(change)
        print(i)
        print(months)
        print(total)
average= sum(change_list)/len(change_list)
print(average)
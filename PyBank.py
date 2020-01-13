import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")
financial_anaylsis= os.path.join("financial_analysis.txt")
#total months
months = 0
#net total profit/losses
total = 0
#change in average
change= 0
change_list = []
greatest_change_list =["", 0]
greatest_decrease_list = ["", 1000000000]
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
        if change > greatest_change_list[1]:
            greatest_change_list[0] = i[0]
            greatest_change_list[1] = change
        if change < greatest_decrease_list[1]:
            greatest_decrease_list[0]= i[0]
            greatest_decrease_list[1]= change
        
average= sum(change_list)/len(change_list)
print(average)
print(months)
print(total)
print(f"{greatest_change_list[0]} {greatest_change_list[1]}")
print(f"{greatest_decrease_list[0]} {greatest_decrease_list[1]}")

summary = (
    f"average: {average}\n"
    f"months: {months}\n"
    f"total: {total}\n"
    f"greatest increase: {greatest_change_list[0]} {greatest_change_list[1]}\n"
    f"greatest decrease: {greatest_decrease_list[0]} {greatest_decrease_list[1]}\n"
)
with open(financial_anaylsis,"w") as file_:
    file_.write(summary)
import os
import csv
#Create path to csv file
datapath = os.path.join('.', 'Resources', 'budget_data.csv')
#open file and store it in a variable called csvfile
with open(datapath) as csvfile:
    reader = csv.reader(csvfile)
    diff_list = [] # creates a list to store differences between months
    previous = 0 # stores previous month's difference
    month = 0 # stores the month
    total = 0
    csv_header = next(reader) # Stores Header Row
    # Loop through each row of csvfile
    for row in reader:
        month += 1 #adds the next month to the previous month and assigns the new value to the variable
        current = int(row[1])
        total += current
       # print(f'Current: {current} Previous: {previous}') commented out for my reference
        # find the difference between the current month and the previous month
        if previous != 0:
            difference = current - previous
            previous = current
        else:
            difference = 0
            previous = current #accounts for the first month not having a difference
#       print(difference)
        diff_list.append(difference)
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: ", (month))
average = round(sum(diff_list) / (month -1),2)
#print (sum(diff_list))
#index = diff_list.index 
print ("Total: $",total)
print ("Average Change: $", average)


maximum = max(diff_list)
print ("Greatest Increase in Profits: $", (maximum))
minimum = min(diff_list)
print ("Greatest Decrease in Profits: $", (minimum))

with open("Analysis/output","w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n")
    textfile.write("------------------------")
    textfile.write("\n")
    textfile.write(f"Total Months:{(month)}")
    textfile.write("\n")
    textfile.write(f"Total: ${sum(diff_list)}")
    textfile.write("\n")
    textfile.write(f"Average Change: $ {round(sum(diff_list)/len(diff_list),2)}")
    textfile.write("\n")
    textfile.write(f"Greatest Increase in Profits: (${(str(maximum))})")
    textfile.write("\n")
    textfile.write(f"Greatest Decrease in Profits: (${(str(minimum))}")
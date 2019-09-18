#main.pay in PyPoll

import os
import csv

# set the path
csvpath = os.path.join( 'election_data_slim.csv')

# initialize the variables
total_votes = 0
total_months = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# open the election_data.csv
with open(csvpath, newline="") as csvfile:
   # read the rows
   csvreader=csv.DictReader(csvfile,delimiter=",")
  #SKips the header row
   csv_header = next(csvfile)
   # loop through the rows and add them to the lists
   for row in csvreader:

################## From Py Bank need to tweak at least variable names or ?
       # increment the total months
       total_months += 1
       print(f"total months: {total_months}")
       # add to the total_profits
       total_profits = int(row[1]) + total_profits 
       print("Total Profit: " + str (total_profits))
       # if the total_months == 1 save the profit to the last_value
       if total_months == 1:
          previous_row = int(row[1])
       # else if total_months > 1 calcuate the change from last value, and set the last_value to the current month value
       elif total_months > 1:
         monthly_change = int(row[1]) - previous_row
         previous_row = int(row[1])
       print("monthly change:" + str(monthly_change)) 
       # add to the total monthly changes
       total_monthly_changes = total_monthly_changes + monthly_change

       # if the g_increase_value is less than the current value set it to the current month value
       if g_increase_value > g_increase_value:
         g_increase_value = g_increase_value + int(row[1]) 
         g_increase_month = g_increase_month + row[0]
       print(f"Greatest Increase in Profits:{g_increase_month} (${g_increase_value})")  
      # if the g_decrease_value is greater than the current valuhe set it the current month value
       if g_decrease_value > g_decrease_value:
         g_decrease_value = g_decrease_value + int(row[1]) 
         g_decrease_month = g_decrease_month + row[0]
       print(f"Greatest Decrease in Profits:{g_decrease_month} (${g_decrease_value})")  

average_monthly_changes = total_monthly_changes / (total_months - 1)
print(f"Average Monthly Changes: {average_monthly_changes}")                



#print the finanacial analysis
# print("Financial Analysis")
# print("--------------------")
# print(f"Total Months: {total_months} ")
# print(f"Total: ${total_profits}")
# print(f"Average change ${round(float(total_monthly_changes/(total_months-1)),2)}")
# print(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})")
# print(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})")
#write it to a text file
#output_path= os.path.join("..","PyBank_output.txt")
# open the file
# with open (output_path, 'w', newline='') as txtfile:
#     # write rows
#     txtwriter = txtfile.write("Financial Analysis\n")
#     txtwriter = txtfile.write("--------------------\n")
#     txtwriter = txtfile.write(f"Total Months: {totalMonths}\n")
#     txtwriter = txtfile.write(f"Total: ${totalProfits}\n")
#     txtwriter = txtfile.write(f"Average change ${round(float(sum_of_changes/(totalMonths-1)),2)}\n")
#     txtwriter = txtfile.write(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})\n")
#     txtwriter = txtfile.write(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})\n")
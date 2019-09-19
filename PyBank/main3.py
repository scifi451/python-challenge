#Here an example pseudo+starter code for the PyBank.
# PyBank main.py
import os
import csv
# set the path
budget_data_csv = os.path.join("..","Resources" , "budget_data.csv")

# initialize the variables
total_profits = 0
total_months = 0
monthly_change = 0
total_monthly_changes = 0
g_increase_value = 0
g_increase_month = ""
g_decrease_value = 0
g_decrease_month = ""

# open the budget_data.csv
with open(budget_data_csv, newline="") as csvfile:
   # read the rows
   csvreader=csv.reader(csvfile,delimiter=",")
  #SKips the header row
   csv_header = next(csvfile)
   # loop through the rows and add them to the lists
   for row in csvreader:
       # increment the total months
       total_months += 1
       #print(f"total months: {total_months}")
       # add to the total_profits
       total_profits = int(row[1]) + total_profits 
       #print("Total Profit: " + str (total_profits))
       # if the total_months == 1 save the profit to the last_value
       if total_months == 1:
          previous_row = int(row[1])
       # else if total_months > 1 calcuate the change from last value, and set the last_value to the current month value
       elif total_months > 1:
         monthly_change = int(row[1]) - previous_row
         previous_row = int(row[1])
       #print("monthly change:" + str(monthly_change)) 
       # add to the total monthly changes
       total_monthly_changes = total_monthly_changes + monthly_change

       # if the g_increase_value is less than the current value set it to the current month value
       if monthly_change  > g_increase_value:
         g_increase_value = monthly_change 
         g_increase_month =  row[0]
       #print(f"Greatest Increase in Profits:{g_increase_month} (${g_increase_value})")  
      # if the g_decrease_value is greater than the current valuhe set it the current month value
       if g_decrease_value > monthly_change:
         g_decrease_value = monthly_change 
         g_decrease_month =  row[0]
       #print(f"Greatest Decrease in Profits:{g_decrease_month} (${g_decrease_value})")  

average_monthly_changes = total_monthly_changes / (total_months - 1)
#print(f"Average Monthly Changes: {average_monthly_changes}")         
#print the finanacial analysis
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months} ")
print(f"Total: ${total_profits}")
print(f"Average change ${round(float(total_monthly_changes/(total_months-1)),2)}")
print(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})")
print(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})")
#write it to a text file
output_path= os.path.join("PyBank_output.txt")
# open the file
with open (output_path, 'w', newline='') as txtfile:
     # write rows
     txtwriter = txtfile.write("Financial Analysis\n")
     txtwriter = txtfile.write("-----------------------\n")
     txtwriter = txtfile.write(f"Total Months: {total_months}\n")
     txtwriter = txtfile.write(f"Total: ${total_profits}\n")
     txtwriter = txtfile.write(f"Average change ${round(float(average_monthly_changes/(total_months-1)),2)}\n")
     txtwriter = txtfile.write(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})\n")
     txtwriter = txtfile.write(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})\n")
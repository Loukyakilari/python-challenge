# Import Modules
import os
import csv

# set path for file
budget_path = os.path.join( "Resources","budget_data.csv")

# Define the variables
total_months=0
total_revenue=0
revenue=[]
list_of_revchange=[]
month=[]


#Open and read the csv
with open(budget_path,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    next(csvreader)

    for row in csvreader:
       
        # Calculate the number of months
        total_months += 1
        month.append(row[0])
      

        # calculate the total revenue        
        total_revenue=total_revenue+int(row[1])
        revenue.append(int(row[1]))
        
       
    for i in range(1,len(revenue)): 
        
        # Calculate the revenue change
        revenue_change=(revenue[i]-revenue[i-1])
        list_of_revchange.append(revenue_change)

        # Calculate the average of revenue change
        average_revenue_change=(round(sum(list_of_revchange)/len(list_of_revchange),2)) 

        # Calculate the greatest increase
        max_rev_change = max(list_of_revchange)
        max_rev_date=str(month[list_of_revchange.index(max(list_of_revchange))+1])
        
        # Calculate the greatest decrease
        min_rev_change=min(list_of_revchange)        
        min_rev_date=str(month[list_of_revchange.index(min(list_of_revchange))+1])

      
# Print statements
print("Financial Analysis")
print("..................................") 
print(f'Total Months: {total_months}')       
print(f'Total: ${total_revenue}')
print(f'Average Change : $ {average_revenue_change}')
print(f'Greatest Increase in Profits: { max_rev_date}  (${max_rev_change})')
print(f'Greatest decrease in Profits: { min_rev_date}  (${min_rev_change})')

# Export the results to text file
file_to_output = os.path.join("Analysis", "budget_analysis.txt")      
with open(file_to_output,"w") as txt:
    txt.write("Financial Analysis")
    txt.write("\n")
    txt.write("..................")
    txt.write("\n")
    txt.write(f'Total Months: {total_months}') 
    txt.write("\n")
    txt.write(f'Total: ${total_revenue}')  
    txt.write("\n")
    txt.write(f'Average Change : $ {average_revenue_change}')
    txt.write("\n")
    txt.write(f'Greatest Increase in Profits: { max_rev_date}  (${max_rev_change})')
    txt.write("\n")
    txt.write(f'Greatest decrease in Profits: { min_rev_date}  (${min_rev_change})')
    
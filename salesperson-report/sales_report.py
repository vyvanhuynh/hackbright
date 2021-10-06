# """Generate sales report showing total melons each salesperson sold."""


# salespeople = [] # create an empty list to add sale people
# melons_sold = [] # create an empty list to add the number of sold melons

# f = open('sales-report.txt') # open the report text file
# for line in f: # loop through each line in the text file, remove the white space and split the entries separated by "|"
#     line = line.rstrip()
#     entries = line.split('|')

#     salesperson = entries[0] # assign the entry at index 0 to the 'salesperson' variable
#     melons = int(entries[2]) # assign the entry at index 2 as an interger to the 'melons' variable

#     if salesperson in salespeople: # check if the person is already mentioned in the salespeople list, if yes, do the below
#         position = salespeople.index(salesperson) # get the position of that sale person in the salespeople list

#         melons_sold[position] += melons # add the number of melons sold at the same according index in the melons_sold list
#     else: # if the person has not been mentioned in the salespeople list
#         salespeople.append(salesperson) # add the sale person to the salespeople list
#         melons_sold.append(melons) # add the number of melons to the melons_sold list 


# for i in range(len(salespeople)): # loop through the index in the salespeople list and print out the result
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons') 


# """Generate sales report showing total melons each salesperson sold."""
import sys

f = open('sales-report.txt')
sale_dict = {}
for line in f:
    line = line.rstrip()
    entries = line.split('|')
   

    key = entries[0]
    value = int(entries[2])

    
    if key in sale_dict.keys():
        sale_dict[key] = sale_dict[key] + value
    else:
        sale_dict[key] = value

for person, melon in sale_dict.items():
    print(f'{person} sold {melon} melons')

"""Generate sales report showing total melons each salesperson sold."""
import sys

# Define empty lists
salespeople = []
melons_sold = []

# define the file
f = open('sales-report.txt')
# iterate each line in file
for line in f:
    
    #split each line by '|'
    line = line.rstrip()
    entries = line.split('|')

    # define each person and number of melons
    salesperson = entries[0]
    melons = int(entries[2])

    # find the index 
    if salesperson in salespeople:
        # find index of person in the list
        position = salespeople.index(salesperson)
        # increment number melons sold by melons
        melons_sold[position] += melons
    else:
        # if add salesperson the list
        salespeople.append(salesperson)
        # attach number of melons sold to list
        melons_sold.append(melons)

#print name and how many melons were sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#######################

def melons_sold_by_report(filename):
    

    melons_sold = {}

    with open(filename[1]) as file:

        for line in file:
            name, dollars_spent, melons = line.rstrip().split('|')

            if name in melons_sold:
                melons_sold[name] += int(melons)
            else:
                melons_sold[name] = int(melons)

        
    for name, melons in melons_sold.items():
        print(f'{name} sold {melons} melons')


print(melons_sold_by_report(sys.argv))













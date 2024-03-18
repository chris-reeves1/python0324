import csv
# create empty lists to store the data. 
companies = []
sales = []

# read data from file
with open('output.csv', newline='') as csvfile:  # r and w are not needed as csv module handles this. 
    reader = csv.reader(csvfile) # reader function from the module, its an iterator which reads all the lines. 
    next(reader) # skip the first line - we dont need the header data. 
    for row in reader: # iterates through each row - each row is represented as a list of strings.
        companies.append(row[0])
        sales.append([int(x.replace(",", "")) for x in row[1:]])

# sum the totals for each month. Complete the list comprehnsion below:
monthly_sum = [sum(x) for x in zip(*sales)] # zip(*sales) unpacks the lists in the sales list, into tuples, you need an item to iterate with and an expression to sum them.   

yearly_sum = {}
# make a for loop that adds companies as keys and sum of corressponding sales as values for the dictionary.
for i in range(len(companies)):
    yearly_sum[companies[i]] = sum(sales[i])

print("Monthly Sales:", monthly_sum)
print("Yearly Sales:")
for company, sales in yearly_sum.items():
    print(company, sales)
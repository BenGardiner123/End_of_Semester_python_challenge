# It will then:

# Count the amount of numbers
# Find the max/highest number
# Find then min/lowest number
# Calculate the average to two decimal places
# Find the most repeated/occurring number
# Find the amount of unique numbers
 

# The following need to be in your code at least once:

# function
# list
# loop
# selection

# Open the file for reading.
my_list = [];
with open('numbers.csv', 'r') as infile:

    data = infile.read()  # Read the contents of the file into memory.

# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()
print (my_list)

for i in range(1, len(my_list)):
    my_list[i] = int(my_list[i])
print ("Modified list is : " + str(my_list))





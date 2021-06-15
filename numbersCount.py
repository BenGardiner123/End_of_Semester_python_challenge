
# https://www.kite.com/python/answers/how-to-remove-newline-character-from-a-list-in-python
writeOutput = [];
numFile = open('numbers.csv').readlines()
firstline = numFile.pop(0)
for line in numFile:
    writeOutput.append(line.strip())
print(writeOutput)    

#attempt to convert the list
convertedList = list(map(int, writeOutput))
print(convertedList)

# Count the amount of numbers
print ("Total amount of nums : " + str(len(convertedList)))

# Find the max/highest number
print ("Max number : " + str(max(convertedList)))

# Find then min/lowest number
print ("Min num : " + str(min(convertedList)))

# Calculate the average to two decimal places
def calcAverage(targetList):
    return sum(targetList) / len(targetList)

result = calcAverage(convertedList)
print("The average : " + str(round(result, 2)))

# Find the most repeated/occurring number
from statistics import mode
mostOccuring = mode(convertedList)
print("The most occuring : " + str(mostOccuring))

# Number of times of the most occurring number 
def mostOccuringCounter(targetList):
    value = 26
    counter = targetList.count(26)
    print("The number appears : " + str(counter) + " times in the list")

mostOccuringCounter(convertedList)

# Find the amount of unique numbers
# using a set to create a list of unique nums 
# https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-a-list
uniqueValues = set(convertedList)
uniqueValuesCount = len(uniqueValues)
print(uniqueValuesCount)

# or
# https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python
def duplicateFinder(targetList):
    duplicateNums = []
    uniqueNums = []
    for i in targetList:
        if i in uniqueNums:
            duplicateNums.append(i)
        else:
            uniqueNums.append(i)
    print("The number of unique values in list is ", len(uniqueNums))
# call duplicate finder
duplicateFinder(convertedList)    



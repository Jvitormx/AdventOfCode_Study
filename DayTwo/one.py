"""
The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

-The levels are either all increasing or all decreasing.
-Any two adjacent levels differ by at least one and at most three.

"""

def createNewMatrix(lines):
     sortedLines = []
     
     for i in range(len(lines)):
        newLines = lines[i].replace(' ', '')
        lineInLines = []
        
        for j in range(len(newLines)):
            lineInLines.append(int(newLines[j]))
            
        if verifyOrder(lineInLines):
            lineInLines.sort()
            sortedLines.append(lineInLines)

     return sortedLines

def verifyOrder(lineInLines):
    if (all(lineInLines[i] <= lineInLines[i + 1] for i in range(len(lineInLines) - 1))) or (all(lineInLines[i] >= lineInLines[i + 1] for i in range(len(lineInLines) - 1))):
        return True
    else:
        return False

def safeQuantity(name):
    with open(name) as file:

        lines = [line.strip() for line in file]

        sortedLines = createNewMatrix(lines)

        safeCounter = 0

        limit = 1

        confirm = 1

        for i in range(len(sortedLines)):
            for j in range(len(sortedLines[i])-1):
                if limit >= 1 and limit <=3 :
                    limit = sortedLines[i][j+1] - sortedLines[i][j]
                else:
                    confirm = 0

            if confirm == 1:
                safeCounter += 1

            confirm = 1
            limit = 1
                
        return safeCounter
    
result = safeQuantity("test.txt")

print(result)

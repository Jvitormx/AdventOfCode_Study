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

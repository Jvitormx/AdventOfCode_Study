def similarityScore(name):
    with open(name) as file:

        esq = []
        dir = []
        soma = 0
        somaSimilarity = 0

        lines = [line.strip() for line in file]

        for i in range(len(lines)):
            separar = lines[i].split("   ")
            esq.append(int(separar[0]))
            dir.append(int(separar[1]))

        esq.sort()
        dir.sort()

        for i in range(len(esq)):
            for j in range(len(dir)):
                if esq[i] == dir[j]:
                    somaSimilarity += 1
            
            soma += esq[i] * somaSimilarity
            somaSimilarity = 0


        return soma
    
result = similarityScore("input.txt")

print(result)

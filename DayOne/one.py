def contar(name):
    with open(name) as file:

        esq = []
        dir = []
        soma = 0

        lines = [line.strip() for line in file]

        for i in range(len(lines)):
            separar = lines[i].split("   ")
            esq.append(int(separar[0]))
            dir.append(int(separar[1]))

        esq.sort()
        dir.sort()

        for i in range(len(esq)):
            if(esq[i] > dir[i]):
                soma += (esq[i] - dir[i])
            else:
                soma += (dir[i] - esq[i])

        return soma
    
um = contar("input.txt")

print(um)

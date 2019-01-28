import sys

# aumenta la recursividad limite que el sistema dispone. El numero es 1000
sys.setrecursionlimit(300000)

a = "\n".join([
    ".W.",
    ".W.",
    "..."
])

b = "\n".join([
    ".W.",
    ".W.",
    "W.."
])

c = "\n".join([
    "......",
    "...W..",
    "......",
    "......",
    "......",
    ".W...."
])

d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "......"
])

def path_finder(maze):
    lista = maze.split()
    down = len(lista)
    size = len(lista[down-1])
    # departure box 
    x = (0,0)
    a,b = x

    # we change string values ​​by integer
    for i in range(len(lista)):

        columns = []
        for j in lista[i]:
            if j == "W":
                columns.append(1)
            else:
                columns.append(0)
        lista[i] = columns

    #value that determines the exit box
    lista[down-1][size-1] = 3



    def travel(i, j):

 
        if lista[i][j] == 3:
            return [(i, j)]
 
        if lista[i][j] == 1:
            return []
 
        lista[i][j] = -1
 
        if i > 0 and lista[i - 1][j] in [0, 3]:                     # North
            path = travel(i - 1, j)
            if path: return [(i, j)] + path
 
        if j < len(lista[i]) - 1 and lista[i][j + 1] in [0, 3]: # West
            path = travel(i, j + 1)
            if path: return [(i, j)] + path
 
        if i < len(lista) - 1 and lista[i + 1][j] in [0, 3]:    # South
            path = travel(i + 1, j)
            if path: return [(i, j)] + path
 
        if j > 0 and lista[i][j - 1] in [0, 3]:                     # East
            path = travel(i, j - 1) 
            if path: return [(i, j)] + path
 
        return []

 

    for x in travel(a,b): a,b = x
    if lista[a][b] == 3:
        return True
    else:
        return False

def path_finder2(maze):
    g = maze.splitlines()
    end, bag = len(g[0]) -1 + len(g) * 1j - 1j, {0}
    grid = {x + y * 1j for y,l in enumerate(g) for x,c in enumerate(l) if '.' == c}
    while bag:
        if end in bag: return True
        grid -= bag
        bag = grid & set.union(*({z + 1j ** k for k in range(4)} for z in bag))
    return False

print(path_finder(c))
print(path_finder2(c))


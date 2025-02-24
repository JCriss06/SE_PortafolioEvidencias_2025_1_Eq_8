import random
#hay que separa el main clases funciones de
def create_vector(n):
    vector = []
    for i in range(n):
        vector.append(random.randint(1,15))
    #print(vector)
    return vector

def objetive(vector):
    vo = 0
    for i in range(len(vector)):
        vo += vector[i]**2
    #print("El valor objetivo es:",vo)
    return vo

def add_vector(m, inicio):
    V = []
    V.append(inicio)
    for i in range(m - 1):
        n = create_vector(len(inicio))
        V.append(n)
    print("listas generadas:", V)
    return V

def torneoBinario(V, totP):
    #totP  = numPar < m
    padres = []
    for i in range(totP):
        v1 = random.choice(V)
        v2 = random.choice(V)
        while v1 == v2:
            v2 = random.choice(V)
        obj_v1 = objetive(v1)
        obj_v2 = objetive(v2)
        if obj_v1 < obj_v2:
            padres.append(v1)
        else:
            padres.append(v2)
    return padres

if __name__ == '__main__':

    can = int(input("Ingrese el tamaño del vector: "))
    v = create_vector(can)
    objetive(v)
    lon = int(input("Ingrese el tamaño del vector de vectores: "))
    ale = add_vector(lon,v)
    torneoBinario(ale, 2)
import random as rnd

min = -10
max = 10

def fo(datos):
    res = sum(i ** 2 for i in datos)
    return res

def Vecindario(So):
    vector = So[:]
    idx = rnd.randint(0, len(So) - 1)
    valor = rnd.randint(min, max)
    vector[idx] = valor
    return vector

def busqueda_local(So):
    print("Solucion temporal: ", So)
    SBest = So[:]
    VBest = fo(SBest)
    it = 0
    max_it = 100
    while it < max_it and VBest != 0:
        So = Vecindario(So)
        VnSolucion = fo(So)

        if VnSolucion < VBest:
            VBest = VnSolucion
            SBest = So[:]
            print("nueva best solucion: ", SBest, end="    ")
            print("vo: ", VnSolucion)
        it += 1
    print(f"Mejor solucion: {SBest}")
    print(f"Mejor vo: {VBest}")

if __name__ == "__main__":
    So = [3,1,2,5,4] # Solucion inicial
    busqueda_local(So)







import random as rnd

def generaVa():
    externa = []
    for i in range(5): # filas 30
        interna = []
        for i in range(3): # columnas 100
            tem = rnd.randint(5,15)
            hum = rnd.randint(40,60)
            rui = rnd.randint(10,30)
            lum = rnd.randint(400,600)
            interna.append([tem,hum,rui,lum])
        #print(interna)
        externa.append(interna)
    return externa

preferencias = [[20,40],
                [30,150],
                [60,250],
                [400,1800]]

Vas = generaVa()

#for idx, f in enumerate(Vas, start=1):
#    print(f"{idx}: {f}")

for f in Vas:
    print(f)
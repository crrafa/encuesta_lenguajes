# Contador de lenguajes de programacion.
# Cuenta las veces que el lenguaje esta repetido en el archivo leguajes.log
# lo almacena en un diccionario con la cantidad de veces que se repitio.

# Diccionario [key:value]
contador = {}

# Abre lenguajes.log, agrega los lenguajes al diccionario contando sus repeticiones.
with open("lenguajes.log", "r") as datos:
    for i in datos:
        i = i.strip()
        if i not in contador:
            contador[i] = 1
        else:
            contador[i] += 1

# Ordena los lenguajes de forma desendiente
sort_lenguajes = sorted(contador.items(), key = lambda x : x[1], reverse = True)

# Imprime los lenguajes y su cantidad de menciones
for i in range(len(sort_lenguajes)):
    print("{}, {}".format(sort_lenguajes[i][0], sort_lenguajes[i][1]))
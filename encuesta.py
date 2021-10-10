# Encuesta tu lenguaje favorio.
# Muestra los lenguajes contenidos en lenguajes.log
# Recogue tu respuesta y la almacena en lenguajes.log

# Diccionario [key:value]
contador = {}

# Abre lenguajes.log, agrega los lenguajes al diccionario contando sus repeticiones.
with open("lenguajes.log", "r") as lectura:
    for i in lectura:
        elemento = i.strip()
        if item not in contador:
            contador[item] = 1
        else:
            contador[item] += 1

# Imprime los lenguajes
print("Elige tu lenguaje de programacion favorito:")
for item in contador:
    print(item)

# Entrada de respuesta
respuesta = input("¿Cual es tu lenguaje favorito? ")
respuesta = respuesta.upper()

# Guarda lenguaje ingresado en lenguajes.log
with open('lenguajes.log', 'a') as datos: 
    escribir = "{}\n".format(respuesta)
    datos.write(escribir)


# Imprime la cantidad de encuestados que han respondido lo mismo o si eres el primero en mensionar el lenguaje
try:
    print("Otros {} encuestados han respondido que su favorito es {} tambien".format(contador[respuesta], respuesta))
    exit(0)
except KeyError:
    print("Eres el primero que menciona ese lenguajes \"{}\".".format(respuesta))
    exit(0)
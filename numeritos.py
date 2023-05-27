numeros = [] #lista vacia, no puede ser una tupla porque esta no se puede editar (inmutable)
ordinales = ["primer", "segundo", "tercer", "cuarto", "quinto", "sexto"]

for iterador in range(6):
    leyenda = ("ingrese el " + ordinales[iterador] + " numero: ") 
    numero = input(leyenda)
    
    try:
     numeros.append(float(numero)) #append es para agregar contenido a la lista numero a numeros.
    except:
        print("solo se aceptan numero, por lo tanto su ingreso sera tomado como 0")
        numeros.append(0)

suma = 0 #inicia en 0 la lista por ser suma
producto = 1 #inicia en 1 la lista por ser multiplicacion
for valor in numeros: # valor tseria como una variable a mi entender.
    suma= suma + valor #lista en donde se guarda la suma el for recorre la lista.
    producto = producto * valor
    
print("-" * 70 )
print(". el numero mayor es: ", max(numeros))
print(". el numero menor es: ", min(numeros))
print(". La suma de todo los numeros es: ", suma)
print(".el producto final es", producto)
print("-" * 70)
nombre_archivo = input ("ingrese un nombre de archivo para analizar: ")
sigue = True

try:
    archivo = open(nombre_archivo, "r")
except:
     sigue = False
     print("archivo no encontrado")
     
if sigue == True:
  contenido = archivo.readlines()
     

  cantidad_caracteres = 0
  for parrafo in contenido:
    cantidad_caracteres = cantidad_caracteres + len(parrafo)

  print("cantidad de caracteres: ", cantidad_caracteres)
  print("cantidad de parrafos: ", len(contenido))
  archivo.close()
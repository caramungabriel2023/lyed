estudiantes = []
ingresos_invalidos = 0

while True:
    estudiante = input('Ingrese apellido y nombre del estudiante: ').strip().upper()
    if len(estudiante) == 0:
        break

    estudiante_trozado = estudiante.split()
    if len(estudiante_trozado) != 2:
        ingresos_invalidos += 1
        print('Solo puede ingresar apellido y nombre!')
        continue

    apellido = estudiante_trozado[0].strip()
    nombre = estudiante_trozado[1].strip()
    if apellido.isalpha() == False or nombre.isalpha() == False:
        ingresos_invalidos += 1
        print('Solo puede ingresar letras!')
    else:
        estudiante_validado = apellido + ' ' + nombre
        if estudiante_validado in estudiantes:
            ingresos_invalidos += 1
            print('Estudiante ya ingresado!')
        else:
            estudiantes.append(estudiante_validado)
            print('Ingresado OK!')

estudiantes.sort()

print('\nIngresos inválidos:', ingresos_invalidos)
print('\nLista ordenada de estudiantes:')
for elemento in estudiantes:
    print(elemento)
print('Cantidad:', len(estudiantes))

archivo = open('estudiantes.txt', 'w')
for estudiante in estudiantes:
    archivo.write(estudiante + '\n')
archivo.close()
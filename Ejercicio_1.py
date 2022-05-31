print("---------------------------------------")
print("---------- Caso 1 Centinela -----------")
print("---------- Notas Estudiantes ----------")
print("---------------------------------------")

cod = int(input("Ingrese el codigo del estudiante: "))
nombre = input("Ingrese el nombre del estudiante: ")

if cod != 0:
    nota1 = float(input("Digite la nota No.1: "))
    nota2 = float(input("Digite la nota No.2: "))
    nota3 = float(input("Digite la nota No.3: "))
else: 
    input("Fin de los datos de entrada.")

reprobados = 0

while cod != 0:
    nota_final = (nota1 + nota2 + nota3) / 3
    print("El estudiante con codigo ", str(cod), ", cuyo nombre es " + nombre + " tiene como nota final ", str(nota_final) )
    if nota_final < 3:
        reprobados = reprobados + 1
    
    cod = int(input("Ingrese el codigo del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    if cod != 0:
        nota1 = float(input("Ingrese la nota No.1: "))
        nota2 = float(input("Ingrese la nota No.2: "))
        nota3 = float(input("Ingrese la nota No.3: "))
    else: 
        print("Fin de los datos de entrada.")

print("La cantidad de estudiantes reprobados es ", str(reprobados))

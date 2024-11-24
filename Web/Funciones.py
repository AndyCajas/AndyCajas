print("Recibe un nombre y retorna un saludo")
def saludar(nombre):
    return f"Hola, {nombre}!"

nombre_usuario = input("Ingrese su nombre: ")

saludo = saludar(nombre_usuario)
print(saludo)

print("Función que recibe dos números y retorna su suma")
def sumar(num1, num2):
    return num1 + num2

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resultado = sumar(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es: {resultado}")

print("Función que verifica si un número es par o impar")
def es_par(num):
    if num % 2 == 0:
        return True  
    else:
        return False  

numero = int(input("Ingrese un número: "))

resultado = es_par(numero)
print(f"El número {numero} es {'par' if resultado else 'impar'}.")

print("Función que calcula el cuadrado de un número")
def calcular_cuadrado(num):
    return num ** 2

numero = float(input("Ingrese un número: "))

resultado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es: {resultado}")

import math

print("Función que calcula el área de un círculo")
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return round(area, 2)

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area} unidades cuadradas.")

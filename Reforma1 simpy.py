#Autores: Ana Ramírez y Diego Perdomo 
#
import simpy
import random
import math

tiempoT = 0
env = simpy.Environment() 
RAM = simpy.Container(env, init=100 , capacity=100)# Capacidad de ram
pro= simpy.Resource(env,capacity = 2)#cantidad de procesadores
#acumulador del total de tiempo utilizado para los procesos
Ttotal = 0
#arreglo que almacena los diferentes tiempos para calcular la desviacion estandar 
times = []
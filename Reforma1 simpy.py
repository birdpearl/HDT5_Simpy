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
def compu(env,inst,num,tiempo_llegada,RAM,pro):
    global times
    global Ttotal
    random_ram = 0 
    global tiempoT
    instrN = 0 
    yield env.timeout(tiempo_llegada)
    llegada = env.now ###########
    
    if RAM.level >= random_ram:
        random_ram = random.randint(1,10)
    
    tiempo_procesando = random_ram
    
    with RAM.get(random_ram) as turn:
        yield turn      
        yield env.timeout(tiempo_procesando) 
        
        instrN = inst - 3#intrucciones por entrada al procesador ########
        with pro.request() as simular:#######
            yield simular
            if(instrN <= 0):
                instrN = 0
            yield env.timeout(1)
            desicion = random.randint(1,2)
            if(desicion == 2):
                yield env.timeout(1)      
        if instrN<3:
            yield env.timeout(5)#intervalos de tiempo
        RAM.put(random_ram)
        
    tiempo = env.now - llegada    
    Ttotal = Ttotal + tiempo
    times.append(tiempo)
    print ('%s,%f' % (num, tiempo))
        
cantprocesos = 200 #cantidad de procesos
for i in range(cantprocesos):
    env.process(compu(env,random.randint(1,10),i,random.expovariate(1.0/1),RAM,pro))
env.run()
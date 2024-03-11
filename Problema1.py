
#9 2 3 2 3 3
def minimos_movimientos(lista_torres,cant_torres,guardados):
    
    #reviso que no tenga ciclos el codigo
    if lista_torres in guardados:
        tot_fichas = contar_fichas(lista)
        return (tot_fichas * cant_torres) ** 2
    else:
        guardados.append(lista_torres)
        comprobar = revisar(lista_torres,cant_torres)
        #miro si ya está organizada
        if comprobar == True:
            return 0
        else:
            #mira la tupla de la las posiciones del error por izquierda 
            error_izquierda = encontrar_error_izq(lista_torres,cant_torres) # (1,2)
            #mira la tupla de la las posiciones del error por derecha
            error_derecha  = encontrar_error_der(lista_torres, cant_torres) # 3, 4
            

            #si el error está en la misma tupla solo hay "un error" 
            if error_derecha == error_izquierda:
                #evalua resolver por izquierda [3,1,2] -> [2,2,2] o False (no es psoible hacer el cambio a la izq)
                cambio_izq = cambiar_por_izq(lista_torres,error_izquierda)
                #evalua resolver por derecha [3,2,2,4] -> [3,2,3,3] 
                cambio_derecha = cambiar_por_der(lista_torres,error_derecha)
                #revisa que ambos cambios son posibles
                if type(cambio_izq) == list and type(cambio_derecha) == list:
                    sol = 1 + min(minimos_movimientos(cambio_izq, cant_torres, guardados), minimos_movimientos(cambio_derecha, cant_torres, guardados))
                    guardados.remove(cambio_izq)
                    guardados.remove(cambio_derecha)
                    return  sol
                #si el cambio de la izquierda no es poosible, no lo considera
                elif type(cambio_izq) != list:
                     sol = 1 + minimos_movimientos(cambio_derecha, cant_torres, guardados)
                     guardados.remove(cambio_derecha)
    
                     return  sol
                #si el cambio no se puede por derecha (sea False)
                elif type(cambio_derecha) != list:
                     sol = 1 + minimos_movimientos(cambio_izq, cant_torres, guardados)
                     guardados.remove(cambio_izq)
                     return  sol
            #si hay error por izquierda y derecha
            else: 

                #Error por izquierda
                cambio_por_izq_izq = cambiar_por_izq(lista_torres,error_izquierda)
                cambio_por_der_izq = cambiar_por_der(lista_torres,error_izquierda)
                
                #Error por derecha
                cambio_por_izq_der = cambiar_por_izq(lista_torres,error_derecha)
                cambio_por_der_der = cambiar_por_der(lista_torres,error_derecha)

                #resolver

                if type(cambio_por_izq_izq) == list and type(cambio_por_der_izq) == list:
                    sol_izq  = 1 + min(minimos_movimientos(cambio_por_izq_izq, cant_torres, guardados), minimos_movimientos(cambio_por_der_izq, cant_torres, guardados))
                    guardados.remove(cambio_por_izq_izq)
                    guardados.remove(cambio_por_der_izq)
                #si el cambio de la izquierda no es posible, no lo considera
                elif type(cambio_por_izq_izq) != list:
                     sol_izq =  1 + minimos_movimientos(cambio_por_der_izq, cant_torres, guardados)
                     
                     guardados.remove(cambio_por_der_izq)
                #si el cambio no es posible por derecha
                elif type(cambio_por_der_izq) != list:
                     sol_izq =  1 + minimos_movimientos(cambio_por_izq_izq, cant_torres, guardados)
                     guardados.remove(cambio_por_izq_izq)
                     
        
                if type(cambio_por_izq_der) == list and type(cambio_por_der_der) == list:
                    sol_der  = 1 + min(minimos_movimientos(cambio_por_izq_der, cant_torres, guardados), minimos_movimientos(cambio_por_der_der, cant_torres, guardados))
                    guardados.remove(cambio_por_izq_der)
                    guardados.remove(cambio_por_der_der)
                #si el cambio de la izquierda no es posible, no lo considera
                elif type(cambio_por_izq_der) != list:
                     sol_der =  1 + minimos_movimientos(cambio_por_der_der, cant_torres, guardados)
                     
                     guardados.remove(cambio_por_der_der)
                #sie el cambio es posible por derecha
                elif type(cambio_por_der_der) != list:
                     sol_der =  1 + minimos_movimientos(cambio_por_izq_izq, cant_torres, guardados)
                     guardados.remove(cambio_por_izq_der)
                     
                
                return min(sol_der,sol_izq)
            

        

def encontrar_error_izq(lista_torres,cant):
    centinela = True
    i = 0
    error = None
    while i<cant-1 and centinela == True:
        torre1 = lista_torres[i]
        torre2 = lista_torres[i+1]
        if torre1 < torre2:
            centinela = False
            error = (i,i+1)
            
        i+=1
    return error

def encontrar_error_der(lista_torres,cant):
    centinela = True
    i = cant-1
    error = None
    while i> 0  and centinela == True:
        torre1 = lista_torres[i-1]
        torre2 = lista_torres[i]
        if torre1 < torre2:
            centinela = False
            error = (i-1,i)
            
        i-=1
    return error

def cambiar_por_izq(lista_torre, error):
    lista = lista_torre.copy()
    i,j = error
    if (i < 1) or (abs(lista_torre[i-1] - lista_torre[i]) <=1) or (lista_torre[i-1] <= lista_torre[i]):
        return False
    else: 
        lista[i] +=1
        lista[i-1] -=1
        return lista
    
def cambiar_por_der(lista_torre, error):
    lista = lista_torre.copy()
    i,j = error
    lista[j] -=1
    lista[i] +=1
    return lista


def revisar(lista_torres: list, cant_torres: int)->bool:
	centinela = True
	for i in range(0,cant_torres-1):
		torre1 = lista_torres[i]
		torre2 = lista_torres[i+1]
		if torre1 < torre2:
			centinela = False
	return centinela


def contar_fichas(lista):
    suma = 0
    for torre in lista:
        suma += torre
    return suma

lista1 = [3,2,2,4]
lista2 = [0,0,0,0,0,0,1]
lista3 = [32, 11, 7, 5, 1, 2, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
lista4 = [36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista5 = [3,0,1,1]
lista6 = [9,2,4,2,3,3]
lista = [0,0,50]
print(lista1)
print(minimos_movimientos(lista1,len(lista1),[]))
print("___________________________-")
print(lista2)
print(minimos_movimientos(lista2,len(lista2),[]))
print("___________________________-")
print(lista3)
print(minimos_movimientos(lista3,len(lista3),[]))
print("___________________________-")
print(lista4)
print(minimos_movimientos(lista4,len(lista4),[]))
print("___________________________-")
print(lista5)
print(minimos_movimientos(lista5,len(lista5),[]))
print("___________________________-")
print(lista6)
print(minimos_movimientos(lista6,len(lista6),[]))
print("___________________________-")
print(lista)
print(minimos_movimientos(lista,len(lista),[]))

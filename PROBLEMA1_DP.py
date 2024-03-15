def problema_torres(arreglo, cant_torres):
    
    torre_mas_alta = max(arreglo)
    total_fichas = total_fichas_f(arreglo)
    matriz_cubica =[]
    matriz_cubica = crear_matriz_inicial(matriz_cubica,total_fichas,torre_mas_alta,cant_torres)
    
    inicio = [0] * (cant_torres + 1)
    for i in range(1, cant_torres + 1):
        valor_calculado = inicio[i - 1] + arreglo[i - 1]
        inicio[i] = valor_calculado

    for i in range(2, cant_torres + 1): #filas
        for j in range(total_fichas + 1): #columnas
            por_ahora = inicio[i - 1]
            for k in range(j // i + 1): #profundidad
                valor_absoluto = calcular_valor_absoluto(j, k, por_ahora)
                if k <= torre_mas_alta:
                    lo_minimo_por_ahora = encontrar_minimo_movimientos(matriz_cubica[i - 1], j, k, i, torre_mas_alta)
                    matriz_cubica[i][j][k] = valor_absoluto + lo_minimo_por_ahora
    
    lo_minimo = minima_cant_movimientos(matriz_cubica,cant_torres,total_fichas)
    for k in range(1, total_fichas // cant_torres + 1):
        if matriz_cubica[cant_torres][total_fichas][k] < lo_minimo:
            lo_minimo = matriz_cubica[cant_torres][total_fichas][k]
    return lo_minimo

def total_fichas_f(torres):
    suma = 0
    for torre in torres:
        suma += torre
    return suma


def crear_matriz_inicial(matriz,tot_fichas,mas_alta, tot_torres): 
    for i in range(tot_torres + 1):
        matriz.append([[0] * (mas_alta + 1) for r in range(tot_fichas + 1)])
    for i in range(mas_alta + 1):
        matriz[0][i] = [0] * (mas_alta + 1)
        matriz[1][i] = [0] * (mas_alta + 1)
    return matriz
 
def minima_cant_movimientos(matriz,cant_torres,tot_fichas):
    lo_minimo = matriz[cant_torres][tot_fichas][0]
    for k in range(1, tot_fichas // cant_torres + 1):
        if matriz[cant_torres][tot_fichas][k] < lo_minimo:
            lo_minimo = matriz[cant_torres][tot_fichas][k]
    return lo_minimo

def calcular_valor_absoluto(j, k, por_ahora):
    diferencia = j - k
    diferencia_con_suma = diferencia - por_ahora
    valor_absoluto = abs(diferencia_con_suma)
    return valor_absoluto

def encontrar_minimo_movimientos(matriz, j, k, i, torre_mas_alta):
    minimos = matriz[j - k][k]
  
    for z in range(k, (j - k) // (i - 1) + 1):
        if z < torre_mas_alta and matriz[j - k][z] < minimos:
            minimos = matriz[j - k][z]
        
    return minimos

lista1 = [3,2,2,4]
lista2 = [0,0,0,0,0,0,1]
lista3 = [32, 11, 7, 5, 1, 2, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
lista4 = [36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista5 = [3,0,1,1]
lista6 = [9,2,4,2,3,3]
lista7 = [ 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,2 ,9 ,3 ,5 ,14 ,19 ,23 ,32]
lista8 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 6, 23, 29]
print(problema_torres(lista1,len(lista1)))
print(problema_torres(lista2,len(lista2)))
print(problema_torres(lista3,len(lista3)))
print(problema_torres(lista4,len(lista4)))
print(problema_torres(lista5,len(lista5)))
print(problema_torres(lista6,len(lista6)))
print(problema_torres(lista7,len(lista7)))
print(problema_torres(lista8,len(lista8)))
def quicksort(lst):
    #Paso base: Verifica si la lista paret de 0 o 1 elementos.
    if len(lst) <= 1:
        return lst

    #Declarar las listas para los elementos menores, iguales o mayores que el pivote.
    left = []
    middle = []
    right = []

    #Seleccionamos el pivote. En este caso será el primer elemento de la lista.
    pivot = lst[0]

    #Iterando sobre la lista, particionar los elementos en las listas left, middle y right.
    for x in lst:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    #Ordenar recursivamente las sublistas menores y mayores que el pivote
    return quicksort(left) + middle + quicksort(right)

#Ejemplo de lista
lst = [3, 6, 8, 10, 1, 2, 1]

#Llamada a la función
sorted_lst = quicksort(lst)

print(f"Lista original: {lst}")
print(f"List ordenada: {sorted_lst}")

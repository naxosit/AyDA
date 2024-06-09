#Link de extracción del codigo: https://github.com/Kashish24/hackerEarthCodingSolutions/blob/main/greedy-algorithm-to-find-minimum-number-of-coins.py

#Codigo modificado para CambioDeMonedas
#Definimos los valores de las monedas chilenas a usar
monedas = [10, 50, 100, 500]

#i es un índice que comienza desde el final de la lista 'monedas'
i = len(monedas) - 1

#Cantidad a cambiar
P = 2550
#Lista donde almacenaremos las monedas que usaremos para el cambio
total_monedas = []

# Mientras 'i' sea mayor o igual a 0, es decir, mientras no hayamos recorrido todas las monedas
while(i >= 0):
    # Si el valor de la moneda actual es menor o igual que P
    if (P >= monedas[i]):
          # Mientras el valor de la moneda actual sea menor o igual que P
        while (P >= monedas[i]):
            #Añadimos la moneda actual a total_monedas
            total_monedas.append(monedas[i])
            #Restamos el valor actual a P
            P -= monedas[i]
    #Decrementamos i para pasar a la siguiente moneda
    i -= 1

print(f'Total monedas usadas {len(total_monedas)} : ', sep=",")
print(*total_monedas)

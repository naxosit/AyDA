def minimo_monedas(monedas, P):
    # ordena las monedas en orden descendente
    monedas.sort(reverse=True)
    
    # número total de monedas inicial
    total_monedas = 0
    
    # Crea una lista que almacena el número de todas las monedas usadas
    num_monedas = [0] * len(monedas)
    
    # Recorre todas las monedas disponibles comenzando por la de mayor valor
    for i, moneda in enumerate(monedas):
        # Si el valor de la moneda es menor o igual que la cantidad P
        if P >= moneda:
            # Calcula cuantas monedas que cumplen se pueden usar
            num = P // moneda
            
            # Actualiza el total de monedas
            total_monedas += num
            
            # Almacena el número de monedas de este tipo usadas
            num_monedas[i] = num


###incompleto aun falta
#https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
#https://www.codespeedy.com/collect-all-coins-in-minimum-number-of-steps-in-greedy-method-in-python/
#code de Dipam Hazra


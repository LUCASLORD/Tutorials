numeros = list(range(18644,33088))

cond = False
qtd = 0
lista = []
for numero in numeros:
    numero = str(numero)
    
    for i in range(len(numero)):
        if numero[i] in '2':
            cond = True
            break
    
    for i in range(len(numero)):
        if numero[i] in '7':
            cond = False
            break
    
    if cond:
        qtd += 1
        lista.append(numero)
    
    cond = False


print(qtd)
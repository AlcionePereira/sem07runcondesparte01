peso = float(input().strip())
tamanho = float(input().strip())
IMC = peso / (tamanho ** 2)


print('{:.2f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do peso')
    
elif 18.5 <= IMC < 25:
    print( 'Peso normal')
        
elif 25 <= IMC < 30:
    print('Sobrepeso')
        
elif 30 <= IMC < 35:
    print( 'Obeso leve')
        
elif 35 <= IMC < 40:
    print('Obeso moderado')
    
else:
    print('Obeso mórbido')
    



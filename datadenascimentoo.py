dia_atual = int(input().strip())
mês_atual = int(input().strip())
ano_atual = int(input().strip())
dia = int(input())
mes = int(input())
ano = int(input())


if dia_atual == dia and mês_atual == mes:
    print('{}'.format(ano_atual - ano))
    
elif dia > dia_atual and mês_atual == mes:
    print('{}'.format(ano_atual - (ano)-1))
    
    
elif mês_atual < mes:
    print('{}'.format(ano_atual - (ano)-1))
    
else:
    print('{}'.format(ano_atual - ano))
    

    
    

def maior(n,nu,num,nume,numer):
    if a > b  and a > c and a > d and a > e:
        return '{}' .format(a)
    elif b > a and b > c and b > d and b > e:
        return'{} ' .format(b)
    elif c > a and c > b and c > d and c > e:
        return '{}  ' .format(c)
    elif d > a and d > b and d > c and d > e:
        return '{}' .format(d)
    else:
        return '{}' .format(e)
    
        
def  menor(n,nu,num,nume,numer):
    if a < b  and a < c and a < d and a < e:
        return '{}' .format(a)
    elif b < a and b < c and b < d and b < e:
        return'{} ' .format(b)
    elif c < a and c < b and c < d and c < e:
        return '{}  ' .format(c)
    elif d < a and d < b and d < c and d < e:
        return '{}' .format(d)
    else:
        return '{}' .format(e)   
    

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())
e = int(input().strip())

        

print(maior(a,b,c,d,e))
print(menor(a,b,c,d,e))
      


    
        
    

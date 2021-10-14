n1 = float(input().strip())
n2 = float(input().strip())
n3 = float(input().strip())
n4 = float(input().strip())
n5 = float(input().strip())

media = (n1 + n2 + n3 + n4 +n5) // 5

print(f'{media:.2f}')
if n1 > media:
    print('{:.2f}'.format(n1))
    if n2 > media:
        print('{:.2f}'.format(n2))
        if n3 >media:
            print('{:.2f}'.format(n3))
            if n4 >media:
                print('{:.2f}'.format(n4))
                if n5 > media:
                    print('{:.2f}'.format(n5))
                    
                    
                
                

   

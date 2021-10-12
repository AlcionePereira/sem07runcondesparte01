def datas(x,y,z,a,b,c):
    if pri_data > seg_data:
        return'{}/{}/{}'.format(d1,m1,an1)
    else:
        return '{}/{}/{}'.format(d2,m2,an2)


d1 = int(input().strip())
m1 = int(input().strip())
an1 = int(input().strip())
d2 = int(input().strip())
m2 = int(input().strip())
an2 = int(input().strip())

pri_data = (d1,m1,an1)
seg_data = (d2,m2,an2)



print(datas(d1,m1,an1,d2,m2,an2))




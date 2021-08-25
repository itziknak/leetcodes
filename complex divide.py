def complex_divide ( complex_num) :
    from numpy import zeros
    count=0
    x=zeros(2,dtype=int)
    for i in complex_num:
        if i=="+":
            num1=complex_num[0:count]
            num2=complex_num[count+1:-1]
        else:
            count+=1
    x[0]=int(num1)
    x[1]=int(num2)
    return x

def multif(com1,com2):
    from numpy import zeros
    x=zeros(2,dtype=int)
    x[0]=com1[0]*com2[0]-com1[1]*com2[1]
    x[1]=com1[0]*com2[1]+com2[0]*com1[1]
    return x
    
print('enter first complex number')
y1=input()
print('ennter second complex number')
y2=input()
x1=complex_divide(y1)
x2=complex_divide(y2)
x1=multif(x1,x2)
y1=str(x1[0])+'+'+str(x1[1])+'i'
print('the multifiction of the two umbers you added is', y1)





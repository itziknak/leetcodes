
def judgeSquareSum(num, c):
    i=0
    while i*i+num*num<=c:
        if i*i+num*num==c:
            return True
        i+=1
    if num*num>c/2:
        return False
    else:
        answer=judgeSquareSum(num+1,c)
    return answer
print('enter the number you wish to check if it a sum of two square intengers')
n=input()
flag=judgeSquareSum(0,n)
print(flag)
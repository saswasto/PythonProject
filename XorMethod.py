def get_missing_summation(a):
    n=a[-1]
    sum1=0
    total = n*(n+1)//2
    sum1=sum(a)
    print(total-sum1)
def get_missing_xor(b):
    n=len(b)
    xor_b=b[0]
    for index in range(1,n):
        xor_b=xor_b^b[index]
    x2=0
    for index in range(1,n+2):
        x2=x2^index
    print(xor_b^x2)
a =[1,2,4,5,6,7]
b = [1, 3,4, 5, 6, 7, 8]
get_missing_summation(a)
get_missing_xor(b)
#here we intro two method one is summation and another is xor method.
#we can also change the value of a = [1, 4, 5, 6, 7, 8]

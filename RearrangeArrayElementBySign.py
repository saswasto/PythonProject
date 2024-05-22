def rearrange_by_sign(A):
    pos=[]
    neg=[]
    for i in range (len(A)):
        if A[i] >0:
            pos.append(A[i])
        else:
            neg.append(A[i])
    for i in range (len(pos)):
        A[2*i] = pos[i]
    for i in range (len(neg)):
        A[2*i+1] = neg[i]
    return A
A=[3,1,-2,-5,2,-4]
ans= rearrange_by_sign(A)
for i in range(len(ans)):
  print(ans[i],end = " ")


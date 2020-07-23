s=""
test_list = [] 
rev=[]
alpha = 'a'
beta='z'
for i in range(0, 26): 
    test_list.append(alpha) 
    alpha = chr(ord(alpha) + 1)
    rev.append(beta)
    beta = chr(ord(beta) - 1)
   

a=input("enter a string to reverse:").lower()
for i in a:
    if i in test_list:
        k=(test_list.index(i))
        s=s+rev[k]
    else:
        s=s+i
print(s)            


n = 1
fact = n*(n-1)
n-=1 
 
while n > 1:
    fact *= (n-1)
    n-=1
print(fact)
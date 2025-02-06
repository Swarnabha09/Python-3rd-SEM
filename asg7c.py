def prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
        
primeList=list(filter(prime, range(1,100))) #filter func.-- filter(function,iterable)
print(primeList)

x=lambda y:(y%400==0) or (y%100!=0 and y%4==0)
leapList=list(filter(x,range(2024,3011)))
print(leapList)

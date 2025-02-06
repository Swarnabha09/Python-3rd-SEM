#total salary
basic=eval(input("Enter basic salary:"))
agp=basic*0.50
mbasic=basic+agp
da=mbasic*0.50
hra=mbasic*0.15
total=mbasic+da+hra
print(f"Total salary={total:0.2f}")

#Quadratic equation
a=eval(input("enter the coefficient of x^2:"))
b=eval(input("enter the coefficient of x:"))
c=eval(input("enter the constant:"))
if a==0:
    print("This is not a quadratic equation:")
else:
    d=b**2-4*a*c
    if d==0:
        print("The roots are real numbers and equal")
        r1=r2=(-b)/(2*a)
        print(f"roots are:{r1:0.3f} and {r2:0.3f}")
    elif d>0:
        print("The roots are real numbers but not equal")
        r1=((-b)+d**0.5)/(2*a)
        r2=((-b)-d**0.5)/(2*a)
        print(f"roots are:{r1:0.3f} and {r2:0.3f}")
    else:
        print("The roots are not real numbers")
        r1=((-b)+d**0.5)/(2*a)
        r2=((-b)-d**0.5)/(2*a)
        print(f"roots are:{r1:0.3f} and {r2:0.3f}")

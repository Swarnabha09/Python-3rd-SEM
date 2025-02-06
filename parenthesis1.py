class myException(Exception):
    pass
def wellBracketed(st):
    stack=[]
    try:
        if type(st)!=str:
            raise myException
        for i in st:
            if i=='(':
                stack.append(i)
            if i==')':
                stack.pop()
    except myException as e1:
        print("not a string")
        check=False
    except IndexError as e2:
        print("stack is empty")
        check=False
    else:
        if len(stack)==0:
            check=True
        else:
            check=False
    finally:
        print("done")
        return check

s=input()
print(wellBracketed(s))

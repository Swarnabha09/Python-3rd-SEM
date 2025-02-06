#parenthesis checker
'''
class myException(Exception):
    pass
def pcheck(s):
    b=[]
    try:
        if type(s)!=str:
            raise myException
        for i in s:
            if i=='(':
                b.append(i)
            if i==')':
                b.pop();
    except myException as e1:
        print("Input expression is not a string")
        check=False
    except IndexError as e2:
        print("the list is empty")
        check=False
    else:
        if len(b)==0:
            check=True
        else:
            check=False
    finally:
        print("Done")
        return check

s=input("enter the string:")
print(pcheck(s))
'''
openl=['(','{','[']
closel=[')','}',']']
def wellBracketed(str):
    try:
        stack=[]
        for i in str:
            if i in openl:
                stack.append(i)
            if i in closel:
                index=closel.index(i)
                if len(stack)>0 and openl[index]==stack[-1]: #checking if the last element of the stack is equal
                    stack.pop()
                else:
                    return False
        return len(stack)==0
    except Exception as e:
        print(f"an error occured {e}")
        return False
    finally:
        print("done")
string=input("enter:")
print(wellBracketed(string))





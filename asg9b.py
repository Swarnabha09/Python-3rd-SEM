#rotation of list
class rotateException(Exception):
    pass
"""
    Rotates a list either left or right based on the number of rotations.

    Parameters:
        lst (list): The list to be rotated.
        rotations (int): The number of rotations. Negative for left, positive for right.
    
    Returns:
        list: The rotated list.
    
    Raises:
        ValueError: If the list is empty.
        RotationError: If the number of rotations is greater than or equal to the length of the list.
"""
def rotateList(lst,rotation=0):
    try:
        n=len(lst)
        if abs(rotation)>n:
            raise rotateException
        if rotation<0:
            rotation+=n
        return lst[-rotation:]+lst[:-rotation]
    except rotateException as e1:
        print("no. of rotation is more than no. of elements in the list")
        return lst
    except IndexError as e2:
        print("list is empty")
    finally:
        print("done")

s=input("enter:")
l1=list(s.split())
r=int(input("enter rotation:"))
x=rotateList(l1,r)
print(x)

#use of match
ch=input("enter character:")
match(ch):
    case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print("vowel")
    case _ if len(ch)==1 and ch.isalpha():
        print("consonant")
    case _:
        print("invalid input")
    

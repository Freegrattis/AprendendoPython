def numerosDivisiveisFor():
    for i in range(121):
        if i%6==0:print(i)

def numerosDivisiveisWhile():
    num=0
    while num<=120:
        if num%6==0:print(num)
        num+=1

if __name__=="__main__":
    print("FOR")
    numerosDivisiveisFor()
    print("\nWHILE")
    numerosDivisiveisWhile()



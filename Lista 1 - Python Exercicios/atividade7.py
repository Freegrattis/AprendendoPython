def somaRangeFor():
    total=0
    for i in range(100,201,1):
        total= total+i
    print(total)

def somaRangeWhile():
    num=100
    total=0
    while num<201:
        total=total+num
        num+=1
    print(total)

if __name__=="__main__":
    print("FOR")
    somaRangeFor()
    print("\nWHILE")
    somaRangeWhile()
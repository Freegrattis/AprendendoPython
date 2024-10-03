def somaFor():
    total=0
    for num in range(101):
        total=total+num
    print(total)

def somaWhile():
    total=0
    contador=0
    while contador<=100:
        total=total+contador
        contador+=1
    
    print(total)

if __name__=="__main__":
    print("FOR")
    somaFor()
    print("\nWHILE")
    somaWhile()

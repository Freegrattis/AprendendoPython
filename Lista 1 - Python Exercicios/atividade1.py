
def paresFor():
    for i in range(16,25,2):
        print(i)

def paresWhile():
    numero=26
    while(numero>15):
        numero+=-2
        print(numero)

if __name__=="__main__":
    print("WHILE\n")
    paresWhile()
    print("\nFOR\n")
    paresFor()
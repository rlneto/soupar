def soupar(number : int) -> None:
    if int(number) & 0b1:
        print("O número é ímpar!")
    else:
        print("O número é par!")
    
        
soupar(int(input("Digite o número: ")))

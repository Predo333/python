peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura em metros: "))
imc=(peso/altura**2)

if imc <0:
    print("Insira um valor válido")
    
    #errado#
else:
    if imc <=18.5: 
        print("Abaixo do peso")
    elif imc <=18.5 and imc <24.9:
        print("Peso Normal")
    elif imc <=25.0 and imc <29.9:
        print("Sobrepeso")
    else:
        print("kawa gay")

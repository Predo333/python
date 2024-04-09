peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
imc=(peso/altura**2)

if imc <=18.5:
    print("Abaixo do peso")
    
    #errado#
elif imc >18.5 and <=24.9: 
    print("Peso normal")





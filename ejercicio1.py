masa = float(input("Ingresa tu masa en KG:"))
altura = float(input("Ingresa tu altura en Metros:"))


imc=masa/altura**2


print("Tu IMC es: "+str(imc))


if imc >= 25:
    print("Tienes SOBREPESO")
if imc <= 19:
    print("Tienes bajo peso")
def calcular_imc(peso, altura) :
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc) :
    if imc < 18.5:
        return "Abaixo peso"
    elif 18.9 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"
    
peso = 60.2
altura = 1.60

imc = calcular_imc(peso, altura)
categoria = classificar_imc(imc)

print(f"seu imc é {imc: .2f}")
print(f"Classificação: {categoria}")
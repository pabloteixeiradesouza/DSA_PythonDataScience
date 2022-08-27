## ******************* PYTHON CALCULATOR *******************

print("Selecione o número da opçãp desejada:\n\n"
      "1 - Soma\n"
      "2 - Subtração\n"
      "3 - Multiplicação\n"
      "4 - Divisão")
opcao = int(input("Digite sua opção (1/2/3/4): "))

resultado = 0.0
sinal = ""

if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):
    print("Opção inválida")
else:
    primeironumero = float(input("Digite o primeiro número: "))
    segundonumero = float(input("Digite o seguindo número: "))
    
    if opcao == 1: 
        resultado = primeironumero + segundonumero
        sinal = "+"
    elif opcao == 2:
        resultado = primeironumero - segundonumero
        sinal = "-"
    elif opcao == 3: 
        resultado = primeironumero * segundonumero
        sinal = "*"
    elif opcao == 4: 
        resultado = primeironumero / segundonumero  
        sinal = "/"
print(primeironumero, sinal, segundonumero, "=", resultado)
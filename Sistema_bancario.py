menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor do depósito: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            
        else:
           print("Valor inválido. Tente novamente.")
        




    elif opcao == "2":
       valor = float(input("Informe o valor de saque: R$"))
       saldo_ultrapassado = valor > saldo
       limite_ultrapassado = valor > limite
       saque_excedido = numero_saques >= LIMITE_SAQUES
       if saldo_ultrapassado:
          	print("Saldo insuficiente. tente novamente.")
       elif limite_ultrapassado:
            print("Falha na operação. valor de saque superior ao limite, tente novamente.") 
       elif saque_excedido:
            print("Limite de saques diários excedidos.")  	

       elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
       else:  
         print ("O Valor informado é inválido.")
     
      
        

    elif opcao == "3": 
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

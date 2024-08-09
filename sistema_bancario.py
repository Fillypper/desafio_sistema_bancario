"""
Falhas no projeto, pode sacar mesmo com saldo zerado.
Após entrar em depositar ou sacar e digitar uma letra, o programa da erro.

"""

menu = """
# 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""

saldo, cont = 0, 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
 
    if opcao == 'd':
        valor = int(input("Qual valor deseja depositar?: "))
        saldo += valor
        print(f"Seu saldo total na conta é de R$ {saldo:.2f}")
        extrato += f"Deposito de R$ {saldo:.2f}\n"

    elif opcao == 's':
        saque = int(input("Qual valor você deseja saca?: "))
        if saque <= limite:
            if cont < LIMITE_SAQUES:
                saldo -= saque
                cont +=1
                print("Saque realizado com sucesso!")
                print(f"Seu saldo agora é de R${saldo:.2f}")
                extrato += f"Saque de R$ {saldo:.2f}\n"
            else:
                print("Você excedeu o limite de 3 saques diários")
        else:
            print("O valor sacado deve ser menor do que R$500.00")


    elif opcao == 'e':
        extratos = "Extrato Bancário"
        print(f"{extratos:=^50}")
        print(f"{extrato:^50}")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print("-"*50)
        print(f"Saldo: {saldo:.2f}")
        
        


    elif opcao == 'q':
        print("Muito obrigado por utilizar nosso sistema!")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a poeração desejada.")

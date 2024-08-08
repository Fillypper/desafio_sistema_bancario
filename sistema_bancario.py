""" operação deposito
    Deve ser possivel depositar valores positivos para minha cota bancaria
    Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato    
    """

""" operação saque
    O sistea deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
    Caso o usuário não tenha saldo, exibir mensagem "não será possivel sacar o dinheiro, saldo insuficiente.
    Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato   
    """

""" operação de extrato
    essa operação deve listar todos os depósitos e saques realizados na conta. no fim da listagem deve ser exibido o saldo atual da conta.
    Os valores devem ser exibidos utilizando o formatado R$ 000.00, Ex: 1500.45 = R$ 1500.45 
    """

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")

    elif opcao == 's':
        print("Depósito")

    elif opcao == 'e':
        print("Depósito")

    elif opcao == 'q':
        print("Depósito")
        
    else:
        print("Operação inválida, por favor selecione novamente a poeração desejada.")
"""
Objetivo Geral

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (client) e cadastrar conta bancária.

Desafio

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

Separação em funções

Devemos criar funções para todas as operações do sistema.

Para exercitar tudo que aparendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

Função Saque

A função daque deve receber os argumentos apenas por nome (keyword only). SUgestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.


FUnção Depósito

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

Função extrato

A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

Novas funções

Precisamos criar duas nova funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

Criar usuário (cliente)

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço (fazer validação). O endereço é uma string com o formato, logradouro, numero - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários no mesmo CPF.

Criar conta corrente

O programa deve armanzenar contas em uma lista, uma conta é composta por: agência, número da ocnta e usuário. O Número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

DICA

Para vincular um usuário a uma conta, filtra a lista de usuários buscando o número do CPF informado para cada usuário na lista.

"""




def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    return

def deposito(saldo, valor, extrato):
    return saldo, extrato

def extrato(saldo, /, extrato):
    return

def criar_usuario(nome, data_nascimento, cpf, endereco):
    #Para vincular um usuário a uma conta, filtra a lista de usuários buscando o número do CPF informado para cada usuário na lista.
    return

def criar_conta_corrente(agencia, numero_conta, usuario):
    #O Número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
    return

def listar_contas():
    return
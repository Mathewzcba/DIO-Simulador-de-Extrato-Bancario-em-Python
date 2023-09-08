import time

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0

def depositar(valor):
    global saldo
    global saque
    saldo += valor
    saque += limite
    extrato.append(f"Depósito: {valor}")
    time.sleep(2)
    print(f'Depósito realizado com sucesso.')

def sacar(valor):
    global saldo
    global numero_saques
    global LIMITE_SAQUES
    global saque
    if numero_saques < LIMITE_SAQUES and valor <= limite:
        if saldo >= valor :
            saldo -= valor
            numero_saques += 1
            LIMITE_SAQUES -= 1
            saque -= valor
            extrato.append(f"Saque: {valor}")
            time.sleep(2)
            print('Saque realizado com sucesso.')
        else:
            print('Você não tem saldo suficiente.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Você já utilizou o limite de saques diários.')
    elif valor > limite:
        print('Saque solicitado é maior que o seu limite atual.')

def mostrar_extrato():
    print('GERANDO EXTRATO...')
    time.sleep(2)
    print(f"Seu saldo unificado é R${saldo}, limite total é R${limite} e você tem disponível {LIMITE_SAQUES} saques diários.")
    print(f'Suas últimas movimentações: {extrato}')

while True:
    print('''SEJA BEM-VINDO AO BANCO DIO
    [0] - DEPÓSITO
    [1] - SAQUE
    [2] - EXTRATO
    [3] - SAIR''')
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 0:
        deposito = int(input('DIGITE O VALOR QUE DESEJA DEPOSITAR, R$: '))
        depositar(deposito)

    elif escolha == 1:
        saque_valor = int(input("DIGITE O VALOR QUE DESEJA SACAR, R$: "))
        sacar(saque_valor)

    elif escolha == 2:
        mostrar_extrato()

    elif escolha == 3:
        print('Obrigado por utilizar o Sistema.')
        break
    else:
        print('Opção inválida, tente novamente.')

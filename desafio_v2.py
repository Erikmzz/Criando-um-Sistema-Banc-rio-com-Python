from datetime import date, datetime, timedelta

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
numero_transacao = 0

datas = []
tipo_transacao = []
valor_transacao = []

LIMITE_SAQUES = 3
LIMITE_TRANSACAO = 10

mascara_ptbr = "%d/%m/%Y %H : %M"

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if numero_transacao >= LIMITE_TRANSACAO:                     #excedeu_saques = numero_saques >= LIMITE_TRANSAÇÃO
            print("Operação falhou! Número máximo de transações excedido.")
            
        elif valor >0:
            saldo += valor
            print("Saque realizado com sucesso.")
            
            data = datetime.now()
            numero_transacao += 1
            
            datas.append(data.strftime(mascara_ptbr))
            tipo_transacao.append("+")
            valor_transacao.append(f'{valor:.2f}')

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:                                              #excedeu_saldo = valor > saldo
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor >limite:                                            #excedeu_limite = valor > limite
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:                           #excedeu_saques = numero_saques >= LIMITE_SAQUES
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif numero_transacao >= LIMITE_TRANSACAO:                     #excedeu_saques = numero_saques >= LIMITE_TRANSAÇÃO
            print("Operação falhou! Número máximo de transações excedido.")

        elif valor > 0:
            saldo -= valor
            print("Saque realizado com sucesso.")

            data = datetime.now()
            numero_saques += 1
            numero_transacao += 1
            
            datas.append(data.strftime(mascara_ptbr))
            tipo_transacao.append("-")
            valor_transacao.append(f'{valor:.2f}')

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        
        if len(datas) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in range(len(datas)):
                print(f"{datas[movimentacao]}       {tipo_transacao[movimentacao]}  R$ {valor_transacao[movimentacao]}\n")

        print("==========================================")
        
    elif opcao == "q":
        print("Obrigado pela sua preferência. Volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

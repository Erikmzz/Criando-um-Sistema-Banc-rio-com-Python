
menu = """

[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Novo cliente
[cb] Nova conta bancaria
[q]  Sair

=> """

saldo = 0
LIMITE = 500

usuarios = []
contas = []

LIMITE_SAQUES = 3
#LIMITE_TRANSACAO = 10

mascara_ptbr = "%d/%m/%Y %H : %M"

def deposito (valor, conta_in, /): 

   contas_filtradas = [conta for conta in contas if conta["numero"] == conta_in]
   
   indices = [i for i, conta in enumerate(contas) if conta["numero"] == conta_in]
   index = indices[0] if indices else -1
   
   if contas_filtradas:
            
        if valor > 0:
            
            contas[index]["saldo"] += valor
            contas[index]["extrato"] += (f"Deposito:\tR$ {valor:.2f}\n")
            
            print("Deposito realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")
   else:
       print("Operação falhou! Conta informada é inválida.")
            
     
def saque (*, valor, conta_in):
       
    contas_filtradas = [conta for conta in contas if conta["numero"] == conta_in]
   
    indices = [i for i, conta in enumerate(contas) if conta["numero"] == conta_in]
    index = indices[0] if indices else -1
    
    if contas_filtradas:

        if valor > contas[index]["saldo"]:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > LIMITE:
            print("Operação falhou! O valor do saque excede o limite.")

        elif contas[index]["numero_saques"] >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            

        elif valor > 0:
            
            contas[index]["saldo"] -= valor
            contas[index]["numero_saques"] += 1
            contas[index]["extrato"] += (f"Saque:\t\tR$ {valor:.2f}\n")
            
            print("Saque realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
       print("Operação falhou! Conta informada é inválida.")

def extrato (conta_in): 
    
   contas_filtradas = [conta for conta in contas if conta["numero"] == conta_in]
   
   indices = [i for i, conta in enumerate(contas) if conta["numero"] == conta_in]
   index = indices[0] if indices else -1
   
   if contas_filtradas:
       
       print("\n================ EXTRATO ================")
       print("Não foram realizadas movimentações." if contas[index]["extrato"] == "" else contas[index]["extrato"])
       saldo_atual = contas[index]["saldo"]
       print(f"\nSaldo:\t\tR$ {saldo_atual:.2f}")
       print("==========================================")

   else:
       print("Operação falhou! Conta informada é inválida.")

def novo_cliente():
    cpf = input("Informe o CPF (somente número): ")
    
    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("=== Usuário criado com sucesso! ===")

    
def nova_conta():
    cpf = input("Informe o CPF (somente número): ")
    
    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    if usuario:
        numero = len(contas)+1
    
        contas.append({"agencia": 1, "numero": numero, "usuario":usuario, "saldo":0, "numero_saques":0, "extrato": ""})
    
        print(f"=== Conta bancaria nº {numero} criada com sucesso! ===")

    else:
        print("Erro! Usuário nao encontrado")
        
        
while True:

    opcao = input(menu)
    
    if opcao =="d":
        conta_in = input("Informe a conta: ")
        valor = input("Informe o valor de deposito: ")
        deposito(int(valor), int(conta_in))              #positional only
        
    elif opcao =="s":
        conta_in = input("Informe a conta: ")
        valor = input("Informe o valor de saque: ")
        saque(valor=int(valor), conta_in=int(conta_in))  #keyword only
        
    elif opcao =="e":
        conta_in = input("Informe a conta: ")
        extrato(int(conta_in))
        
    elif opcao == "nc":
        novo_cliente()
        
    elif opcao =="cb":
        nova_conta()
        
    else:
        print("Obrigado pela sua preferência. Volte sempre!")
        break

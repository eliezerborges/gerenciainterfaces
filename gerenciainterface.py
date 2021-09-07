import interface

if __name__ == "__main__":
    nome_equipamento = input("Nome do Equipamento: ")
    qtd_interfaces = int(input("Quantidade de interfaces: "))
    ctrl_while = 1
    interfaces = []

    while(ctrl_while <= qtd_interfaces):
        nome = input("Digite o NOME da interface "+ str(ctrl_while) +": ")
        ip = input("Digite o IP da interface "+str(ctrl_while)+": ")
        newInterface = interface.Interface(nome, ip)
        interfaces.append(newInterface)
        ctrl_while += 1

    ctrl_while = 1
    print("----- RELATORIO -----")
    print("Equipamento: "+ nome_equipamento)
    for interface in interfaces:
        interface.imprime()    
from operator import itemgetter
placa2 = ""
contador = 0
veiculo = {}
veiculos = []
opcao = 8
filtro = True
print("Bem-vindo ao leitor, o que deseja fazer? ")
while opcao == 8:
    print("-" * 45)
    opcao = int(input(

            "\nListar todos Veiculos[1]"
            "\nCadastrar Veículos[2]"
            "\nListar Veículos por ano de fabricação[3]"
            "\nFiltrar Veículo por Modelo[4]"
            "\nFiltrar a Partir de determinado ano[5]"
            "\nFiltrar Veículo por Nome[6]"
            "\nFinalizar[7]"
            "\nInsira a Opção escolhida:"))
    #Listar Veículos OPCAO 1#
    while opcao == 1:
        print("-"*45)
        print("Os veiculos cadastrados são:")
        if len(veiculos) < 1:
            continuar = str(input("Não há veiculos Cadastrados. Deseja cadastrar?")).upper().strip()
            while continuar not in "NnSsYy":
                continuar = str(input("Opção Incorreta. Deseja cadastrar?? 'Sim' ou 'Não'. "))[0].upper().strip()
            if continuar in "Nn":
                opcao = 8
            elif continuar in "SsYy":
                opcao = 2
                break
        for pos, carro in enumerate(veiculos):
            print(f"{pos+1} Nome: {carro['nome']} - Ano: {carro['fab']} - Marca: {carro['marca']} - Placa: "
                  f"{carro['placay']}-{carro['placax']} - Modelo: {carro['modelo']}")

        continuar = str(input("RETORNAR AO MENU? 'Sim' ou 'Não'. "))[0].upper().strip()
        if continuar in "SsYy":
            opcao = 8
        while continuar not in "NnSsYy":
            continuar = str(input("Opção Incorreta. Deseja continuar? 'Sim' ou 'Não'. "))[0].upper().strip()
        if continuar in "Nn":
            print("Obrigado. Finalizando o programa.")
            break
    #------------------------#
    #Cadastro de Veículos OPCAO 2#
    print("-" * 45)
    while opcao == 2:
        while contador != 10 and opcao == 2:

            nome = str(input("Digite o Nome do Veículo: ")).upper().strip()
            marca = str(input("Digite a Marca do Veículo: ")).upper().strip()
            modelo = str(input("Digite o Modelo do Veículo: ")).upper().strip()
            fab = str(input("Digite o ano de fabricação: ")).upper().strip()

            placaY = str(input("Digite as 3 Primeiras LETRAS(YYY): ")).upper().strip()
            while len(placaY) != 3:
                placaY = str(input("Formato de placa incorreto, digite 3 digitos(YYY): ")).upper().strip()
            placaX = int(input("Digite os 4 ultimos Números(XXXX): "))
            while len(str(placaX)) !=4:
                placaX = int(input("Invalido. Digite os 4 ultimos Números(XXXX): "))


            veiculo["nome"] = nome
            veiculo["fab"] = fab
            veiculo["marca"] = marca
            veiculo["placay"] = placaY
            veiculo["placax"] = placaX
            veiculo["modelo"] = modelo

            placa2 = ""
#CADASTRO EM ORDEM CRESCENTE POR FAB NA LISTA#
            veiculos.append(veiculo.copy())
            #ORDENA A LISTA PARA CRESCENTE
            veiculos = sorted(veiculos, key=itemgetter('fab'))
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
            contador += 1
            if contador == 10:
                print("O Número Máximo de veiculos foi cadastrado")
                opcao = 8
                break
            continuar = str(input("Deseja continuar cadastrando veículos?? 'Sim' ou 'Não'. "))[0].upper().strip()
            print(f"Foram Cadastrados {contador} veiculos. Restam {10-contador} até o limite.")
            while continuar not in "NnSsYy":
                continuar = str(input("Opção Incorreta. Deseja continuar? 'Sim' ou 'Não'. "))[0].upper().strip()
            if continuar in "Nn":
                opcao = 8
            elif continuar in "SsYy":
                opcao = 2

    #LISTAR Veiculos por Ano de fab OPCAO 3#
    while opcao == 3:
        print("-" * 45)
        filtroAno = int(input("Digite o Ano do Veiculo que deseja ver: "))
        print(f"Os Veiculos do ano de {filtroAno} cadastrados são: ")

        for pos, carro in enumerate(veiculos):
            if filtroAno == int(carro['fab']):
                print(f"{pos+1} Nome: {carro['nome']} - Ano: {carro['fab']} - Marca: {carro['marca']} - Placa: "
                  f"{carro['placay']}-{carro['placax']} - Modelo: {carro['modelo']}")
                filtro = False
            elif filtro and pos+1 == len(veiculos):
                print(f"Não há veiculos de {filtroAno} Cadastrados.")
                break
        continuar = str(input("Deseja verificar outro ano? 'Sim' ou 'Não'. "))[0].upper().strip()
        filtro = True
        while continuar not in "NnSsYy":
            continuar = str(input("Opção Incorreta. Deseja continuar? 'Sim' ou 'Não'. "))[0].upper().strip()
        if continuar in "Nn":
            opcao = 8
        else:
            continuar = 3

#--------------------------------------------------------------------------------------------------------------#
# FILTRAR POR MODELO
    while opcao == 4:
        print("-" * 45)
        filtroModelo = str(input("Digite o Modelo dos veiculos que deseja ver: ")).upper().strip()
        print(f"Os Veiculos do modelo {filtroModelo} cadastrados são: ")
        for pos, carro in enumerate(veiculos):
            if filtroModelo == str(carro['modelo']):
                print(f"Nome: {carro['nome']} - Ano: {carro['fab']} - Marca: {carro['marca']} - Placa: "
                  f"{carro['placay']}-{carro['placax']} - Modelo: {carro['modelo']}")
                filtro = False
            elif filtro and pos+1 == len(veiculos):

                print(f"Não há veiculos {filtroModelo} Cadastrados.")
                filtro = True
                break
        continuar = str(input("Deseja Continuar verificando por Modelo? 'Sim' ou 'Não'. "))[0].upper().strip()
        filtro = True
        while continuar not in "NnSsYy":
            continuar = str(input("Opção Incorreta. Deseja continuar? 'Sim' ou 'Não'. "))[0].upper().strip()
        if continuar in "Nn":
            opcao = 8
        else:
            opcao = 4

#---------------------------------------------#
#FILTRAR A PARTIR DE DETERMINADO ANO OPCAO 5#
    while opcao == 5:
        print("-" * 45)
        filtroAno = int(input("Digite o Ano do Veiculo que deseja ver: "))
        print(f"Os Veiculos a partir de {filtroAno} cadastrados são: ")

        for pos, carro in enumerate(veiculos):
            if filtroAno <= int(carro['fab']):
                print(f"Nome: {carro['nome']} - Ano: {carro['fab']} - Marca: {carro['marca']} - Placa: "
                  f"{carro['placay']}-{carro['placax']} - Modelo: {carro['modelo']}")
                filtro = False

            elif filtro and pos+1 == len(veiculos):
                print(f"Não há veiculos a partir de {filtroAno} Cadastrados.")
                filtro = True
                break
        continuar = str(input("Deseja verificar outro ano? 'Sim' ou 'Não'. "))[0].upper().strip()
        filtro = True
        while continuar not in "NnSsYy":
            continuar = str(input("Opção Incorreta. Deseja continuar? 'Sim' ou 'Não'. "))[0].upper().strip()
        if continuar in "Nn":
            opcao = 8
        else:
            opcao = 5

#---------------------------------------------#
#FILTRAR A PARTIR DO NOME#
    while opcao == 6:
        print("-" * 45)
        filtroNome = str(input("Digite o Nome do Veiculo que deseja ver: ")).upper().strip()
        print(f"Os Veiculos nomeados com '{filtroNome}' cadastrados são: ")
        for pos, carro in enumerate(veiculos):
            if carro['nome'] in filtroNome:
                print(f"Nome: {carro['nome']} - Ano: {carro['fab']} - Marca: {carro['marca']} - Placa: "
                  f"{carro['placay']}-{carro['placax']} - Modelo: {carro['modelo']}")
                filtro = False
            elif filtro and pos+1 == len(veiculos):
                print(f"Não há veiculos Cadastrados com o nome '{filtroNome}'.")

                break
        continuar = str(input("Deseja Continuar?? 'Sim' ou 'Não'. "))[0].upper().strip()
        filtro = True
        while continuar not in "NnSsYy":
            continuar = str(input("Opção Incorreta. Deseja continuar? 'Sim' ou 'Não'. "))[0].upper().strip()
        if continuar in "Nn":
            opcao = 8
        else:
            opcao == 6
#---------------------------------------------#
    if opcao == 7:
        print("Muito Obrigado. Finalizando o Sistema.")


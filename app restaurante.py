import time

def opção_invalida():

    input("Opção inválida, pressione o ENTER para voltar")

def activate_restaurant(restaurant):
    print("Ativando restaurante...")
    time.sleep(1)
    print("Restaurante ativado!")
    print("Aqui estão as informações do restaurante:")
    print("Nome:", restaurant['nome'])
    print("endereço:", restaurant['endereço'])
    print("contato:", restaurant['contato'])
    print("Restaurante ativado com sucesso!")
    print("Retornando para o menu...")
    time.sleep(3)

restaurante = []

while True:
    try:
        print("\nseja bem vindo ao restaurantes Barueri")
        print("\n1. Cadastrar restaurante")
        print("2. Listar os restaurantes")
        print("3. Ativar restaurantes")
        print("4. Sair")
        opçãoescolhida = int(input("\nescolha sua opção:"))
        if (opçãoescolhida == 1):
            print("\nseja bem vindo a tela de cadastro!")
            cadastro = input("digite aqui o nome do seu restaurante:")
            endereço = input("digite o endereço do seu restaurante:")
            numero = input("Digite o numero de contato:")
            print ("\nmuito obrigado, cadastro feito com sucesso!")
            print ("\naqui estão os dados:")
            time.sleep(1)
            print ("nome:",cadastro)
            print ("endereço:",endereço)
            print ("numero:",numero)
            print ("\nrestaurante cadastrado com sucesso!")
            print ("\nadicionando restaurante à lista...")
            time.sleep(1)

            
            restaurante.append({
                'nome': cadastro,
                'endereço': endereço,
                'contato': numero
            })

            print ("\nrestaurante adicionado à lista!")
            print ("\nretornando a pagina inicial...")
            time.sleep(3)
            continue
        elif (opçãoescolhida == 2):
            print("olá, vamos listar alguns restaurantes para você:")
            if not restaurante:
                print("Não há restaurantes cadastrados.")
            else:
                for i, restaurant in enumerate(restaurante, start=1):
                    print(f"\n   nome: {restaurant['nome']}")
                    print(f"   Endereço: {restaurant['endereço']}")
                    print(f"   Contato: {restaurant['contato']}")
            time.sleep(5)
            continue
        elif (opçãoescolhida == 3):
            if not restaurante:
                print("Não há restaurantes cadastrados.")
            else:
                for i, restaurant in enumerate(restaurante, start=1):
                    print(f"\n{i}   nome: {restaurant['nome']}")
                    print(f"   Endereço: {restaurant['endereço']}")
                    print(f"   Contato: {restaurant['contato']}")
                print("selecione o restaurante para ativar:")
                maxvalue = int(input("Digite o número do restaurante: "))
                activate_restaurant(restaurante[maxvalue - 1])
            time.sleep(5)
            continue
        elif (opçãoescolhida == 4):
            print("Saindo...")
            time.sleep(1)
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
    except:
        opção_invalida()     
        continue
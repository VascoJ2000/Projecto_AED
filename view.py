import model
import controller

print("\n Seja Bem-vindo ao teatro. \n")
print(f"As datas dos espetáculos são: {model.Datas}\n")
print("\n Escolha um lugar vago. \n")

print(model.numero_lugaresK)  # Imprime o número de lugares disponíveis para o espetáculo K
print(model.numero_lugaresJ)
print(model.numero_lugaresI)
print(model.numero_lugaresH)
print(model.numero_lugaresG)
print(model.numero_lugaresF)
print(model.numero_lugaresE)
print(model.numero_lugaresD)
print(model.numero_lugaresC)
print(model.numero_lugaresB)
print(model.numero_lugaresA)
print(model.Palco)

print("\nInsira os comandos RL(para reservar lugar), ER(para eliminar reserva), AR(alterar reserva) e CVB(para consultar o valor da bilheteira).\n")
def main ():  # Função principal
    while True:
        try:
            comandos = input().split(" ")
        except EOFError:
            return
    
        
        if comandos [0] == "RL": #RL -> reservar lugar na sala   
            letra = input("Digite a letra da fila desejada: ")
            numero = input("Digite o numero do lugar desejado: ")
            data = input("Insira a data do espetáculo desejada(dd/mm/aaaa): ")

            while controller.valido_letra(letra) == False:                                          # Verifica se a letra é válida
                print("Letra da fila inválida.")                                                    # Se não for, imprime mensagem de erro
                letra = input("Digite a letra da fila desejada novamente: ")

            while controller.valido_numero(letra, numero) == False:                                 # Verifica se o numero é válido
                print("Número do lugar inválido.")
                numero = input("Digite o número do lugar desejado novamente: ")
            
            while controller.Validar_data(data) == False:                                            # Verifica se a data é válida
                print("Data inválida.")
                data = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")
            
            if controller.verificar_lugares_reservados(letra, numero, data) == True:                    # Verifica se o lugar está reservado
                controller.reservar_lugares(letra, numero, data)                                        # Reserva o lugar
                print("\nLugar registado com sucesso.\n")
            else:
                print("\nLugar já se encontra reservado, insira o comando (RL) para reservar lugar novamente.\n")
                
                

        if comandos[0] == "ER": #ER -> Eliminar reserva
            print("\n Escolha um lugar ocupado. \n")
            letra = input("Digite a letra da fila desejada: ")
            numero = input("Digite o numero do lugar desejado: ")
            data = input("Insira a data do espetáculo desejada(dd/mm/aaaa): ")

            while controller.valido_letra(letra) == False:                                            # Verifica se a letra é válida
                print("Letra da fila inválida.")
                letra = input("Digite a letra da fila desejada novamente: ")

            while controller.valido_numero(letra, numero) == False:                                   # Verifica se o numero é válido
                print("Número do lugar inválido.")
                numero = input("Digite o número do lugar desejado novamente: ")

            while controller.Validar_data(data) == False:                                             # Verifica se a data é válida
                print("Data inválida.")                                                               # Verifica se a data é válida
                data = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")
            
                                                    
            if controller.verificar_lugares_reservados(letra, numero, data) == False:                 # Verifica se o lugar está reservado
                controller.eliminar_lugar_reservado(letra, numero, data)                              # Elimina o lugar
                print("\nLugar eliminado com sucesso.\n")                                             # Imprime mensagem de sucesso
            else:
                print("\nLugar não se encontra reservado.\n")                                         # Imprime mensagem de erro
                print("Insira o comando (RL) para reservar um lugar.")                                # Imprime mensagem de erro


        if comandos[0] == "AR": #AR -> Alterar reserva
            print("\n Escolha um lugar a alterar. \n")
            letra = input("Digite a letra da fila que pretende alterar: ")
            numero = input("Digite o numero do lugar que pretende alterar: ")
            data = input("Insira a data do espetáculo que pretende alterar(dd/mm/aaaa): ")

            while controller.valido_letra(letra) == False:  # Verifica se a letra é válida
                print("Letra da fila inválida.")
                letra = input("Digite a letra da fila desejada novamente: ")

            while controller.valido_numero(letra, numero) == False:                                    # Verifica se o numero é válido
                print("Número do lugar inválido.")                                                     # Verifica se a data é válida
                numero = input("Digite o número do lugar desejado novamente: ")

            while controller.Validar_data(data) == False:                                              # Verifica se a data é válida
                print("Data inválida.")                                                                # Se não for, pede a data novamente
                data = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")

            if controller.verificar_lugares_reservados(letra, numero, data) == False:                  # Verifica se o lugar está reservado
                controller.eliminar_lugar_reservado(letra, numero, data)                               # Elimina o lugar
                print("\nLugar eliminado com sucesso.\n")                                               # Elimina o lugar
            else:
                print("\nLugar não se encontra reservado.\n")


            print("\n Escolha o seu novo lugar. \n")

            letrab = input("Digite a letra da fila desejada: ")
            numerob = input("Digite o numero do lugar desejado: ")
            datab = input("Insira a data do espetáculo desejada(dd/mm/aaaa): ")

            while controller.valido_letra(letrab) == False:                                            # Verifica se a letra é válida
                print("Letra da fila inválida.")                                                       # Se não for, pede para inserir novamente
                letrab = input("Digite a letra da fila desejada novamente: ")                          # Se for, continua a execução

            while controller.valido_numero(letrab, numerob) == False:                                  # Verifica se o numero é válido
                print("Número do lugar inválido.")                                                     # Verifica se o numero é válido
                numerob = input("Digite o número do lugar desejado novamente: ")

            while controller.Validar_data(datab) == False:                                             # Verifica se a data é válida
                print("Data inválida.")                                                                # Verifica se a data é válida
                datab = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")
                                                    
            if controller.verificar_lugares_reservados(letrab, numerob, datab) == True:                # Verifica se o lugar está reservado
                controller.reservar_lugares(letrab, numerob, datab)                                    # Reserva o lugar
                print("\nLugar alterado com sucesso.\n")                                               # Imprime mensagem de sucesso
            else:                                                                                      # Caso contrário
                print("\nLugar já se encontra reservado, insira o comando (RL) para reservar lugar novamente.\n")



        if comandos[0] == "CVB": #CVB -> Consultar valor da bilheteira
            print(f"As datas dos espetáculos são: {model.Datas}\n")                                  # Mostra as datas dos espetáculos
            dado = input("Digite o que quer consultar o valor(dia, mes , ano): ")                    # Pede o que quer consultar
            if dado == "dia":                                                                        # Se for dia
                data = input(f"Que dia pretende consultar{model.Datas}?: ")                          # Pede a data
                controller.contar_valor(data)                                                        # Conta o valor
            elif dado == "mes":                                                                      # Se for mes
                data = input(f"Que mes pretende consultar(07/22, 08/22, 09/22, 01/23, 02/23)?: ")       # Pede o mês
                controller.contar_valor(data)                                                        # Conta o valor
            elif dado == "ano":                                                                      # Se for ano
                data = input(f"Que ano pretende consultar(2022, 2023)?: ")                           # Pede o ano
                controller.contar_valor(data)                                                        # Conta o valor

               
            
            
                
         
import sys

import model
import controller

def main ():
    sala = model.sala
    lugares_sala = model.lugares_sala
    valor_bilheteira = model.Valor_bilheteira
    print("Bem vindo ao teatro")
    print("A sala tem {} lugares".format(sala))
    print("Os lugares disponiveis sao:")
    for lugares in lugares_sala:
        print(lugares)
    print("O valor do bilheteira e de {}".format(valor_bilheteira))
    print("Para reservar lugares digite 'RL'")
    print("Para eliminar reserva digite 'ER'")
    print("Para alterar reserva digite 'AR'")
    print("Para sair digite 'sair'")





    while True:
        try:
            comandos = input().split(" ")   #separa os comandos em uma lista
        except EOFError:
            return
    
    
        if comandos [0] == "RL": #RL -> reservar lugar na sala
            print(model.numero_lugaresK)
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
            print("\n Escolha um lugar vago \n")
            input("Digite a letra da fila desejada: ")
            if controller.valido_letra(comandos) == True:                      #verifica se a letra digitada é válida
                input("Digite o numero do lugar desejado : ")

        if comandos[0] == "ER": #ER -> Eliminar reserva  de lugar na sala
            print("\n Escolha um lugar ocupado \n")
            input("Digite a letra da fila desejada: ")                                         #letra da fila
            if controller.valido_letra(comandos) == True:                                    #valido_letra
                input("Digite o numero do lugar desejado : ")                                #numero do lugar
                if controller.valido_numero(comandos) == True:                             #valido_numero
                    print("\n Reserva eliminada \n")                                #reserva eliminada
                else:                                                        #reserva eliminada
                    print("\n Valor invalido \n")






        if comandos[0] == "AR": #AR -> Alterar reserva
            print("\n Escolha um lugar ocupado \n")
            input("Digite a letra da fila desejada: ")                                         #letra da fila
            if controller.valido_letra(comandos) == True:                                    #valido_letra
                input("Digite o numero do lugar desejado : ")                                #numero do lugar
                if controller.valido_numero(comandos) == True:                             #valido_numero
                    print("\n Reserva alterada \n")                                #reserva alterada
                else:                                                        #reserva alterada
                    print("\n Valor invalido \n")




        if comandos[0] == "CVB": #CVB -> Consultar valor da bilheteira
            print("\n Valor da bilheteira: {} \n".format(valor_bilheteira))


        if comandos[0] == "sair": #sair -> sair do programa
            print("\n Obrigado por usar o programa \n")
            sys.exit()

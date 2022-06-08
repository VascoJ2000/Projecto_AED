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
            comandos = input().split(" ")
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
            if controller.valido_letra(comandos) == True:
                input("Digite o numero do lugar desejado : ")

        if comandos[0] == "ER": #ER -> Eliminar reserva
           print()


        if comandos[0] == "AR": #AR -> Alterar reserva
          print()


        if comandos[0] == "CVB": #CVB -> Consultar valor da bilheteira
            print(*valor_bilheteira , sep = ' , ')

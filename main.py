from Player import Player
from Round import Round

hands = {
    1: "PEDRA",
    2: "PAPEL",
    3: "TESOURA"
}

menu = 's'
while menu in 'Ss':
    rounds = {}

    print(f"{' PEDRA | PAPEL | TESOURA ':=^50}")
    name = input("Insira o seu nome: ")
    print('')

    player_one = Player(name.capitalize())
    player_two = Player('Maquina', True)

    print(f"{' ' + player_one.name + ' ':=^20}{' VS ':=^10}{' ' + player_two.name + ' ':=^20}")
    for i in range(1, 4):
        # Escolha da mão:
        print(f"{' Round ' + str(i) + ' ':-^50}")
        while True:
            print(f"{'PEDRA | PAPEL | TESOURA':^50}")
            hand = input("Escolha uma mão: ")

            if hand.lower() == 'pedra':
                player_one.add_hand(1)
                break
            elif hand.lower() == 'papel':
                player_one.add_hand(2)
                break
            elif hand.lower() == 'tesoura':
                player_one.add_hand(3)
                break
            else:
                print("Essa mão não existe no jogo! Tente novamente.")

        # Início do round:
        rounds[i] = Round(player_one, player_two, i)
        rounds[i].start()

        print(f"{' FIGHT ':-^50}")
        print(f"{hands[player_one.get_hand_by_round(i)]:^20}{'VS':^10}{hands[player_two.get_hand_by_round(i)]:^20}")
        print(f"{'':=<50}")
        if rounds[i].get_winner().name.lower() == 'empate':
            print(f"{'Empate':^50}\n")
        else:
            print(f"{rounds[i].get_winner().name + ' venceu!':^50}\n")

    print(f"{' PLACAR FINAL ':=^50}")
    print(f"{player_one.name + ':':<15} {player_one.get_score()} pontos")
    print(f"{player_two.name + ':':<15} {player_two.get_score()} pontos")
    print(f"{'':-^50}")
    # Imprime o vencedor:
    if player_one.get_score() > player_two.get_score():
        print(f"{player_one.name + ' venceu a partida!':^50}")
    elif player_two.get_score() > player_one.get_score():
        print(f"{player_two.name + ' venceu a partida!':^50}")
    else:
        print(f"{'PARTIDA EMPATADA!':^50}")
    print(f"{'':=^50}")

    opcao = '9'
    while opcao not in 'SsNn':
        opcao = input("Deseja jogar novamente? (S/n): ")
        if opcao not in 'SsNn':
            print("Erro! Digite uma opção válida.")
        else:
            menu = opcao

print("JOGO ENCERRADO!")

from Game import Game

print(f"{' PEDRA | PAPEL | TESOURA ':=^40}")

p1 = input("Insira o primero jogador: ")
p2 = input("Insira o segundo jogador: ")
print('')


game = Game(p1, p2)
game.start()

print(f"{' ' + p1 + ' ':=^15}{' VS ':=^10}{' ' + p2 + ' ':=^15}")
for num, r in game.get_rounds().items():
    print(f"{' Round ' + str(num) + ' ':-^40}")
    print(f"{r.hands[r.hand_p1]:^15}{'VS':^10}{r.hands[r.hand_p2]:^15}")
    print(f"{'':=<40}")

    if r.hand_p1 != r.hand_p2:
        print(f"Mão vencedora: {r.hands[r.hand_p1]}")
        print(f"Jogador: {r.get_winner().name}\n")
    else:
        print("EMPATE! Não houve vencedor.")
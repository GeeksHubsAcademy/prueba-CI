from random import randint

options = ["Piedra", "Papel", "Tijeras"]

def quienGana(player, ai):
    return ""
        
def Game():
    player = input("¿Piedra, Papel o Tijeras?")
    print("Elegiste: " + player)

    ai = options[randint(0,2)]
    print("AI eligio: " + ai)

    winner = quienGana(player, ai)

    print("Por lo tanto, haz: "  + winner )


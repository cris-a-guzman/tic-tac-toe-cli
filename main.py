from logic.logica import  validar_coordenadas,validar_ganador,verificar_empate, usr_pedir_input, colocar_ficha, verificar_empate
from interface.tablero import mostrar_tablero

def jugar():
    matriz = [[" ", " ", " "],
            [" "," "," "],
            [" "," "," "]]
    simbolo_jugador1 = "X"
    simbolo_jugador2 = "O"
    while True:
        while True:
            print(mostrar_tablero(matriz))
            print("Jugador 1")
            f,c = usr_pedir_input()
            if validar_coordenadas(f,c,matriz):
                colocar_ficha(f,c,matriz,simbolo_jugador1)
                print(mostrar_tablero(matriz))
                resultado= validar_ganador(matriz, simbolo_jugador1)
                break
                
            else:
                print("La casilla ya esta usada.")
        if resultado:
            print(f"GANOOO {simbolo_jugador1}")
            break
        if verificar_empate(matriz):
            print("EMPATE")
            break
        while True:
            print("Jugador 2")
            f,c = usr_pedir_input()
            if validar_coordenadas(f,c,matriz):
                colocar_ficha(f,c,matriz,simbolo_jugador2)
                print(mostrar_tablero(matriz))
                resultado = validar_ganador(matriz, simbolo_jugador2)
                break
                
            else:
                print("La casilla ya esta usada.")
        if resultado:
            print(f"GANOOO {simbolo_jugador2}")
            break
        
        if verificar_empate(matriz):
            print("EMPATE")
            break
            
            
if __name__ == "__main__":
    jugar()
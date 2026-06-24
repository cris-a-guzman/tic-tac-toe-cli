from interface.colores import *

matriz_logica = [[" ", " ", " "],
            [" "," "," "],
            [" "," "," "]]

def crear_simbolo(simbolo):
    if simbolo == "X":
        return ["*   *", " * * ", "  *  ", " * * ","*   *"]
    elif simbolo == "O":
        return ["  *  ", " * * ", "*   *", " * * ", "  *  "]
    elif simbolo == " ":
        return ["     ", "     ", "     ", "     ","     "]

    
def mostrar_tablero(tablero):
    matriz_tablero = [[["   ", "   ", "   ","    ","     "] for _ in range(3)] for _ in range(3)]
    texto = "    "
    for i, fila in enumerate(tablero):
        for indice, celda in enumerate(fila):
            if celda == "X":
                matriz_tablero[i][indice] = crear_simbolo("X")
            elif celda == "O":
                matriz_tablero[i][indice] = crear_simbolo("O")
            elif celda == " ":
                matriz_tablero[i][indice] = crear_simbolo(" ")
    
    for i in range(3):
        
        texto += f"{CIAN} COl {i}{RESET}"
    
    texto += "\n    ┌" + "─────┬" * 2 + "─────┐\n"
    for i, fila in enumerate(matriz_tablero):
        for linea in range(5):
            # Aca hay que imprimir la linea visual
            texto += "    │"
            for celda in fila:
                # aca se toma la linea correspondiente
                texto += f"{celda[linea]}"
                texto += "│"
            if linea == 2:
                texto += f" FILA {i}"
            texto += "\n"
        if i != 2:
                texto += "    ├" + "─────┼" * 2 + "─────┤\n"
        else:
            texto += "    └" + "─────┴" * 2 + "─────┘\n"
    return texto
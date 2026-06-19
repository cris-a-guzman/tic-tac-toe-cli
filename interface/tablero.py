
matriz = [[" ", " ", " "],
            [" "," "," "],
            [" "," "," "]]
def dibujar_tablero(tablero):
    numeros = ["COL 0","COL 1","COL 2"]
    texto = "\n"
    for i in range(3):
        texto += "" + numeros[i] + " "
    texto += '\n'

    for i, algo in enumerate(tablero):        
        for indice, celda in enumerate(algo):
            texto += "  " + celda + "  "

            if indice != 2:
                texto += "|"
            else: 
                texto += " FILA " + str(i)
        texto += "\n"
        if i != 2:
            for j in range(16):
                if j == 0:
                    texto += " "

                else:
                    if j == 5 or j == 11:
                        texto += "+"

                    else:
                        texto +="-"
        texto += "\n"
    return texto
 


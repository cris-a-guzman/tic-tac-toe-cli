matriz = [[" ", " ", " "],
            [" "," "," "],
            [" "," "," "]]

def validar_ganador(matriz, simbolo):
    combinaciones = [[(0,0),(0,1),(0,2)],
             [(1,0),(1,1),(1,2)],
             [(2,0),(2,1),(2,2)],
             [(0,0),(1,0),(2,0)],
             [(0,1),(1,1),(2,1)],
             [(0,2),(1,2),(2,2)],
             [(0,0), (1,1), (2,2)],
             [(0,2), (1,1), (2,0)]]
    for combinacion in combinaciones:
        verificador = 0
        for coordenada in combinacion:
            if matriz[coordenada[0]][coordenada[1]] == simbolo:
                verificador += 1
        if verificador == 3:
            return True
    
    return False

def usr_pedir_input():
    while True:
        try:
            
            usr_f = int(input("Ingresa la fila: "))
            usr_c = int(input("Ingresa la columna"))
        except ValueError:
            print("Ingresa numeros.")
            continue
        if 0 <= usr_f <= 2 and 0 <= usr_c <= 2:
            return usr_f, usr_c
        else:
            print("Lo ingresado no es una cordenada valida, intentelo de nuevo.")

def colocar_ficha(f,c,matriz, simbolo):
        matriz[f][c] = simbolo
        
def validar_coordenadas(f,c,matriz):
    if matriz[f][c] == " ":
        return True
    else:
        return False

def verificar_empate(matriz):
    for fila in matriz:
        for columna in fila:
            if columna == " ":
                return False
    return True
        

def jugar():
    while True:
        while True:
            simbolo = "X"
            print("Jugador 1")
            f,c = usr_pedir_input()
            if validar_coordenadas(f,c,matriz):
                colocar_ficha(f,c,matriz,simbolo)
                # imprimir(matriz)
                resultado= validar_ganador(matriz, simbolo)
                break
                
            else:
                print("La casilla ya esta usada.")
                continue # Esto salta el bucle, cierto?
        if resultado:
            print(f"GANOOO {simbolo}")
            break
        if verificar_empate(matriz):
            print("EMPATE")
            break
        while True:
            simbolo = "0"
            print("Jugador 2")
            f,c = usr_pedir_input()
            if validar_coordenadas(f,c,matriz):
                colocar_ficha(f,c,matriz,simbolo)
                # imprimir(matriz)
                resultado = validar_ganador(matriz, simbolo)
                break
                
            else:
                print("La casilla ya esta usada.")
                continue # Esto salta el bucle, cierto?
        if resultado:
            print(f"GANOOO {simbolo}")
            break
        
        if verificar_empate(matriz):
            print("EMPATE")
            break
            
        


ESTADO_FINAL ="ESTADO FINAL"
ESTADO_NO_FINAL ="ESTADO NO FINAL"
ESTADO_TRAMPA = "ESTADO TRAMPA"
""" TOKENS_ACEPTADOS = [("PARA",automata_para),("DESDE",automata_para)] """
def automata_para(n):
    estado_actual = 0 
    estados_finales =[4]
    for i in n:
        if estado_actual == 0 and i == "p":
            estado_actual = 1
        elif estado_actual == 0 and i != "p":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "a":
            estado_actual = 2
        elif estado_actual == 1 and i != "a":
            estado_actual = -1
            break
        elif estado_actual == 2 and i == "r":
            estado_actual = 3
        elif estado_actual == 2 and i != "r":
            estado_actual = -1
            break
        elif estado_actual == 3 and i == "a":
            estado_actual = 4
        elif estado_actual == 3 and i != "a":
            estado_actual = -1
            break
        elif estado_actual == 4:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def automata_desde(n):
    estado_actual = 0
    estados_finales = [5]
    for i in n:
        if estado_actual == 0 and i == "d":
            estado_actual = 1
        elif estado_actual == 0 and i != "d":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "e":
            estado_actual = 2
        elif estado_actual == 1 and i != "e":
            estado_actual = -1
            break
        elif estado_actual == 2 and i == "s":
            estado_actual = 3
        elif estado_actual == 2 and i != "s":
            estado_actual = -1
            break
        elif estado_actual == 3 and i == "d":
            estado_actual = 4
        elif estado_actual == 3 and i != "d":
            estado_actual = -1
            break
        elif estado_actual == 4 and i == "e":
            estado_actual = 5
        elif estado_actual == 4 and i == "e":
            estado_actual = -1
            break
        elif estado_actual ==5:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL

def automata_hasta(n):
    estado_actual = 0
    estados_finales = [5]
    for i in n:
        if estado_actual == 0 and i == "h":
            estado_actual = 1
        elif estado_actual == 0 and i != "h":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "a":
            estado_actual = 2
        elif estado_actual == 1 and i != "a":
            estado_actual = -1
            break
        elif estado_actual == 2 and i == "s":
            estado_actual = 3
        elif estado_actual == 2 and i != "s":
            estado_actual = -1
            break
        elif estado_actual == 3 and i == "t":
            estado_actual = 4
        elif estado_actual == 3 and i != "t":
            estado_actual = -1
            break
        elif estado_actual == 4 and i == "a":
            estado_actual = 5
        elif estado_actual == 4 and i == "a":
            estado_actual = -1
            break
        elif estado_actual ==5:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def automata_entonces(n):
    estado_actual = 0
    estados_finales = [8]
    for i in n:
        if estado_actual == 0 and i == "e":
            estado_actual = 1
        elif estado_actual == 0 and i != "e":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "n":
            estado_actual = 2
        elif estado_actual == 1 and i != "n":
            estado_actual = -1
            break
        elif estado_actual == 2 and i == "t":
            estado_actual = 3
        elif estado_actual == 2 and i != "t":
            estado_actual = -1
            break
        elif estado_actual == 3 and i == "o":
            estado_actual = 4
        elif estado_actual == 3 and i != "o":
            estado_actual = -1
            break
        elif estado_actual == 4 and i == "n":
            estado_actual = 5
        elif estado_actual == 4 and i == "n":
            estado_actual = -1
            break
        elif estado_actual == 5 and i == "c":
            estado_actual = 6
        elif estado_actual == 5 and i != "c":
            estado_actual = -1
            break
        elif estado_actual == 6 and i == "e":
            estado_actual = 7
        elif estado_actual == 6 and i != "e":
            estado_actual = -1
            break
        elif estado_actual == 7 and i == "s":
            estado_actual = 8
        elif estado_actual == 7 and i != "s":
            estado_actual = -1
            break
        if estado_actual == 8:
            estado_actual =-1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
  
def automata_si(n):
    estado_actual = 0
    estados_finales = [2]
    for i in n:
        if estado_actual == 0 and i == "s":
            estado_actual = 1
        elif estado_actual == 0 and i != "s":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "i":
            estado_actual = 2
        elif estado_actual == 1 and i != "i":
            estado_actual = -1
            break
        elif estado_actual == 2:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL

def automata_sino(n):
    estado_actual = 0
    estados_finales = [4]
    for i in n:
        if estado_actual == 0 and i == "s":
            estado_actual = 1
        elif estado_actual == 0 and i != "s":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "i":
            estado_actual = 2
        elif estado_actual == 1 and i != "i":
            estado_actual = -1
            break
        elif estado_actual == 2 and i == "n":
            estado_actual = 3
        elif estado_actual == 2 and i != "n":
            estado_actual = -1
            break
        elif estado_actual == 3 and i == "o":
            estado_actual = 4
        elif estado_actual == 3 and i != "o":
            estado_actual = -1
            break
        elif estado_actual == 4 :
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def automata_mostrar(n):
    estado_actual = 0
    estados_finales = [7]
    for i in n:
        if estado_actual == 0 and i == "m":
            estado_actual = 1
        elif estado_actual == 0 and i != "m":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "o":
            estado_actual = 2
        elif estado_actual == 1 and i != "o":
            estado_actual = -1
            break
        elif estado_actual == 2 and i == "s":
            estado_actual = 3
        elif estado_actual == 2 and i != "s":
            estado_actual = -1
            break
        elif estado_actual == 3 and i == "t":
            estado_actual = 4
        elif estado_actual == 3 and i != "t":
            estado_actual = -1
            break
        elif estado_actual == 4 and i == "r":
            estado_actual = 5
        elif estado_actual == 4 and i == "r":
            estado_actual = -1
            break
        elif estado_actual == 5 and i == "a":
            estado_actual = 6
        elif estado_actual == 5 and i != "a":
            estado_actual= -1
            break
        elif estado_actual == 6 and i == "r":
            estado_actual = 7
        elif estado_actual == 6 and i != "r":
            estado_actual = -1
            break
        elif estado_actual == 7:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def automata_aceptar(n):
    estado_actual = 0
    estados_finales = [7]
    for i in n:
        if estado_actual == 0 and i == "a":
            estado_actual = 1
        elif estado_actual == 0 and i != "a":
            estado_actual = -1
            break
        elif estado_actual == 1 and i == "c":
            estado_actual = 2
        elif estado_actual == 1 and i != "c":
            estado_actual = -1
            break
        elif estado_actual == 2 and i == "e":
            estado_actual = 3
        elif estado_actual == 2 and i != "e":
            estado_actual = -1
            break
        elif estado_actual == 3 and i == "p":
            estado_actual = 4
        elif estado_actual == 3 and i != "p":
            estado_actual = -1
            break
        elif estado_actual == 4 and i == "t":
            estado_actual = 5
        elif estado_actual == 4 and i == "t":
            estado_actual = -1
            break
        elif estado_actual == 5 and i == "a":
            estado_actual = 6
        elif estado_actual == 5 and i != "a":
            estado_actual= -1
            break
        elif estado_actual == 6 and i == "r":
            estado_actual = 7
        elif estado_actual == 6 and i != "r":
            estado_actual = -1
            break
        elif estado_actual == 7:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def automata_id(n):
    estado_actual = 0
    estados_finales =[1]
    for i in n:
        if estado_actual == 0 and i.isalpha():
            estado_actual = 1
        elif estado_actual == 1 and i.isalnum():
            estado_actual = 1
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def automata_cte(n):
    estado_actual = 0
    estados_finales =[1,2,4]
    for i in n:
        if estado_actual == 0 and i == "0":
            estado_actual = 2
        elif estado_actual == 0 and i in ["1","2","3","4","5","6","7","8","9"]:
            estado_actual = 1
        elif estado_actual == 1 and i in ["0","1","2","3","4","5","6","7","8","9"]:
            estado_actual = 1
        elif estado_actual == 1 and i ==".":
            estado_actual = 3
        elif estado_actual == 2 and i == ".":
            estado_actual = 3
        elif estado_actual == 3 and i in ["0","1","2","3","4","5","6","7","8","9"]:
            estado_actual = 4
        elif estado_actual == 4 and i in ["0","1","2","3","4","5","6","7","8","9"]:
            estado_actual = 4
        else:
            estado_actual = -1
            break
    if estado_actual  == -1:
         return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
def automata_op(n):
    if len(n)>1:
        return ESTADO_TRAMPA
    elif (n=="=" or n=="+" or n=="*"):
        return ESTADO_FINAL
    else: 
        return ESTADO_NO_FINAL
def automata_parender(n):
    if len(n)>1:
        return ESTADO_TRAMPA
    elif n==")":
        return ESTADO_FINAL
    else: 
        return ESTADO_NO_FINAL
def automata_parenizq(n):
    if len(n)>1:
        return ESTADO_TRAMPA
    elif n=="(":
        return ESTADO_FINAL
    else: 
        return ESTADO_NO_FINAL
def automata_corder(n):
    if len(n)>1:
        return ESTADO_TRAMPA
    elif n=="}":
        return ESTADO_FINAL
    else: 
        return ESTADO_NO_FINAL
def automata_corizq(n):
    if len(n)>1:
        return ESTADO_TRAMPA
    elif n=="{":
        return ESTADO_FINAL
    else: 
        return ESTADO_NO_FINAL
def lexer(cadena):
    tokens = []
    posicion = 0
    if type(cadena) == str:
        cadena = cadena.lower()
    while posicion < len(cadena):
        while cadena[posicion].isspace():
            posicion+=1
        comienzo_lexema = posicion
        posibles_tokens = []
        posibles_tokens_con_uno_mas = []
        lexema = ""
        todos_trampa = False
        while not todos_trampa:
            todos_trampa = True
            lexema = cadena[comienzo_lexema:posicion+1]
            posibles_tokens = posibles_tokens_con_uno_mas
            posibles_tokens_con_uno_mas = []
            '''para'''
            simulacion_para = automata_para(lexema)
            if simulacion_para == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("para")
                todos_trampa = False
            elif simulacion_para == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''desde'''
            simulacion_desde = automata_desde(lexema)
            if simulacion_desde == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("desde")
                todos_trampa = False
            elif simulacion_desde == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''hasta'''
            simulacion_hasta = automata_hasta(lexema)
            if simulacion_hasta == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("hasta")
                todos_trampa = False
            elif simulacion_hasta == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''entonces'''
            simulacion_entonces = automata_entonces(lexema)
            if simulacion_entonces == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("entonces")
                todos_trampa = False
            elif simulacion_entonces == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''si'''
            simulacion_si = automata_si(lexema)
            if simulacion_si == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("si")
                todos_trampa = False
            elif simulacion_si == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''sino'''
            simulacion_sino = automata_sino(lexema)
            if simulacion_sino == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("sino")
                todos_trampa = False
            elif simulacion_sino == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''mostrar'''
            simulacion_mostrar = automata_mostrar(lexema)
            if simulacion_mostrar == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("mostrar")
                todos_trampa = False
            elif simulacion_mostrar == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''aceptar'''
            simulacion_aceptar = automata_aceptar(lexema)
            if simulacion_aceptar == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("aceptar")
                todos_trampa = False
            elif simulacion_aceptar == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''id'''
            simulacion_id = automata_id(lexema)
            if simulacion_id == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("id")
                todos_trampa = False
            elif simulacion_id == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''cte'''        
            simulacion_cte = automata_cte(lexema)
            if simulacion_cte == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("cte")
                todos_trampa = False
            elif simulacion_cte == ESTADO_NO_FINAL:
                    todos_trampa = False  
            '''op'''
            simulacion_op = automata_op(lexema)
            if simulacion_op == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("op")
                todos_trampa = False
            elif simulacion_op == ESTADO_NO_FINAL:
                  todos_trampa = False       
            '''parender'''            
            simulacion_parender = automata_parender(lexema)
            if simulacion_parender == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("parender")
                todos_trampa = False
            elif simulacion_parender == ESTADO_NO_FINAL:
                    todos_trampa = False
            '''parenizq'''
            simulacion_parenizq = automata_parenizq(lexema)
            if simulacion_parenizq == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("parenizq")
                todos_trampa = False
            elif simulacion_parenizq == ESTADO_NO_FINAL:
                    todos_trampa = False  
            '''corder'''
            simulacion_corder = automata_corder(lexema)
            if simulacion_corder == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("corder")
                todos_trampa = False
            elif simulacion_corder == ESTADO_NO_FINAL:
                    todos_trampa = False      
            posicion = posicion + 1
            '''corizq'''
            simulacion_corizq = automata_corizq(lexema)
            if simulacion_corizq == ESTADO_FINAL:
                posibles_tokens_con_uno_mas.append("corizq")
                todos_trampa = False
            elif simulacion_corizq == ESTADO_NO_FINAL:
                    todos_trampa = False
        if len(posibles_tokens) == 0:
            print("Error TOKEN desconocido" + lexema)
        var_aux_token = posibles_tokens[0]
        token = (var_aux_token, lexema)
        tokens.append(token)
    return tokens
prueba1 = "varaux = 5 * (x + 3)"
prueba2 = "para i desde 1 hasta 11 {mostrar nombre}"
prueba3 = "hsfg = 125 + x * (3 + 2)"
prueba4 = "si ( x + 3 ) entonces { mostrar hola }"
prueba5 = "si ( x + 3 ) entonces { mostrar hola } sino { mostrar python }"
prueba6 = "num = 32"
prueba7 = "mostrar ( 4 + 2 )"
prueba8 = "para i desde 10 hasta 20 { mostrar ( i * 2 ) }"
prueba9 = " " '''derivo programa en lambda'''
prueba10 = "dosporuatro = 2 * 4"
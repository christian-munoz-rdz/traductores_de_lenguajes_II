def es_letra(c):
    return c.isalpha()

def es_digito(c):
    return c.isdigit()

def es_espacio(c):
    return c in ' \t\n\r'

def obtener_tokens(codigo):
    tokens = {
        ";": ("Punto y coma", ";", 2), ",": ("Coma", ",", 3), "(": ("ParéntesisI", "(", 4), ")": ("ParéntesisD", ")", 5), 
        "{": ("LlaveI", "{", 6), "}": ("LlaveD", "}", 7), "=": ("Asignación", "=", 8),
        "if": ("Palabra Reservada", "if", 9), "while": ("Palabra Reservada", "while", 10), 
        "return": ("Palabra Reservada", "return", 11), "else": ("Palabra Reservada", "else", 12), 
        "+": ("Operador Suma", "+", 14), "-": ("Operador Suma", "-", 14),
        "||": ("Operador Logico", "||", 15), "&&": ("Operador Logico", "&&", 15), 
        "*": ("Operador Multiplicacion", "*", 16), "/": ("Operador Multiplicacion", "/", 16), 
        "==": ("Operador Relacional", "==", 17), "<": ("Operador Relacional", "<", 17), 
        "<=": ("Operador Relacional", "<=", 17), ">": ("Operador Relacional", ">", 17), 
        ">=": ("Operador Relacional", ">=", 17), "!=": ("Operador Relacional", "!=", 17), 
        "$": ("Fin de Archivo", "$", 18)
    }
    tipos_de_dato = ["int", "float", "char", "void"]
    
    i = 0
    longitud = len(codigo)
    tokens_identificados = []

    while i < longitud:
        if es_espacio(codigo[i]):
            i += 1
            continue
        
        temp = ""
        
        if es_letra(codigo[i]) or codigo[i] == '_':  # Inicio de identificador o palabra reservada
            while i < longitud and (es_letra(codigo[i]) or es_digito(codigo[i]) or codigo[i] == '_'):
                temp += codigo[i]
                i += 1
            
            if temp in tipos_de_dato:
                tokens_identificados.append(("Tipo de Dato", temp, 0))
            elif temp in tokens:
                tokens_identificados.append(tokens[temp])
            else:
                tokens_identificados.append(("Identificador", temp, 1))
        
        elif es_digito(codigo[i]) or (codigo[i] == '.' and i + 1 < longitud and es_digito(codigo[i + 1])):  # Inicio de constante numérica
            while i < longitud and (es_digito(codigo[i]) or codigo[i] == '.'):
                temp += codigo[i]
                i += 1
            tokens_identificados.append(("Constante", temp, 13))
        
        else:  # Otros caracteres (operadores, delimitadores)
            temp += codigo[i]
            if i + 1 < longitud:
                temp_doble = temp + codigo[i + 1]
                if temp_doble in tokens:  # Verificar operadores de dos caracteres
                    tokens_identificados.append(tokens[temp_doble])
                    i += 2
                    continue
            if temp in tokens:
                tokens_identificados.append(tokens[temp])
            i += 1

    return tokens_identificados

codigo = """
int funcion(int a, float b) {
    int resultado = 0;
    if (a == 0 || b > 0.0) {
        resultado = a + 1;
    } else {
        while (b <= 10.5) {
            resultado = resultado + a * b;
            b = b - 1;
        }
    }
    return resultado;
} 
$
"""

tokens = obtener_tokens(codigo)
for token in tokens:
    print(token)


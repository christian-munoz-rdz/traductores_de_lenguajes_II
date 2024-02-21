import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHBoxLayout

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

# Clase principal de la ventana de la aplicación
class TokenizerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Analizador de Tokens')
        self.setGeometry(100, 100, 1200, 600)
        
        # Layout principal
        layout = QHBoxLayout()
        
        # Área de texto para entrada de código
        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)
        
        # Botón para analizar el texto
        self.btnAnalyze = QPushButton('Analizar')
        self.btnAnalyze.clicked.connect(self.analyzeText)
        layout.addWidget(self.btnAnalyze)
        
        # Tabla para mostrar los tokens
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Tipo de Token', 'Token', 'Número Asociado'])
        layout.addWidget(self.tableWidget)

        #Añadir text edit vacío a la derecha
        self.textEdit2 = QTextEdit()
        layout.addWidget(self.textEdit2)
        
        # Widget contenedor y set layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def analyzeText(self):
        codigo = self.textEdit.toPlainText()
        tokens = obtener_tokens(codigo)
        self.tableWidget.setRowCount(len(tokens))
        
        for i, token in enumerate(tokens):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(token[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(token[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(token[2])))
        
# Punto de entrada de la aplicación
def main():
    app = QApplication(sys.argv)
    ex = TokenizerWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
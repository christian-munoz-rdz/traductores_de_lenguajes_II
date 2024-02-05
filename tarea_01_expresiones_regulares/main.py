from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QColor
import sys
import re

class RegExValidatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Expresiones regulares
        self.regex_patterns = {
            "Dirección IP": r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$", 
            "URL": r"^(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?$", #Completo
            "RFC": r"^[A-ZÑ&]{3,4}\d{6}(?:[A-Z\d]{3})?$", 
            "Fecha de Nacimiento": r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}$", 
            "Email": r"^[\w\.-]+@[\w\.-]+\.\w+$", 
        }

        # Crear campos de entrada y botones
        self.fields = {}
        for label, regex in self.regex_patterns.items():
            h_layout = QHBoxLayout()
            line_edit = QLineEdit()
            button = QPushButton("Verificar")
            result_label = QLabel()
            button.clicked.connect(lambda checked, le=line_edit, rgx=regex, rl=result_label: self.verify(le, rgx, rl))
            h_layout.addWidget(QLabel(label))
            h_layout.addWidget(line_edit)
            h_layout.addWidget(button)
            h_layout.addWidget(result_label)
            self.layout.addLayout(h_layout)
            self.fields[label] = (line_edit, result_label)

        self.setLayout(self.layout)
        self.setWindowTitle('Regex Validator')
        self.show()

    def verify(self, line_edit, regex, result_label):
        text = line_edit.text()
        if re.match(regex, text):
            result_label.setText("Válido")
            result_label.setStyleSheet("color: green")
        else:
            result_label.setText("Inválido")
            result_label.setStyleSheet("color: red")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegExValidatorApp()
    sys.exit(app.exec_())
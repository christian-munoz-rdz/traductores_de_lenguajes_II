import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QColor
import re

class ValidatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Expresiones regulares
        self.regex_patterns = {
            "IP Address": r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",
            "CURP": r"^[A-Z]{4}[0-9]{6}[H,M][A-Z]{5}[A-Z0-9]{2}$",
            "RFC": r"^[A-Z,Ñ,&]{3,4}[0-9]{6}[A-Z,0-9]{3}$",
            "Date of Birth": r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}$",
            "Email": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        }

        # Crear campos de entrada y botones
        self.fields = {}
        for label, regex in self.regex_patterns.items():
            h_layout = QHBoxLayout()
            line_edit = QLineEdit()
            button = QPushButton("Verify")
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
            result_label.setText("Valid")
            result_label.setStyleSheet("color: green")
        else:
            result_label.setText("Invalid")
            result_label.setStyleSheet("color: red")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ValidatorApp()
    sys.exit(app.exec_())
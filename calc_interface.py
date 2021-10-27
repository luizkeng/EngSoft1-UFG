import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget



# GUI da calculadora
class Calculadora_Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        # Config da janela principal
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235, 235)
        # Ajustando o layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Criando os widgets display e buttons
        self._criarDisplay()
        self._criarButtons()
        
    def _criarDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
        
    def _criarButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Buttons e respectiva posição no grid
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '.': (3, 1),
                   'x²': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Adicionar botões ao grid
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)
        
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def limparDisplay(self):
        self.setDisplayText('')

# Client code
def main():
    """Main function."""
    # Instanciando QApplication e carregando o GUI
    pycalc = QApplication(sys.argv)
    view = Calculadora_Ui()
    view.show()
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from functools import partial

# MSG de erro 
ERROR_MSG = 'Expressão Inválida'

def avaliar_expressao(expressao):
    try:
        result = str(eval(expressao, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

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

class Calculadora_control:
    def __init__(self, model, view):
        self._view = view
        self._avaliar = model
        self._connectSignals()

    def _calculateResult(self):
        result = self._avaliar(expressao=self._view.displayText())
        self._view.setDisplayText(result)

    def _ExpressaoMat(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.limparDisplay()
            
        expressao = self._view.displayText() + sub_exp
        self._view.setDisplayText(expressao)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', 'x²'}:
                btn.clicked.connect(partial(self._ExpressaoMat, btnText))
            
            elif btnText == 'x²':
                
                btn.clicked.connect(partial(self._ExpressaoMat, "**2"))

        self._view.buttons['='].clicked.connect(self._calculateResult)  
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.limparDisplay)

# Client code
def main():
    # Instanciando QApplication e carregando o GUI
    pycalc = QApplication(sys.argv)
    view = Calculadora_Ui()
    view.show()
    model = avaliar_expressao
    Calculadora_control(model=model, view=view)
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
import sys
import calculadora
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
		self.display.setReadOnly(False)
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
		self.buttons['7'].clicked.connect(self.action7)
		self.buttons['8'].clicked.connect(self.action8)
		self.buttons['9'].clicked.connect(self.action9)
		self.buttons['/'].clicked.connect(self.actionDiv)
		self.buttons['C'].clicked.connect(self.actionC)
		self.buttons['4'].clicked.connect(self.action4)
		self.buttons['5'].clicked.connect(self.action5)
		self.buttons['6'].clicked.connect(self.action6)
		self.buttons['*'].clicked.connect(self.actionMult)
		self.buttons['('].clicked.connect(self.actionAP)
		self.buttons['1'].clicked.connect(self.action1)
		self.buttons['2'].clicked.connect(self.action2)
		self.buttons['3'].clicked.connect(self.action3)
		self.buttons['-'].clicked.connect(self.actionMenus)
		self.buttons[')'].clicked.connect(self.actionFP)
		self.buttons['0'].clicked.connect(self.action0)
		self.buttons['.'].clicked.connect(self.actionP)
		self.buttons['x²'].clicked.connect(self.actionQ)
		self.buttons['+'].clicked.connect(self.actionMais)
		self.buttons['='].clicked.connect(self.actionIgual)
		
	def setDisplayText(self, text):
		self.display.setText(text)
		self.display.setFocus()

	def displayText(self):
		return self.display.text()

	def limparDisplay(self):
		self.setDisplayText('')

	def action7(self): 
		text = self.display.text() 
		self.display.setText(text + "7")

	def action8(self):
		text = self.display.text() 
		self.display.setText(text + "8")
	
	def action9(self):
		text = self.display.text() 
		self.display.setText(text + "9")
	
	def actionDiv(self):
		text = self.display.text() 
		self.display.setText(text + "/")
	
	def actionC(self):
		self.limparDisplay()
	
	def action4(self):
		text = self.display.text() 
		self.display.setText(text + "4")
	
	def action5(self):
		text = self.display.text() 
		self.display.setText(text + "5")
	
	def action6(self):
		text = self.display.text() 
		self.display.setText(text + "6")
	
	def actionMult(self):
		text = self.display.text() 
		self.display.setText(text + "*")
	
	def actionAP(self):
		text = self.display.text() 
		self.display.setText(text + "(")
	
	def action1(self):
		text = self.display.text() 
		self.display.setText(text + "1")
	
	def action2(self):
		text = self.display.text() 
		self.display.setText(text + "2")
	
	def action3(self):
		text = self.display.text() 
		self.display.setText(text + "3")
	
	def actionMenus(self):
		text = self.display.text() 
		self.display.setText(text + "-")
	
	def actionFP(self):
		text = self.display.text() 
		self.display.setText(text + ")")
	
	def action0(self):
		text = self.display.text() 
		self.display.setText(text + "0")
	
	def actionP(self):
		text = self.display.text() 
		self.display.setText(text + ".")
	
	def actionQ(self):
		text = self.display.text() 
		self.display.setText(text + "**2")
	
	def actionMais(self):
		text = self.display.text() 
		self.display.setText(text + "+")
	
	def actionIgual(self):
		equacao = self.display.text() 
		try: 
			resp = eval(equacao) 
			self.display.setText(str(resp)) 
		except: 
			  self.display.setText("ERRO") 

	

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
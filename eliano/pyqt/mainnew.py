import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():    
    app = QApplication(sys.argv)
    widget = QWidget()
    grid = QGridLayout()

## BUTTONS ###
for i in range(0,5):
    for j in range(0,5):
        grid.addWidget(QPushButton(str(i)+str(j)),i,j)
## FIM BUTTONS ##

### GEOMETRY DO LAYOUT
    widget.setLayout(grid)    
    widget.setGeometry(50,50,200,200)
    widget.setWindowTitle("PyQT Calculadora")
    widget.show()
    sys.exit(app.exec_())

# ## FUNCOES ##
def button1_clicked():
    return 1
def button2_clicked():
    return 2
def buttontotal_clicked():   
    return button1_clicked()+button2_clicked()
        
## FIM FUNCAO ##
if __name__ == "__main__":
    window()
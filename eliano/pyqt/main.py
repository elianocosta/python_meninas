import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

## BUTTONS ###
    button1 = QPushButton(widget)
    button1.setText("1")
    button1.move(220,400)
    button1.clicked.connect(button1_clicked)

    button2 = QPushButton(widget)
    button2.setText("2")
    button2.move(140,400)
    button2.clicked.connect(button2_clicked)
    
    button3 = QPushButton(widget)
    button3.setText("3")
    button3.move(60,400)
    button3.clicked.connect(button3_clicked)

    button4 = QPushButton(widget)
    button4.setText("4")
    button4.move(220,375)
    button4.clicked.connect(button4_clicked)

    button5 = QPushButton(widget)
    button5.setText("5")
    button5.move(140,375)
    button5.clicked.connect(button5_clicked)
    
    button6 = QPushButton(widget)
    button6.setText("6")
    button6.move(60,375)
    button6.clicked.connect(button6_clicked)
    
    button7 = QPushButton(widget)
    button7.setText("7")
    button7.move(220,375)
    button7.clicked.connect(button7_clicked)

    button8 = QPushButton(widget)
    button8.setText("8")
    button8.move(140,375)
    button8.clicked.connect(button8_clicked)
    
    button9 = QPushButton(widget)
    button9.setText("9")
    button9.move(60,375)
    button9.clicked.connect(button9_clicked)
    
    buttontotal = QPushButton(widget)
    buttontotal.setText("total")
    buttontotal.move(120,450)
    buttontotal.clicked.connect(buttontotal_clicked)
## FIM BUTTONS ##

### GEOMETRY DO LAYOUT
    widget.setGeometry(50,50,400,500)
    widget.setWindowTitle("PyQT Calculadora")
    widget.show()
    sys.exit(app.exec_())

# ## FUNCOES ##
def button1_clicked():
    return 1
def button2_clicked():
    return 2
def button3_clicked():
    return 3
def button4_clicked():
    return 4
def button5_clicked():
    return 5
def button6_clicked():
    return 6
def button7_clicked():
    return 7
def button8_clicked():
    return 8
def button9_clicked():
    return 9
def buttontotal_clicked(button1_clicked):   
    print(button1_clicked)
        
## FIM FUNCAO ##
if __name__ == "__main__":
    window()
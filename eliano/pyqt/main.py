import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QApplication,  QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 500))    
        self.setWindowTitle("SetWindowTitle") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        buttontotal = QPushButton('Total', self)
        buttontotal.clicked.connect(self.clickMethod)
        buttontotal.resize(100,32)
        buttontotal.move(80, 60)   
                
        button0 = QPushButton()
        button0.setText('0')
        button0.move(140,325)
        button0.clicked.connect(button0_clicked)

    def clickMethod(self):
        print('Your name: ' + self.line.text())
        
    def button0_clicked():
        return 0
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
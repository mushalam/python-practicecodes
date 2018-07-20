<<<<<<< HEAD
import sys 
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.b=QtWidgets.QPushButton('push me')
        self.bclr = QtWidgets.QPushButton('clear')
        self.l=QtWidgets.QLabel('look at me')
        self.le=QtWidgets.QLineEdit()


        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)
        v_box.addWidget(self.bclr)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('signal')

        self.b.clicked.connect(self.btn_clk)
        self.bclr.clicked.connect(self.btn_clr)

        self.show()
    def btn_clk(self):
        self.l.setText(self.le.text())
        print(self.le.text())

    def btn_clr(self):
        self.l.setText('')
        self.le.setText('')

app=QtWidgets.QApplication(sys.argv)
a_window=Window()
sys.exit(app.exec_())
=======
import sys 
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.b=QtWidgets.QPushButton('push me')
        self.bclr = QtWidgets.QPushButton('clear')
        self.l=QtWidgets.QLabel('look at me')
        self.le=QtWidgets.QLineEdit()


        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)
        v_box.addWidget(self.bclr)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('signal')

        self.b.clicked.connect(self.btn_clk)
        self.bclr.clicked.connect(self.btn_clr)

        self.show()
    def btn_clk(self):
        self.l.setText(self.le.text())
        print(self.le.text())

    def btn_clr(self):
        self.l.setText('')
        self.le.setText('')

app=QtWidgets.QApplication(sys.argv)
a_window=Window()
sys.exit(app.exec_())
>>>>>>> c3a581a6142b4afe5141cc94fd60406c12aa70fe

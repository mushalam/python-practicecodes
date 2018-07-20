import sys
from PyQt5 import QtWidgets

def window():
    app=QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    b=QtWidgets.QPushButton('push me')
    l=QtWidgets.QLabel('look at me')

    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)

    v_box.addLayout(h_box)
    #v_box.addWidget(l)
    w.setLayout(v_box)

    w.setWindowTitle('this is not important')
    w.show()

    sys.exit(app.exec_())

window()
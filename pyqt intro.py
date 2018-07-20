<<<<<<< HEAD
import sys
from PyQt5 import QtWidgets, QtGui
from PIL import Image

def window():
    app= QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    l1=QtWidgets.QLabel(w)
    l2=QtWidgets.QLabel(w)
    img=Image.open('bbt.jpg')
    img=img.resize(50,50)
    img_widget=QtWidgets.
    l1.setText('i am better than you ')
    l2.setPixmap(QtGui.QPixmap('bbt.jpg'))
    l2.setGeometry(50,50,50,50)
    w.setWindowTitle('hello world')
    l1.move(100,20)
    l2.move(100,30)
    w.setGeometry(100,100,300,200)

    w.show()

    sys.exit(app.exec_())

=======
import sys
from PyQt5 import QtWidgets, QtGui
from PIL import Image

def window():
    app= QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    l1=QtWidgets.QLabel(w)
    l2=QtWidgets.QLabel(w)
    img=Image.open('bbt.jpg')
    img=img.resize(50,50)
    img_widget=QtWidgets.
    l1.setText('i am better than you ')
    l2.setPixmap(QtGui.QPixmap('bbt.jpg'))
    l2.setGeometry(50,50,50,50)
    w.setWindowTitle('hello world')
    l1.move(100,20)
    l2.move(100,30)
    w.setGeometry(100,100,300,200)

    w.show()

    sys.exit(app.exec_())

>>>>>>> c3a581a6142b4afe5141cc94fd60406c12aa70fe
window()
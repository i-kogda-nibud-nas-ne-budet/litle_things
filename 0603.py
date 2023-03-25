# create pyqt5 window object
import sys
from PyQt5 import QtWidgets
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.setWindowTitle("PyQt5")
window.setGeometry(100, 100, 300, 300)
# create a label widget
label = QtWidgets.QLabel(window)
label.setText("Hello PyQt5!")
window.show()
app.exec()
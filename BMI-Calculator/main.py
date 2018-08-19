
from BMI_app import *
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
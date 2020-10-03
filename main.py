from window import Window
import sys
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
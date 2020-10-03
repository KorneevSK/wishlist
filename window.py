from PyQt5 import QtWidgets, QtCore
from MainWindow import Ui_MainWindow
import mysql.connector

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.insert())
        self.ui.pushButton_2.clicked.connect(lambda: self.delete())
        self.ui.pushButton_3.clicked.connect(lambda: self.update_())
        self.ui.pushButton_4.clicked.connect(lambda: self.get_())


    def insert(self):
        name = self.ui.textEdit.toPlainText()
        price = self.ui.textEdit_2.toPlainText()
        link = self.ui.textEdit_3.toPlainText()
        note = self.ui.textEdit_4.toPlainText()

        err_msg = QtWidgets.QMessageBox()
        err_msg.setIcon(QtWidgets.QMessageBox.Warning)
        err_msg.setText("Введены не все поля")
        err_msg.setWindowTitle("Статус ввода")
        err_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        succ_msg = QtWidgets.QMessageBox()
        succ_msg.setIcon(QtWidgets.QMessageBox.Information)
        succ_msg.setText("Ввод выполнен успешно")
        succ_msg.setWindowTitle("Статус ввода")
        succ_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        if (name=="" or price=="" or link=="" or note==""):
            err_msg.exec()
        else:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="vista",
                port="3306"
            )
            cursor = con.cursor()
            cursor.execute("insert into wishlist values('"+ name +"','"+ price +"','"+ link +"','"+ note +"')")
            cursor.execute("commit")

            self.ui.textEdit.clear()
            self.ui.textEdit_2.clear()
            self.ui.textEdit_3.clear()
            self.ui.textEdit_4.clear()
            succ_msg.exec()
            con.close()

    def delete(self):
        name = self.ui.textEdit.toPlainText()

        err_msg = QtWidgets.QMessageBox()
        err_msg.setIcon(QtWidgets.QMessageBox.Warning)
        err_msg.setText('Поле "Имя" обязательно для ввода')
        err_msg.setWindowTitle("Статус удаления")
        err_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        succ_msg = QtWidgets.QMessageBox()
        succ_msg.setIcon(QtWidgets.QMessageBox.Information)
        succ_msg.setText("Удаление выполнено успешно")
        succ_msg.setWindowTitle("Статус удаления")
        succ_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        if (name==""):
            err_msg.exec()
        else:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="vista",
                port="3306"
            )
            cursor = con.cursor()
            cursor.execute("delete from wishlist where name='" + name + "'")
            cursor.execute("commit")

            self.ui.textEdit.clear()
            self.ui.textEdit_2.clear()
            self.ui.textEdit_3.clear()
            self.ui.textEdit_4.clear()
            succ_msg.exec()
            con.close()

    def update_(self):
        name = self.ui.textEdit.toPlainText()
        price = self.ui.textEdit_2.toPlainText()
        link = self.ui.textEdit_3.toPlainText()
        note = self.ui.textEdit_4.toPlainText()

        err_msg = QtWidgets.QMessageBox()
        err_msg.setIcon(QtWidgets.QMessageBox.Warning)
        err_msg.setText("Введены не все поля")
        err_msg.setWindowTitle("Статус изменения")
        err_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        succ_msg = QtWidgets.QMessageBox()
        succ_msg.setIcon(QtWidgets.QMessageBox.Information)
        succ_msg.setText("Изменение выполнено успешно")
        succ_msg.setWindowTitle("Статус изменения")
        succ_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        if (name == "" or price == "" or link == "" or note == ""):
            err_msg.exec()
        else:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="vista",
                port="3306"
            )
            cursor = con.cursor()
            cursor.execute("update wishlist set price='" + price + "', link='" + link + "', note='" + note + "' where name='" + name + "'")
            cursor.execute("commit")

            self.ui.textEdit.clear()
            self.ui.textEdit_2.clear()
            self.ui.textEdit_3.clear()
            self.ui.textEdit_4.clear()
            succ_msg.exec()
            con.close()

    def get_(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vista",
            port="3306"
        )
        
        cursor = con.cursor()
        cursor.execute("select * from wishlist")
        rows = cursor.fetchall()
        table = self.ui.tableView
        model = TableModel(rows)
        table.setModel(model)

        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()
        self.ui.textEdit_3.clear()
        self.ui.textEdit_4.clear()
        con.close()
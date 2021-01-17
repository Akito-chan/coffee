import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.select_data)

    def select_data(self):
        query = "SELECT * FROM coffee"
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
    
    
# import sys
# 
# from PyQt5 import uic 
# from PyQt5.QtWidgets import QApplication, QMainWindow
# 
# 
# class MyWidget(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('main.ui', self) 
#         self.pushButton.clicked.connect(self.run)
# 
#     def run(self):
#         self.label.setText("OK")
#         # Имя элемента совпадает с objectName в QTDesigner
# 
# 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWidget()
#     ex.show()
#     sys.exit(app.exec_())
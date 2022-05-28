from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(668, 634)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.add_btn = QtWidgets.QPushButton(Dialog,clicked=lambda : self.add())
        self.add_btn.setGeometry(QtCore.QRect(94, 270, 141, 41))
        self.add_btn.setObjectName("add_btn")
        self.next_btn = QtWidgets.QPushButton(Dialog,clicked=lambda : self.next())
        self.next_btn.setGeometry(QtCore.QRect(390, 270, 121, 41))
        self.next_btn.setObjectName("next_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 40, 211, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 211, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 220, 461, 20))
        self.label_3.setObjectName("label_3")
        self.txt_num = QtWidgets.QLineEdit(Dialog)
        self.txt_num.setGeometry(QtCore.QRect(332, 129, 211, 41))
        self.txt_num.setObjectName("txt_num")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(100, 360, 456, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 500)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def add(self):
        stream = self.txt_num.text().strip().upper()
        if stream =='' :
            self.label_3.setText('Please enter the stream name first')
        else:
            con=mysql.connector.connect(host='localhost',user='root',passwd='gautam123',database='sms')
            cur1=con.cursor()
            sql= "insert into streams(stream) values (%s);"
            value=(stream,)
            cur1.execute(sql,value)
            if cur1.rowcount>0:
                self.label_3.setText('Stream Added Sucessfully!!!')
                self.add_btn.setEnabled(False)
            else:
                self.label_3.setText('Error')

            con.commit()
            con.close()
            self.show_stream()


    def next(self):
        self.add_btn.setEnabled(True)
        self.txt_num.setText('')
        self.txt_num.setFocus(True)

    def show_stream(self):
        con=mysql.connector.connect(host='localhost',user='root',passwd='gautam123',database='sms')
        cur1=con.cursor()
        sql='select * from streams'
        cur1.execute(sql)
        result=cur1.fetchall()
        self.tableWidget.setRowCount(len(result))
        tbl_row=0
        for data in result:
            self.tableWidget.setItem(tbl_row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.tableWidget.setItem(tbl_row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            tbl_row += 1
        con.close()






    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_btn.setText(_translate("Dialog", "ADD"))
        self.next_btn.setText(_translate("Dialog", "Next"))
        self.label.setText(_translate("Dialog", "Add Stream Name"))
        self.label_2.setText(_translate("Dialog", "Enter Stream Name"))
        self.label_3.setText(_translate("Dialog", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "student_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "student_stream"))
        self.show_stream()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

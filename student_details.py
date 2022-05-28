from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from add_stream import Ui_Dialog


class Ui_add_student(object):
    def setupUi(self, add_student):
        add_student.setObjectName("add_student")
        add_student.resize(656, 544)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        add_student.setFont(font)
        self.label = QtWidgets.QLabel(add_student)
        self.label.setGeometry(QtCore.QRect(230, 30, 271, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(add_student)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 121, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(add_student)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(add_student)
        self.label_4.setGeometry(QtCore.QRect(90, 260, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(add_student)
        self.label_5.setGeometry(QtCore.QRect(90, 330, 111, 31))
        self.label_5.setObjectName("label_5")
        self.lbl_msg = QtWidgets.QLabel(add_student)
        self.lbl_msg.setGeometry(QtCore.QRect(90, 400, 471, 41))
        self.lbl_msg.setObjectName("lbl_msg")
        self.btn_saave = QtWidgets.QPushButton(add_student)
        self.btn_saave.setGeometry(QtCore.QRect(280, 470, 111, 41))
        self.btn_saave.setObjectName("btn_saave")
        self.btn_next = QtWidgets.QPushButton(add_student)
        self.btn_next.setGeometry(QtCore.QRect(484, 472, 101, 41))
        self.btn_next.setObjectName("btn_next")
        self.txt_name = QtWidgets.QLineEdit(add_student)
        self.txt_name.setGeometry(QtCore.QRect(270, 110, 201, 41))
        self.txt_name.setObjectName("txt_name")
        self.txt_roll = QtWidgets.QLineEdit(add_student)
        self.txt_roll.setGeometry(QtCore.QRect(270, 180, 201, 41))
        self.txt_roll.setObjectName("txt_roll")
        self.txt_phone = QtWidgets.QLineEdit(add_student)
        self.txt_phone.setGeometry(QtCore.QRect(270, 260, 201, 41))
        self.txt_phone.setObjectName("txt_phone")
        self.cmb_stream = QtWidgets.QComboBox(add_student)
        self.cmb_stream.setGeometry(QtCore.QRect(270, 340, 191, 31))
        self.cmb_stream.setObjectName("cmb_stream")

        self.retranslateUi(add_student)
        QtCore.QMetaObject.connectSlotsByName(add_student)

        self.btn_saave.clicked.connect(self.save)
        self.btn_next.clicked.connect(self.next)


    def save(self):

        s_name=self.txt_name.text().upper().strip()
        s_roll=self.txt_roll.text().strip()
        s_phone=self.txt_phone.text().strip()
        s_stream=self.cmb_stream.currentData()
        if s_name=='' or s_roll == '' or s_phone == '':
            self.lbl_msg.setText('please enter correct name ,roll no. and phone')
        else:
            con=mysql.connector.connect(host='localhost',user='root',passwd='gautam123',database='sms')
            cur1=con.cursor()
            sql='insert into students(name,roll_no,phone_no,stream_id) values (%s,%s,%s,%s);'
            value=(s_name,s_roll,s_phone,s_stream)
            cur1.execute(sql,value)
            if cur1.rowcount > 0:
                self.lbl_msg.setText('Data Added Sucessfully!!!')
                self.btn_saave.setEnabled(False)
            else:
                self.lbl_msg.setText('Error')

            con.commit()
            con.close()


    def show_streams(self):
        con = mysql.connector.connect(host='localhost', user='root', passwd='gautam123', database='sms')
        cur1 = con.cursor()
        sql='select * from streams'
        cur1.execute(sql)
        data=cur1.fetchall()
        for stream in data:
            self.cmb_stream.addItem(stream[1],stream[0])
        con.close()


    def next(self):
        self.txt_phone.setText("")
        self.txt_roll.setText("")
        self.txt_name.setText("")
        self.btn_saave.setEnabled(True)
        self.txt_name.setFocus(True)


    def retranslateUi(self, add_student):
        _translate = QtCore.QCoreApplication.translate
        add_student.setWindowTitle(_translate("add_student", "Student Management System"))
        self.label.setText(_translate("add_student", "Add Student Form"))
        self.label_2.setText(_translate("add_student", "Name"))
        self.label_3.setText(_translate("add_student", "Roll No."))
        self.label_4.setText(_translate("add_student", "Phone NO."))
        self.label_5.setText(_translate("add_student", "Stream"))
        self.lbl_msg.setText(_translate("add_student", ""))
        self.btn_saave.setText(_translate("add_student", "Save"))
        self.btn_next.setText(_translate("add_student", "Next"))
        self.show_streams()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_student = QtWidgets.QDialog()
    ui = Ui_add_student()
    ui.setupUi(add_student)
    add_student.show()
    sys.exit(app.exec_())

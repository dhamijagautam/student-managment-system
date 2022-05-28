from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from fpdf import FPDF
import settings

con_str= settings.con_str


class Ui_rep_find_name(object):
    def setupUi(self, rep_find_rollno):
        rep_find_rollno.setObjectName("rep_find_rollno")
        rep_find_rollno.resize(654, 561)
        self.label = QtWidgets.QLabel(rep_find_rollno)
        self.label.setGeometry(QtCore.QRect(120, 30, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(rep_find_rollno)
        self.label_2.setGeometry(QtCore.QRect(16, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_roll = QtWidgets.QLineEdit(rep_find_rollno)
        self.txt_roll.setGeometry(QtCore.QRect(122, 110, 131, 31))
        self.txt_roll.setObjectName("txt_roll")
        self.btn_search = QtWidgets.QPushButton(rep_find_rollno)
        self.btn_search.setGeometry(QtCore.QRect(290, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.btn_next = QtWidgets.QPushButton(rep_find_rollno)
        self.btn_next.setGeometry(QtCore.QRect(410, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_next.setFont(font)
        self.btn_next.setObjectName("btn_next")
        self.btn_export = QtWidgets.QPushButton(rep_find_rollno)
        self.btn_export.setGeometry(QtCore.QRect(540, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_export.setFont(font)
        self.btn_export.setObjectName("btn_export")
        self.tbl_result = QtWidgets.QTableWidget(rep_find_rollno)
        self.tbl_result.setGeometry(QtCore.QRect(10, 210, 641, 221))
        self.tbl_result.setObjectName("tbl_result")
        self.tbl_result.setColumnCount(5)
        self.tbl_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(4, item)
        self.lbl_msg = QtWidgets.QLabel(rep_find_rollno)
        self.lbl_msg.setGeometry(QtCore.QRect(20, 160, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_msg.setFont(font)
        self.lbl_msg.setObjectName("lbl_msg")

        self.retranslateUi(rep_find_rollno)
        QtCore.QMetaObject.connectSlotsByName(rep_find_rollno)
        self.btn_search.clicked.connect(self.search)
        self.btn_export.clicked.connect(self.export)

    def search(self):
        rn = self.txt_roll.text().strip()
        if rn == '' :
            self.lbl_msg.setText('Please enter the name to search')
        else:
            #con = mysql.connector.connect(host='localhost', user='root', passwd='gautam123', database='sms')
            con = eval('mysql.connector.connect({})'.format(con_str))
            cur1 = con.cursor()
            sql = '''select stu_id,name,stream,roll_no,phone_no from students 
            inner join streams using(stream_id) where name like "%'''+str(rn)+'''%"'''
            cur1.execute(sql)
            tbl_data=cur1.fetchall()
            tr=0
            self.tbl_result.setRowCount(len(tbl_data))
            for data in tbl_data:
                self.tbl_result.setItem(tr,0,QtWidgets.QTableWidgetItem(str(data[0])))
                self.tbl_result.setItem(tr, 1, QtWidgets.QTableWidgetItem(str(data[1])))
                self.tbl_result.setItem(tr, 2, QtWidgets.QTableWidgetItem(str(data[2])))
                self.tbl_result.setItem(tr, 3, QtWidgets.QTableWidgetItem(str(data[3])))
                self.tbl_result.setItem(tr, 4, QtWidgets.QTableWidgetItem(str(data[4])))
                tr+=1
            con.close()


    def export(self):
        pdf=FPDF('P','mm','A4')
        pdf.add_page()
        pdf.set_font('times','BIU',20)
        pdf.set_text_color(255,0,0)
        pdf.cell(50,10,'list of students admitted in the instuitution',ln=True,border=False)
        pdf.set_font('times','B',10)
        pdf.set_text_color(0,0,0)
        pdf.set_fill_color(244,164,96)
        pdf.cell(10,10,'SN',align='C',border=True,fill=True)
        pdf.cell(10,10, ' Id ',align='C',border=True,fill=True)
        pdf.cell(40, 10, 'Name', border=True, fill=True)
        pdf.cell(40, 10, 'Stream', border=True, fill=True)
        pdf.cell(20, 10, 'Roll no', align='C', border=True, fill=True)
        pdf.cell(20, 10, 'Phone NO', align='C',ln=True, border=True, fill=True)

        rn = self.txt_roll.text().strip()
        if rn == '' :
            self.lbl_msg.setText('Please enter the name')
        else:
            #con = mysql.connector.connect(host='localhost', user='root', passwd='gautam123', database='sms')
            con = eval('mysql.connector.connect({})'.format(con_str))
            cur1 = con.cursor()
            sql = '''select stu_id,name,stream,roll_no,phone_no from students 
            inner join streams using(stream_id) where name like "%'''+str(rn)+'''%"'''
            cur1.execute(sql)
            tbl_data = cur1.fetchall()
            SN=1
            pdf.set_font('times','',14)
            for data in tbl_data:
                if SN%2==0:
                    pdf.set_fill_color(222,184,135)
                else:
                    pdf.set_fill_color(250,235,215)
                pdf.cell(10, 10, str(SN), align='C', border=True, fill=True)
                pdf.cell(10, 10, str(data[0]), align='C', border=True, fill=True)
                pdf.cell(40, 10, data[1], border=True, fill=True)
                pdf.cell(40, 10, data[2], border=True, fill=True)
                pdf.cell(20, 10, str(data[3]), align='C', border=True, fill=True)
                pdf.cell(20, 10, str(data[4]), align='C', border=True, fill=True)
                pdf.ln(10)
                SN+=1

            con.close()
            pdf.output('student_rec.pdf')
            import webbrowser
            webbrowser.open_new('student_rec.pdf')



    def retranslateUi(self, rep_find_rollno):
        _translate = QtCore.QCoreApplication.translate
        rep_find_rollno.setWindowTitle(_translate("rep_find_rollno", "Find student by Name"))
        self.label.setText(_translate("rep_find_rollno", "Find Student By Name"))
        self.label_2.setText(_translate("rep_find_rollno", "Name"))
        self.btn_search.setText(_translate("rep_find_rollno", "Search"))
        self.btn_next.setText(_translate("rep_find_rollno", "Next"))
        self.btn_export.setText(_translate("rep_find_rollno", "Export"))
        item = self.tbl_result.horizontalHeaderItem(0)
        item.setText(_translate("rep_find_rollno", "Student_id"))
        item = self.tbl_result.horizontalHeaderItem(1)
        item.setText(_translate("rep_find_rollno", "Name"))
        item = self.tbl_result.horizontalHeaderItem(2)
        item.setText(_translate("rep_find_rollno", "Stream"))
        item = self.tbl_result.horizontalHeaderItem(3)
        item.setText(_translate("rep_find_rollno", "Roll No."))
        item = self.tbl_result.horizontalHeaderItem(4)
        item.setText(_translate("rep_find_rollno", "Phone NO"))
        self.lbl_msg.setText(_translate("rep_find_rollno", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rep_find_rollno = QtWidgets.QDialog()
    ui = Ui_rep_find_name()
    ui.setupUi(rep_find_rollno)
    rep_find_rollno.show()
    sys.exit(app.exec_())

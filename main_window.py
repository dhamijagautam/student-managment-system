from PyQt5 import QtCore, QtGui, QtWidgets
from add_stream import Ui_Dialog
from student_details import Ui_add_student
from rpt_search_name import Ui_rep_find_name
from rpt_search_rollno import Ui_rep_find_rollno
from rpt_search_stream import Ui_rep_find_stream


class Ui_main_sms(object):
    def setupUi(self, main_sms):
        main_sms.setObjectName("main_sms")
        main_sms.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_sms)
        self.centralwidget.setObjectName("centralwidget")
        main_sms.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_sms)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdd_data = QtWidgets.QMenu(self.menubar)
        self.menuAdd_data.setObjectName("menuAdd_data")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        main_sms.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_sms)
        self.statusbar.setObjectName("statusbar")
        main_sms.setStatusBar(self.statusbar)
        self.actionAdd_stream = QtWidgets.QAction(main_sms,triggered=lambda: self.show_form('add_stream'))
        self.actionAdd_stream.setObjectName("actionAdd_stream")
        self.actionAdd_student = QtWidgets.QAction(main_sms,triggered=lambda: self.show_form('add_student'))
        self.actionAdd_student.setObjectName("actionAdd_student")
        self.actionsearch_student_by_name = QtWidgets.QAction(main_sms,triggered=lambda: self.show_form('rpt_name'))
        self.actionsearch_student_by_name.setObjectName("actionsearch_student_by_name")
        self.actionSearch_student_by_roll_no = QtWidgets.QAction(main_sms,triggered=lambda: self.show_form('rpt_rollno'))
        self.actionSearch_student_by_roll_no.setObjectName("actionSearch_student_by_roll_no")
        self.actionSearch_student_by_streeam = QtWidgets.QAction(main_sms,triggered=lambda: self.show_form('rpt_stream'))
        self.actionSearch_student_by_streeam.setObjectName("actionSearch_student_by_streeam")
        self.menuAdd_data.addAction(self.actionAdd_stream)
        self.menuAdd_data.addAction(self.actionAdd_student)
        self.menuReports.addAction(self.actionsearch_student_by_name)
        self.menuReports.addAction(self.actionSearch_student_by_roll_no)
        self.menuReports.addAction(self.actionSearch_student_by_streeam)
        self.menubar.addAction(self.menuAdd_data.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())


        self.retranslateUi(main_sms)
        QtCore.QMetaObject.connectSlotsByName(main_sms)


    def show_form(self,n):
        self.window= QtWidgets.QWidget()
        if n=='add_stream':
            self.ui = Ui_Dialog()
        elif n=='add_student':
            self.ui=Ui_add_student()
        elif n=='rpt_name':
            self.ui=Ui_rep_find_name()
        elif n=='rpt_rollno':
            self.ui=Ui_rep_find_rollno()
        elif n=='rpt_stream':
            self.ui =Ui_rep_find_stream()


        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, main_sms):
        _translate = QtCore.QCoreApplication.translate
        main_sms.setWindowTitle(_translate("main_sms", "Student Management System"))
        self.menuAdd_data.setTitle(_translate("main_sms", "Add data"))
        self.menuReports.setTitle(_translate("main_sms", "Reports"))
        self.actionAdd_stream.setText(_translate("main_sms", "Add stream"))
        self.actionAdd_student.setText(_translate("main_sms", "Add student"))
        self.actionsearch_student_by_name.setText(_translate("main_sms", "Search student by name "))
        self.actionSearch_student_by_roll_no.setText(_translate("main_sms", "Search student by roll no"))
        self.actionSearch_student_by_streeam.setText(_translate("main_sms", "Search student by stream"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_sms = QtWidgets.QMainWindow()
    ui = Ui_main_sms()
    ui.setupUi(main_sms)
    main_sms.show()
    sys.exit(app.exec_())

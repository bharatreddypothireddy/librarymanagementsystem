# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb
from datetime import datetime
import re
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 613)
        self.error_dialog = QtWidgets.QErrorMessage()
        self.message_dialog = QtWidgets.QMessageBox()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.notebook = QtWidgets.QTabWidget(self.centralwidget)
        self.notebook.setGeometry(QtCore.QRect(10, 0, 921, 571))
        self.notebook.setObjectName("notebook")
        self.search_tab = QtWidgets.QWidget()
        self.search_tab.setObjectName("search_tab")
        self.search_button = QtWidgets.QPushButton(self.search_tab)
        self.search_button.setGeometry(QtCore.QRect(670, 40, 201, 61))
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.search1)
        self.search_entry = QtWidgets.QLineEdit(self.search_tab)
        self.search_entry.setGeometry(QtCore.QRect(10, 50, 461, 51))
        self.search_entry.setObjectName("search_entry")
        self.search_table = QtWidgets.QTableWidget(self.search_tab)
        self.search_table.setGeometry(QtCore.QRect(10, 140, 891, 381))
        self.search_table.setObjectName("search_table")
        self.search_table.setColumnCount(4)
        self.search_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(3, item)
        self.label_6 = QtWidgets.QLabel(self.search_tab)
        self.label_6.setGeometry(QtCore.QRect(10, 19, 141, 21))
        self.label_6.setObjectName("label_6")
        self.notebook.addTab(self.search_tab, "")
        self.checkout_tab = QtWidgets.QWidget()
        self.checkout_tab.setObjectName("checkout_tab")
        self.checkout_cardno_entry = QtWidgets.QLineEdit(self.checkout_tab)
        self.checkout_cardno_entry.setGeometry(QtCore.QRect(130, 50, 211, 31))
        self.checkout_cardno_entry.setObjectName("checkout_cardno_entry")
        self.checkout_isbn_entry = QtWidgets.QLineEdit(self.checkout_tab)
        self.checkout_isbn_entry.setGeometry(QtCore.QRect(130, 110, 211, 31))
        self.checkout_isbn_entry.setObjectName("checkout_isbn_entry")
        self.label_2 = QtWidgets.QLabel(self.checkout_tab)
        self.label_2.setGeometry(QtCore.QRect(20, 55, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.checkout_tab)
        self.label_3.setGeometry(QtCore.QRect(20, 105, 91, 41))
        self.label_3.setObjectName("label_3")
        self.checkout_button = QtWidgets.QPushButton(self.checkout_tab)
        self.checkout_button.setGeometry(QtCore.QRect(530, 40, 201, 91))
        self.checkout_button.setObjectName("checkout_button")
        self.checkout_button.clicked.connect(self.checkout1)
        self.notebook.addTab(self.checkout_tab, "")
        self.checkin_tab = QtWidgets.QWidget()
        self.checkin_tab.setObjectName("checkin_tab")
        self.checkin_isbn = QtWidgets.QLineEdit(self.checkin_tab)
        self.checkin_isbn.setGeometry(QtCore.QRect(140, 10, 151, 31))
        self.checkin_isbn.setObjectName("checkin_isbn")
        self.checkin_cardno = QtWidgets.QLineEdit(self.checkin_tab)
        self.checkin_cardno.setGeometry(QtCore.QRect(480, 10, 113, 31))
        self.checkin_cardno.setObjectName("checkin_cardno")
        self.checkin_name = QtWidgets.QLineEdit(self.checkin_tab)
        self.checkin_name.setGeometry(QtCore.QRect(750, 10, 161, 31))
        self.checkin_name.setObjectName("checkin_name")
        self.label = QtWidgets.QLabel(self.checkin_tab)
        self.label.setGeometry(QtCore.QRect(10, 15, 111, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.checkin_tab)
        self.label_4.setGeometry(QtCore.QRect(370, 15, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.checkin_tab)
        self.label_5.setGeometry(QtCore.QRect(650, 15, 81, 21))
        self.label_5.setObjectName("label_5")
        self.checkin_checkloans_button = QtWidgets.QPushButton(self.checkin_tab)
        self.checkin_checkloans_button.setGeometry(QtCore.QRect(310, 60, 311, 41))
        self.checkin_checkloans_button.setObjectName("checkin_checkloans_button")
        self.checkin_checkloans_button.clicked.connect(self.checkforloans)
        self.checkin_table = QtWidgets.QTableWidget(self.checkin_tab)
        self.checkin_table.setGeometry(QtCore.QRect(10, 110, 751, 311))
        self.checkin_table.setObjectName("checkin_table")
        self.checkin_table.setColumnCount(6)
        self.checkin_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.checkin_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkin_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkin_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkin_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkin_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkin_table.setHorizontalHeaderItem(5, item)
        self.checkin_checkin_button = QtWidgets.QPushButton(self.checkin_tab)
        self.checkin_checkin_button.setGeometry(QtCore.QRect(330, 451, 291, 41))
        self.checkin_checkin_button.setObjectName("checkin_checkin_button")
        self.checkin_checkin_button.clicked.connect(self.checkin1)
        self.notebook.addTab(self.checkin_tab, "")
        self.borrower_tab = QtWidgets.QWidget()
        self.borrower_tab.setObjectName("borrower_tab")
        self.borrower_name = QtWidgets.QLineEdit(self.borrower_tab)
        self.borrower_name.setGeometry(QtCore.QRect(140, 20, 231, 41))
        self.borrower_name.setObjectName("borrower_name")
        self.borrower_email = QtWidgets.QLineEdit(self.borrower_tab)
        self.borrower_email.setGeometry(QtCore.QRect(630, 20, 211, 41))
        self.borrower_email.setObjectName("borrower_email")
        self.borrower_address = QtWidgets.QLineEdit(self.borrower_tab)
        self.borrower_address.setGeometry(QtCore.QRect(140, 180, 321, 171))
        self.borrower_address.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.borrower_address.setObjectName("borrower_address")
        self.borrower_ssn = QtWidgets.QLineEdit(self.borrower_tab)
        self.borrower_ssn.setGeometry(QtCore.QRect(140, 100, 231, 41))
        self.borrower_ssn.setObjectName("borrower_ssn")
        self.borrower_phone = QtWidgets.QLineEdit(self.borrower_tab)
        self.borrower_phone.setGeometry(QtCore.QRect(630, 100, 211, 41))
        self.borrower_phone.setObjectName("borrower_phone")
        self.borrower_addborrower_button = QtWidgets.QPushButton(self.borrower_tab)
        self.borrower_addborrower_button.setGeometry(QtCore.QRect(70, 420, 181, 51))
        self.borrower_addborrower_button.setObjectName("borrower_addborrower_button")
        self.borrower_addborrower_button.clicked.connect(self.addborrowers)
        self.borrower_reset_button = QtWidgets.QPushButton(self.borrower_tab)
        self.borrower_reset_button.setGeometry(QtCore.QRect(490, 420, 171, 51))
        self.borrower_reset_button.setObjectName("borrower_reset_button")
        self.borrower_reset_button.clicked.connect(self.resetdetails)
        self.label_7 = QtWidgets.QLabel(self.borrower_tab)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 91, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.borrower_tab)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 91, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.borrower_tab)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 91, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.borrower_tab)
        self.label_10.setGeometry(QtCore.QRect(500, 20, 101, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.borrower_tab)
        self.label_11.setGeometry(QtCore.QRect(500, 100, 91, 31))
        self.label_11.setObjectName("label_11")
        self.notebook.addTab(self.borrower_tab, "")
        self.fines_tab = QtWidgets.QWidget()
        self.fines_tab.setObjectName("fines_tab")
        self.label_12 = QtWidgets.QLabel(self.fines_tab)
        self.label_12.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.label_12.setObjectName("label_12")
        self.fines_checkfines_button = QtWidgets.QPushButton(self.fines_tab)
        self.fines_checkfines_button.setGeometry(QtCore.QRect(650, 30, 181, 41))
        self.fines_checkfines_button.setObjectName("fines_checkfines_button")
        self.fines_checkfines_button.clicked.connect(self.checkfines)
        self.fines_refresh_button = QtWidgets.QPushButton(self.fines_tab)
        self.fines_refresh_button.setGeometry(QtCore.QRect(680, 460, 131, 41))
        self.fines_refresh_button.setObjectName("fines_refresh_button")
        self.fines_refresh_button.clicked.connect(self.refreshfines)
        self.fines_fineamount_button = QtWidgets.QPushButton(self.fines_tab)
        self.fines_fineamount_button.setGeometry(QtCore.QRect(350, 460, 161, 41))
        self.fines_fineamount_button.setObjectName("fines_fineamount_button")
        self.fines_fineamount_button.clicked.connect(self.fineamount)
        self.fines_payfines_button = QtWidgets.QPushButton(self.fines_tab)
        self.fines_payfines_button.setGeometry(QtCore.QRect(30, 460, 161, 41))
        self.fines_payfines_button.setObjectName("fines_payfines_button")
        self.fines_payfines_button.clicked.connect(self.payfines)
        self.fines_entry = QtWidgets.QLineEdit(self.fines_tab)
        self.fines_entry.setGeometry(QtCore.QRect(150, 30, 201, 31))
        self.fines_entry.setObjectName("fines_entry")
        self.fines_table = QtWidgets.QTableWidget(self.fines_tab)
        self.fines_table.setGeometry(QtCore.QRect(30, 80, 801, 341))
        self.fines_table.setObjectName("fines_table")
        self.fines_table.setColumnCount(5)
        self.fines_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fines_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fines_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fines_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fines_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fines_table.setHorizontalHeaderItem(4, item)
        self.notebook.addTab(self.fines_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.notebook.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.search_entry.setPlaceholderText(_translate("MainWindow", "Enter Isbn/Author Name/Title"))
        item = self.search_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.search_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book Title"))
        item = self.search_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Author"))
        item = self.search_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Availability"))
        self.label_6.setText(_translate("MainWindow", "Enter here"))
        self.notebook.setTabText(self.notebook.indexOf(self.search_tab), _translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Card No*:"))
        self.label_3.setText(_translate("MainWindow", "ISBN*:"))
        self.checkout_button.setText(_translate("MainWindow", "Check Out"))
        self.notebook.setTabText(self.notebook.indexOf(self.checkout_tab), _translate("MainWindow", "Check Out"))
        self.label.setText(_translate("MainWindow", "ISBN:"))
        self.label_4.setText(_translate("MainWindow", "Card Number:"))
        self.label_5.setText(_translate("MainWindow", "Name:"))
        self.checkin_checkloans_button.setText(_translate("MainWindow", "Check for Loans"))
        item = self.checkin_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LOAN ID"))
        item = self.checkin_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.checkin_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CARD ID"))
        item = self.checkin_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DATE OUT"))
        item = self.checkin_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DUE DATE"))
        item = self.checkin_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DATE IN"))
        self.checkin_checkin_button.setText(_translate("MainWindow", "Check In"))
        self.notebook.setTabText(self.notebook.indexOf(self.checkin_tab), _translate("MainWindow", "Check In"))
        self.borrower_name.setPlaceholderText(_translate("MainWindow", "FirstName + Last Name"))
        self.borrower_email.setPlaceholderText(_translate("MainWindow","example@mail.com"))
        self.borrower_phone.setPlaceholderText(_translate("MainWindow", "(999)99-9999"))
        self.borrower_ssn.setPlaceholderText(_translate("MainWindow","999-99-9999"))
        self.borrower_addborrower_button.setText(_translate("MainWindow", "Add Borrower"))
        self.borrower_reset_button.setText(_translate("MainWindow", "Reset Details"))
        self.label_7.setText(_translate("MainWindow", "Name:"))
        self.label_8.setText(_translate("MainWindow", "SSN:"))
        self.label_9.setText(_translate("MainWindow", "Address:"))
        self.label_10.setText(_translate("MainWindow", "Email:"))
        self.label_11.setText(_translate("MainWindow", "Phone:"))
        self.notebook.setTabText(self.notebook.indexOf(self.borrower_tab), _translate("MainWindow", "Borrower"))
        self.label_12.setText(_translate("MainWindow", "Card No:"))
        self.fines_checkfines_button.setText(_translate("MainWindow", "Check Fines"))
        self.fines_refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.fines_fineamount_button.setText(_translate("MainWindow", "Fine Amount"))
        self.fines_payfines_button.setText(_translate("MainWindow", "Pay Fines"))
        item = self.fines_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Loan_ID"))
        item = self.fines_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.fines_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fine"))
        item = self.fines_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Paid"))
        item = self.fines_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Returned"))
        self.notebook.setTabText(self.notebook.indexOf(self.fines_tab), _translate("MainWindow", "Fines"))

    def search1(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        search = self.search_entry.text()
        if(search!=""):
            try:
                query = "select b.isbn10,b.title,a.name,b.status FROM BOOK b ,BOOK_AUTHORS ba , AUTHORS A WHERE b.isbn10=ba.isbn10 AND ba.author_id=a.author_id AND (b.isbn10 like '%" + search + "%' OR b.title like '%" + search + "%' OR a.name like '%" + search + "%') ORDER BY b.isbn10"
                cursor.execute(query)
                row = cursor.fetchall()
                self.search_table.setRowCount(0)
                for row_number,row_data in enumerate(row):
                    self.search_table.insertRow(row_number)
                    for column_number,data in enumerate(row_data):
                        self.search_table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

            except Exception as e:
                logger.error(str(e))
        else:
            self.error_dialog.showMessage('Enter ISBN/Author Name/Title')
        db.close()

    def checkout1(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        isbn10 = self.checkout_isbn_entry.text()
        cardid = self.checkout_cardno_entry.text()
        if(isbn10!="" and cardid!=""):


            query1 = "select * FROM BOOK where isbn10='"+isbn10+"'"
            query2 = "select * FROM BORROWER where card_id='"+cardid+"'"
            query3 = "select count(loan_id) FROM BOOK_LOANS where card_id='"+cardid+"' AND date_in IS NULL"
            cursor.execute(query1)
            row1 = cursor.fetchall()
            cursor.execute(query2)
            row2 = cursor.fetchall()
            cursor.execute(query3)
            row3 = cursor.fetchall()
            try:
                if(len(row1)==1 and len(row2)==1):
                    if(row3[0][0]<3):
                         if(row1[0][3]==1):   #checking availability

                             query4 = "insert into BOOK_LOANS (isbn10,card_id,date_out,due_date)" + "values ('" + isbn10 + "', '" + cardid + "', curdate(), DATE_ADD(date_out,INTERVAL 14 DAY))"
                             query5 = "UPDATE BOOK SET status = 0 WHERE isbn10='" + isbn10 + "'"
                             cursor.execute(query4)
                             cursor.execute(query5)
                             db.commit()
                             self.message_dialog.about(self.message_dialog,"","New entry created in BOOK_LOANS")
                         else:
                             self.error_dialog.showMessage('Book is not available ')
                    else:
                        self.error_dialog.showMessage('User already borrowed 3 books')
                else:
                    self.error_dialog.showMessage('Please enter details of ISBN and CARDID again')



            except Exception as e:
                print(str(e))

        elif(isbn10=="" or cardid==""):
            self.error_dialog.showMessage('Please enter details of ISBN and CARDID ')

        db.close()

    def checkforloans(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        isbn10 = self.checkin_isbn.text()
        cardid = self.checkin_cardno.text()
        name = self.checkin_name.text()
        if(isbn10 != "" or cardid != "" or name != ""):
            if(isbn10!="" and cardid=="" and name==""):
                query1 = "SELECT * FROM BOOK_LOANS WHERE isbn10='"+isbn10+"' AND date_in IS NULL"
            elif (isbn10 == "" and cardid != "" and name == ""):
                query1 = "SELECT * FROM BOOK_LOANS WHERE card_id='" + cardid + "' AND date_in IS NULL"
            elif (isbn10 == "" and cardid == "" and name != ""):
                query1 = "SELECT bl.* FROM BOOK_LOANS bl,BORROWER b WHERE b.card_id=bl.card_id  AND bl.date_in IS NULL AND b.bname like '%"+name+"%'"
            elif (isbn10 != "" and cardid != "" and name == ""):
                query1 = "SELECT * FROM BOOK_LOANS WHERE isbn10='" + isbn10 + "' AND date_in IS NULL"
            elif (isbn10 != "" and cardid == "" and name != ""):
                query1 = "SELECT * FROM BOOK_LOANS WHERE isbn10='" + isbn10 + "' AND date_in IS NULL"
            elif (isbn10 == "" and cardid != "" and name != ""):
                query1= "SELECT * FROM BOOK_LOANS WHERE card_id='" + cardid + "' AND date_in IS NULL"
            elif (isbn10 != "" and cardid != "" and name != ""):
                query1 = "SELECT * FROM BOOK_LOANS WHERE isbn10='" + isbn10 + "' AND date_in IS NULL"

            cursor.execute(query1)
            row = cursor.fetchall()
            self.checkin_table.setRowCount(0)
            if(len(row)==0):
                self.message_dialog.about(self.message_dialog,"","You have no outstanding loans")
            else:
                for row_number, row_data in enumerate(row):
                    self.checkin_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.checkin_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.message_dialog.about(self.message_dialog,"","Please select the ISBN of book you want to checkin")
        elif (isbn10 == "" and cardid == "" and name == ""):
            self.message_dialog.about(self.message_dialog, "Error", "Please enter atleast one of ISBN/CARD No/Name")
        db.close()

    def checkin1(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        if(self.checkin_table.rowCount()>0):
            isbn10 = self.checkin_table.currentItem().text()
            loan_id = self.checkin_table.item(self.checkin_table.currentItem().row(),0).text()
            if(len(isbn10)== 10):

                try:
                    query1 = "UPDATE BOOK_LOANS SET date_in = curdate() WHERE isbn10 = '" + isbn10 + "'"
                    query2 = "UPDATE BOOK SET status = 1 WHERE isbn10 = '"+ isbn10 + "'"

                    cursor.execute(query1)
                    cursor.execute(query2)
                    db.commit()
                    query3 = "select datediff(date_in,due_date) as diff from BOOK_LOANS where isbn10 = '" + isbn10 + "'"
                    cursor.execute(query3)
                    row3 = cursor.fetchall()
                    days = row3[0][0]
                    if(len(row3)==1 and days > 0):
                        fine = float(days*0.25)
                        query4 = "INSERT INTO FINES(loan_id,fine_amount,paid) values ('"+loan_id+"','"+fine+"',0)"
                        cursor.execute(query4)
                    db.commit()
                    self.message_dialog.about(self.message_dialog, "","Check in successful.")
                except Exception as e:
                    print(str(e))
            else:
                self.message_dialog.about(self.message_dialog, "", "Please select the ISBN of the book you want to check in.")

        else:
            self.message_dialog.about(self.message_dialog, "Error", "You don't have any books to check in.")
        db.close()

    def addborrowers(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        name = self.borrower_name.text()
        email = self.borrower_email.text()
        ssn = self.borrower_ssn.text()
        phone = self.borrower_phone.text()
        address = self.borrower_address.text()
        query1 = "SELECT count(*) FROM BORROWER where ssn = '"+ssn+"'"
        cursor.execute(query1)
        row1 = cursor.fetchall()
        if(name!="" and email!="" and ssn!="" and phone!="" and address!=""):
            if(re.match("^[0-9]{3}\-[0-9]{2}\-[0-9]{4}",ssn)):
                if(row1[0][0] == 0):
                    if(re.match("^\([0-9]{3}\)\-[0-9]{3}\-[0-9]{4}",phone)):
                        if(re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email)):
                            query1 = "INSERT INTO BORROWER(ssn,bname,email,address,phone) VALUES ('"+ssn+"','"+name+"','"+email+"','"+address+"','"+phone+"')"
                            cursor.execute(query1)
                            db.commit()
                            self.message_dialog.about(self.message_dialog, "Error", "Successfully added a borrower.")
                        else:
                            self.message_dialog.about(self.message_dialog, "Error", "Please enter a valid email.")
                    else:
                        self.message_dialog.about(self.message_dialog, "Error", "Please enter a valid phone number in the specified format.")
                else:
                    self.message_dialog.about(self.message_dialog, "Error", "Library card already exists with the SSN.")
            else:
                self.message_dialog.about(self.message_dialog, "Error", "Please enter a valid SSN in the specified format.")
        else:
            self.message_dialog.about(self.message_dialog, "Error", "Please enter all the required fields.")

        db.close()

    def resetdetails(self):
        self.borrower_name.setText("")
        self.borrower_email.setText("")
        self.borrower_ssn.setText("")
        self.borrower_phone.setText("")
        self.borrower_address.setText("")

    def checkfines(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        card_id = self.fines_entry.text()
        if(card_id == ""):
            self.message_dialog.about(self.message_dialog, "Error", "Please enter your Card number/ID.")
        else:
            query1 = "SELECT * FROM BORROWER WHERE card_id ='"+card_id+"'"
            cursor.execute(query1)
            row1 = cursor.fetchall()
            if(len(row1)==0):
                self.message_dialog.about(self.message_dialog, "Error", "Invalid Card number/ID")
            else:
                query2 = "SELECT f.loan_id,bl.isbn10,f.fine_amount,f.paid,bl.date_in,datediff(curdate(), bl.due_date) as curdue,datediff( bl.date_in,bl.due_date) as indue from book_loans bl join fines f on  bl.loan_id = f.loan_id where  bl.card_id='"+card_id+"' having curdue>0 or indue>0"
                cursor.execute(query2)
                row2 = cursor.fetchall()
                self.fines_table.setRowCount(0)
                if(len(row2)==0):
                    self.message_dialog.about(self.message_dialog, "Error", "No Loans available ")
                else:
                    for i,data in enumerate(row2):
                        self.fines_table.insertRow(i)
                        self.fines_table.setItem(i,0,QtWidgets.QTableWidgetItem(str(row2[i][0])))
                        self.fines_table.setItem(i,1,QtWidgets.QTableWidgetItem(str(row2[i][1])))
                        self.fines_table.setItem(i,2, QtWidgets.QTableWidgetItem(str(row2[i][2])))
                        self.fines_table.setItem(i,3, QtWidgets.QTableWidgetItem(str(row2[i][3])))
                        if(row2[i][4]== "NULL" ):
                            self.fines_table.setItem(i,4,QtWidgets.QTableWidgetItem(str("NO")))
                        else:
                            self.fines_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str("YES")))
                    self.message_dialog.about(self.message_dialog, "", "Please select the item you want to pay fine for")
        db.close()

    def payfines(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        if(self.fines_table.rowCount() == 0):
            self.message_dialog.about(self.message_dialog, "", "No Fines to pay")
        else:
            i = self.fines_table.currentItem().row()
            if(i<0):
                self.message_dialog.about(self.message_dialog, "", "Please select the item you want to pay fine for")
            else:
                loan_id = self.fines_table.item(i,0).text()
                paid = self.fines_table.item(i,3).text()
                returned = self.fines_table.item(i,4).text()
                if(returned == "NO"):
                    self.message_dialog.about(self.message_dialog, "", "The book is yet to be checked in.")
                else:
                    if(paid == "1"):
                        self.message_dialog.about(self.message_dialog, "", "Fine already paid for this book - No Dues.")
                    else:
                        query1 = "UPDATE FINES set paid = 1 where loan_id ='"+loan_id+"'"
                        cursor.execute(query1)
                        db.commit()
                        self.message_dialog.about(self.message_dialog, "", "Fine Paid.")

        db.close()

    def fineamount(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        card_id = self.fines_entry.text()
        if(card_id!=""):
            query1 = "select * from BORROWER where card_id ='"+card_id+"'"
            cursor.execute(query1)
            row1 = cursor.fetchall()
            if(len(row1)==0):
                self.message_dialog.about(self.message_dialog, "", "Invalid Card Number/ID")
            else:
                query2 = "select sum(fine_amount) as sum from FINES f join BOOK_LOANS bl on bl.loan_id=f.loan_id where card_id ='"+card_id+"' and paid=0"
                cursor.execute(query2)
                row2 = cursor.fetchall()
                print (row2)
                if(row2[0][0] != None):
                    sum = str(row2[0][0])
                    if(sum == "NULL"):
                        self.message_dialog.about(self.message_dialog, "", "No fines")
                    else:
                        self.message_dialog.about(self.message_dialog, "", "Total fine amount is :"+sum)
                else:
                    self.message_dialog.about(self.message_dialog, "", "No fines")
        else:
            self.message_dialog.about(self.message_dialog, "", "Please enter card number/ID")
        db.close()

    def refreshfines(self):
        db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                             user="root",  # your username
                             passwd="bharath44",  # your password
                             db="LIBRARY_MANAGEMENT")  # name of the data base
        cursor = db.cursor()
        query1 = "select loan_id,date_in,datediff(curdate(), due_date),datediff(date_in,due_date) from book_loans"
        cursor.execute(query1)
        row1 =cursor.fetchall()
        for i,data in enumerate(row1):
            loan_id = row1[i][0]
            date_in = row1[i][1]
            if(date_in == None):
                day1 = row1[i][2]
                if(day1 > 0):
                    fine_amount = float(day1*0.25)
                    query2 = "select * from fines where loan_id='" + loan_id + "'"
                    cursor.execute(query2)
                    row2 = cursor.fetchall()
                    if(len(row2)>0 and (row2[0][3] == 0 or row2[0][3] == "0")):
                        query3 = "Update fines set fine_amount = '" + fine_amount + "' where loan_id = '" + loan_id + "'"
                        cursor.execute(query3)
                    else:
                        query4 = "INSERT INTO FINES(loan_id, fine_amount ) values ('"+loan_id+"','"+fine_amount+"')"
                        cursor.execute(query4)
                else:
                    print("No fines for loan_id :"+str(loan_id))
            else:
                day1 = row1[i][3]
                if (day1!= None):
                    if(day1>0):
                        fine_amount = float(day1 * 0.25)
                        query2 = "select * from fines where loan_id='" + loan_id + "'"
                        cursor.execute(query2)
                        row2 = cursor.fetchall()
                        if (len(row2) > 0 and (row2[0][3] == 0 or row2[0][3] == "0")):
                            query3 = "Update fines set fine_amount = '" + fine_amount + "' where loan_id = '" + loan_id + "'"
                            cursor.execute(query3)
                        else:
                            query4 = "INSERT INTO FINES(loan_id, fine_amount ) values ('" + loan_id + "','" + fine_amount + "')"
                            cursor.execute(query4)
                else:
                    print("No fines for loan_id :" + str(loan_id))
        db.commit()
        self.message_dialog.about(self.message_dialog, "", "Fines refreshed")
        db.close()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

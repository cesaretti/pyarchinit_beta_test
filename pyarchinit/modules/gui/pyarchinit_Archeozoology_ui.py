# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_Archeozoology_ui.ui'
#
# Created: Thu Mar 15 23:48:03 2012
#      by: PyQt4 UI code generator snapshot-4.8.6-4726879563e5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogArcheoZoology(object):
    def setupUi(self, DialogArcheoZoology):
        DialogArcheoZoology.setObjectName(_fromUtf8("DialogArcheoZoology"))
        DialogArcheoZoology.resize(700, 591)
        DialogArcheoZoology.setMinimumSize(QtCore.QSize(540, 400))
        DialogArcheoZoology.setWindowTitle(QtGui.QApplication.translate("DialogArcheoZoology", "pyArchInit Gestione Scavi - Archeozoologia Quantificazioni", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconSite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogArcheoZoology.setWindowIcon(icon)
        self.gridLayout_9 = QtGui.QGridLayout(DialogArcheoZoology)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_29 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setText(QtGui.QApplication.translate("DialogArcheoZoology", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.pushButton_connect = QtGui.QPushButton(DialogArcheoZoology)
        self.pushButton_connect.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Reload DB", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.gridLayout_2.addWidget(self.pushButton_connect, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_first_rec = QtGui.QPushButton(DialogArcheoZoology)
        self.pushButton_first_rec.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/5_leftArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon1)
        self.pushButton_first_rec.setObjectName(_fromUtf8("pushButton_first_rec"))
        self.gridLayout.addWidget(self.pushButton_first_rec, 0, 0, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(DialogArcheoZoology)
        self.pushButton_prev_rec.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/4_leftArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon2)
        self.pushButton_prev_rec.setObjectName(_fromUtf8("pushButton_prev_rec"))
        self.gridLayout.addWidget(self.pushButton_prev_rec, 0, 1, 1, 2)
        self.pushButton_next_rec = QtGui.QPushButton(DialogArcheoZoology)
        self.pushButton_next_rec.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/6_rightArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon3)
        self.pushButton_next_rec.setObjectName(_fromUtf8("pushButton_next_rec"))
        self.gridLayout.addWidget(self.pushButton_next_rec, 0, 4, 1, 1)
        self.pushButton_last_rec = QtGui.QPushButton(DialogArcheoZoology)
        self.pushButton_last_rec.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/7_rightArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon4)
        self.pushButton_last_rec.setObjectName(_fromUtf8("pushButton_last_rec"))
        self.gridLayout.addWidget(self.pushButton_last_rec, 0, 5, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        self.pushButton_new_rec.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/newrec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon5)
        self.pushButton_new_rec.setObjectName(_fromUtf8("pushButton_new_rec"))
        self.gridLayout.addWidget(self.pushButton_new_rec, 0, 6, 1, 1)
        self.pushButton_save = QtGui.QPushButton(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/b_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon6)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 0, 7, 1, 1)
        self.pushButton_delete = QtGui.QPushButton(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon7)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.gridLayout.addWidget(self.pushButton_delete, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(70, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        self.pushButton_new_search.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/new_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon8)
        self.pushButton_new_search.setObjectName(_fromUtf8("pushButton_new_search"))
        self.gridLayout.addWidget(self.pushButton_new_search, 1, 4, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        self.pushButton_search_go.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon9)
        self.pushButton_search_go.setObjectName(_fromUtf8("pushButton_search_go"))
        self.gridLayout.addWidget(self.pushButton_search_go, 1, 5, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon10)
        self.pushButton_sort.setObjectName(_fromUtf8("pushButton_sort"))
        self.gridLayout.addWidget(self.pushButton_sort, 1, 6, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        self.pushButton_view_all.setToolTip(QtGui.QApplication.translate("DialogArcheoZoology", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/view_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon11)
        self.pushButton_view_all.setObjectName(_fromUtf8("pushButton_view_all"))
        self.gridLayout.addWidget(self.pushButton_view_all, 1, 7, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line_6 = QtGui.QFrame(DialogArcheoZoology)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_42 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setText(QtGui.QApplication.translate("DialogArcheoZoology", "DB Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_43 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setMargin(0)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_status = QtGui.QLabel(DialogArcheoZoology)
        self.label_status.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_status.setMouseTracking(False)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setMargin(0)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_4.addWidget(self.label_status, 1, 0, 1, 1)
        self.label_sort = QtGui.QLabel(DialogArcheoZoology)
        self.label_sort.setMinimumSize(QtCore.QSize(40, 0))
        self.label_sort.setSizeIncrement(QtCore.QSize(40, 0))
        self.label_sort.setBaseSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_sort.setFont(font)
        self.label_sort.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_sort.setMouseTracking(False)
        self.label_sort.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sort.setFrameShape(QtGui.QFrame.Box)
        self.label_sort.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sort.setText(_fromUtf8(""))
        self.label_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sort.setMargin(0)
        self.label_sort.setObjectName(_fromUtf8("label_sort"))
        self.gridLayout_4.addWidget(self.label_sort, 1, 1, 1, 1)
        self.label_34 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setMargin(0)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_27 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setText(QtGui.QApplication.translate("DialogArcheoZoology", "record n.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setMargin(0)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_rec_corrente = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_corrente.setFont(font)
        self.label_rec_corrente.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_rec_corrente.setMouseTracking(False)
        self.label_rec_corrente.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_corrente.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_corrente.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_corrente.setText(QtGui.QApplication.translate("DialogArcheoZoology", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_corrente.setObjectName(_fromUtf8("label_rec_corrente"))
        self.gridLayout_3.addWidget(self.label_rec_corrente, 0, 1, 1, 1)
        self.label_28 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setText(QtGui.QApplication.translate("DialogArcheoZoology", "record tot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setMargin(0)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_rec_tot = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_tot.setFont(font)
        self.label_rec_tot.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_rec_tot.setMouseTracking(False)
        self.label_rec_tot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_tot.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_tot.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_tot.setText(QtGui.QApplication.translate("DialogArcheoZoology", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_tot.setObjectName(_fromUtf8("label_rec_tot"))
        self.gridLayout_3.addWidget(self.label_rec_tot, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_8 = QtGui.QFrame(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout.addWidget(self.line_8)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.comboBox_sito = QtGui.QComboBox(DialogArcheoZoology)
        self.comboBox_sito.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_sito.setFont(font)
        self.comboBox_sito.setMouseTracking(True)
        self.comboBox_sito.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_sito.setEditable(True)
        self.comboBox_sito.setMaxVisibleItems(99999)
        self.comboBox_sito.setMaxCount(2147483647)
        self.comboBox_sito.setFrame(False)
        self.comboBox_sito.setObjectName(_fromUtf8("comboBox_sito"))
        self.comboBox_sito.addItem(_fromUtf8(""))
        self.comboBox_sito.setItemText(0, QtGui.QApplication.translate("DialogArcheoZoology", "Inserisci un valore", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_7.addWidget(self.comboBox_sito, 0, 0, 3, 5)
        self.label = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Sito", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("DialogArcheoZoology", "US", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_7.addWidget(self.label_8, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Area", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit_area = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_area.setObjectName(_fromUtf8("lineEdit_area"))
        self.gridLayout_7.addWidget(self.lineEdit_area, 5, 0, 1, 1)
        self.lineEdit_us = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_us.setObjectName(_fromUtf8("lineEdit_us"))
        self.gridLayout_7.addWidget(self.lineEdit_us, 5, 1, 1, 1)
        self.lineEdit_quadrato = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_quadrato.setObjectName(_fromUtf8("lineEdit_quadrato"))
        self.gridLayout_7.addWidget(self.lineEdit_quadrato, 5, 2, 1, 1)
        self.label_2 = QtGui.QLabel(DialogArcheoZoology)
        self.label_2.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Quadrato", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 6, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(500, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 5, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_3 = QtGui.QLabel(DialogArcheoZoology)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_coord_x = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_coord_x.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_coord_x.setFont(font)
        self.lineEdit_coord_x.setText(QtGui.QApplication.translate("DialogArcheoZoology", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_coord_x.setObjectName(_fromUtf8("lineEdit_coord_x"))
        self.gridLayout_6.addWidget(self.lineEdit_coord_x, 0, 2, 1, 1)
        self.lineEdit_coord_y = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_coord_y.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_coord_y.setFont(font)
        self.lineEdit_coord_y.setText(QtGui.QApplication.translate("DialogArcheoZoology", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_coord_y.setObjectName(_fromUtf8("lineEdit_coord_y"))
        self.gridLayout_6.addWidget(self.lineEdit_coord_y, 0, 3, 1, 1)
        self.lineEdit_bos_bison = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_bos_bison.setObjectName(_fromUtf8("lineEdit_bos_bison"))
        self.gridLayout_6.addWidget(self.lineEdit_bos_bison, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(DialogArcheoZoology)
        self.label_6.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Bos/Bison", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_9 = QtGui.QLabel(DialogArcheoZoology)
        self.label_9.setText(QtGui.QApplication.translate("DialogArcheoZoology", "DATI QUANTITATIVI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_6.addWidget(self.label_9, 1, 0, 1, 1)
        self.lineEdit_coord_z = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_coord_z.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_coord_z.setObjectName(_fromUtf8("lineEdit_coord_z"))
        self.gridLayout_6.addWidget(self.lineEdit_coord_z, 0, 4, 1, 1)
        self.lineEdit_calcinati = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_calcinati.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_calcinati.setObjectName(_fromUtf8("lineEdit_calcinati"))
        self.gridLayout_6.addWidget(self.lineEdit_calcinati, 2, 1, 1, 1)
        self.lineEdit_camoscio = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_camoscio.setObjectName(_fromUtf8("lineEdit_camoscio"))
        self.gridLayout_6.addWidget(self.lineEdit_camoscio, 2, 2, 1, 1)
        self.label_11 = QtGui.QLabel(DialogArcheoZoology)
        self.label_11.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Calcinati", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_6.addWidget(self.label_11, 3, 1, 1, 1)
        self.label_12 = QtGui.QLabel(DialogArcheoZoology)
        self.label_12.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Camoscio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_6.addWidget(self.label_12, 3, 2, 1, 1)
        self.lineEdit_combuste = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_combuste.setObjectName(_fromUtf8("lineEdit_combuste"))
        self.gridLayout_6.addWidget(self.lineEdit_combuste, 2, 3, 1, 1)
        self.label_16 = QtGui.QLabel(DialogArcheoZoology)
        self.label_16.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Combuste", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_6.addWidget(self.label_16, 3, 3, 1, 1)
        self.label_4 = QtGui.QLabel(DialogArcheoZoology)
        self.label_4.setText(QtGui.QApplication.translate("DialogArcheoZoology", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setIndent(0)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(DialogArcheoZoology)
        self.label_5.setText(QtGui.QApplication.translate("DialogArcheoZoology", "y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setIndent(0)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 1, 3, 1, 1)
        self.label_10 = QtGui.QLabel(DialogArcheoZoology)
        self.label_10.setText(QtGui.QApplication.translate("DialogArcheoZoology", "z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_6.addWidget(self.label_10, 1, 4, 1, 1)
        self.label_19 = QtGui.QLabel(DialogArcheoZoology)
        self.label_19.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Stambecco", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_6.addWidget(self.label_19, 5, 2, 1, 1)
        self.lineEdit_capriolo = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_capriolo.setObjectName(_fromUtf8("lineEdit_capriolo"))
        self.gridLayout_6.addWidget(self.lineEdit_capriolo, 4, 0, 1, 1)
        self.lineEdit_cervi = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_cervi.setObjectName(_fromUtf8("lineEdit_cervi"))
        self.gridLayout_6.addWidget(self.lineEdit_cervi, 4, 1, 1, 1)
        self.lineEdit_strie = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_strie.setObjectName(_fromUtf8("lineEdit_strie"))
        self.gridLayout_6.addWidget(self.lineEdit_strie, 4, 3, 1, 1)
        self.lineEdit_stambecco = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_stambecco.setObjectName(_fromUtf8("lineEdit_stambecco"))
        self.gridLayout_6.addWidget(self.lineEdit_stambecco, 4, 2, 1, 1)
        self.label_15 = QtGui.QLabel(DialogArcheoZoology)
        self.label_15.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Cervi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_6.addWidget(self.label_15, 5, 1, 1, 1)
        self.label_13 = QtGui.QLabel(DialogArcheoZoology)
        self.label_13.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Capriolo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_6.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_20 = QtGui.QLabel(DialogArcheoZoology)
        self.label_20.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Strie", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_6.addWidget(self.label_20, 5, 3, 1, 1)
        self.lineEdit_Coni = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_Coni.setObjectName(_fromUtf8("lineEdit_Coni"))
        self.gridLayout_6.addWidget(self.lineEdit_Coni, 2, 4, 1, 1)
        self.label_18 = QtGui.QLabel(DialogArcheoZoology)
        self.label_18.setText(QtGui.QApplication.translate("DialogArcheoZoology", "PDI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 3, 5, 1, 1)
        self.label_17 = QtGui.QLabel(DialogArcheoZoology)
        self.label_17.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Coni", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_6.addWidget(self.label_17, 3, 4, 1, 1)
        self.lineEdit_pdi = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_pdi.setObjectName(_fromUtf8("lineEdit_pdi"))
        self.gridLayout_6.addWidget(self.lineEdit_pdi, 2, 5, 1, 1)
        self.lineEdit_canidi = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_canidi.setObjectName(_fromUtf8("lineEdit_canidi"))
        self.gridLayout_6.addWidget(self.lineEdit_canidi, 4, 4, 1, 1)
        self.lineEdit_ursidi = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_ursidi.setObjectName(_fromUtf8("lineEdit_ursidi"))
        self.gridLayout_6.addWidget(self.lineEdit_ursidi, 4, 5, 1, 1)
        self.label_21 = QtGui.QLabel(DialogArcheoZoology)
        self.label_21.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Canidi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_6.addWidget(self.label_21, 5, 4, 1, 1)
        self.label_22 = QtGui.QLabel(DialogArcheoZoology)
        self.label_22.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Ursidi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_6.addWidget(self.label_22, 5, 5, 1, 1)
        self.lineEdit_megacero = QtGui.QLineEdit(DialogArcheoZoology)
        self.lineEdit_megacero.setObjectName(_fromUtf8("lineEdit_megacero"))
        self.gridLayout_6.addWidget(self.lineEdit_megacero, 6, 0, 1, 1)
        self.label_14 = QtGui.QLabel(DialogArcheoZoology)
        self.label_14.setText(QtGui.QApplication.translate("DialogArcheoZoology", "Megacero", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_6.addWidget(self.label_14, 7, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.verticalLayout_2.addLayout(self.gridLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.label_8.setBuddy(self.lineEdit_us)
        self.label_7.setBuddy(self.lineEdit_area)
        self.label_2.setBuddy(self.lineEdit_quadrato)

        self.retranslateUi(DialogArcheoZoology)
        QtCore.QMetaObject.connectSlotsByName(DialogArcheoZoology)

    def retranslateUi(self, DialogArcheoZoology):
        pass

import resources_rc

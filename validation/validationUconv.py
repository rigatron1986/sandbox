# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\Rigadisk\06_library\12_SCRIPTS_AND_WORKFILES\python\pipeline\core\Validation\validation.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(360, 680)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(376, 681))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lw_errors = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_errors.sizePolicy().hasHeightForWidth())
        self.lw_errors.setSizePolicy(sizePolicy)
        self.lw_errors.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lw_errors.setAutoScroll(False)
        self.lw_errors.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lw_errors.setProperty("showDropIndicator", False)
        self.lw_errors.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.lw_errors.setResizeMode(QtGui.QListView.Adjust)
        self.lw_errors.setLayoutMode(QtGui.QListView.SinglePass)
        self.lw_errors.setViewMode(QtGui.QListView.IconMode)
        self.lw_errors.setObjectName(_fromUtf8("lw_errors"))
        self.gridLayout.addWidget(self.lw_errors, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))


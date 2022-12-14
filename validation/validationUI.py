# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 680)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(376, 681))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lw_errors = QListWidget(Form)
        self.lw_errors.setObjectName(u"lw_errors")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_errors.sizePolicy().hasHeightForWidth())
        self.lw_errors.setSizePolicy(sizePolicy)
        self.lw_errors.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lw_errors.setAutoScroll(False)
        self.lw_errors.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lw_errors.setProperty("showDropIndicator", False)
        self.lw_errors.setSelectionMode(QAbstractItemView.NoSelection)
        self.lw_errors.setResizeMode(QListView.Adjust)
        self.lw_errors.setLayoutMode(QListView.SinglePass)
        self.lw_errors.setViewMode(QListView.IconMode)

        self.gridLayout.addWidget(self.lw_errors, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

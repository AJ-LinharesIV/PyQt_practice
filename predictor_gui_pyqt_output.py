# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'predictor_template.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(976, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelMain = QtWidgets.QLabel(self.centralwidget)
        self.labelMain.setGeometry(QtCore.QRect(230, 20, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelMain.setFont(font)
        self.labelMain.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMain.setObjectName("labelMain")
        self.ButtonPredict = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPredict.setGeometry(QtCore.QRect(680, 130, 161, 61))
        self.ButtonPredict.setObjectName("ButtonPredict")
        self.groupBoxInput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxInput.setGeometry(QtCore.QRect(9, 50, 591, 141))
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBoxInput)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 571, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPredEndDate = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelPredEndDate.setObjectName("labelPredEndDate")
        self.verticalLayout.addWidget(self.labelPredEndDate)
        self.labelInputData = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelInputData.setObjectName("labelInputData")
        self.verticalLayout.addWidget(self.labelInputData)
        self.labelPredSpecDate = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelPredSpecDate.setObjectName("labelPredSpecDate")
        self.verticalLayout.addWidget(self.labelPredSpecDate)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.datePredictEnd = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.datePredictEnd.setObjectName("datePredictEnd")
        self.verticalLayout_5.addWidget(self.datePredictEnd)
        self.pushButtonInputFile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonInputFile.setObjectName("pushButtonInputFile")
        self.verticalLayout_5.addWidget(self.pushButtonInputFile)
        self.datePredictSpec = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.datePredictSpec.setObjectName("datePredictSpec")
        self.verticalLayout_5.addWidget(self.datePredictSpec)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.linePredEndDate = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.linePredEndDate.setObjectName("linePredEndDate")
        self.verticalLayout_2.addWidget(self.linePredEndDate)
        self.lineInputDataFile = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineInputDataFile.setObjectName("lineInputDataFile")
        self.verticalLayout_2.addWidget(self.lineInputDataFile)
        self.linePredSpecDate = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.linePredSpecDate.setObjectName("linePredSpecDate")
        self.verticalLayout_2.addWidget(self.linePredSpecDate)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 391, 421))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 371, 391))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelPredValue = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelPredValue.setObjectName("labelPredValue")
        self.horizontalLayout_2.addWidget(self.labelPredValue)
        self.linePredValue = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.linePredValue.setObjectName("linePredValue")
        self.horizontalLayout_2.addWidget(self.linePredValue)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.checkSavePlotToFile = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkSavePlotToFile.setObjectName("checkSavePlotToFile")
        self.verticalLayout_3.addWidget(self.checkSavePlotToFile)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelPlotFile = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelPlotFile.setObjectName("labelPlotFile")
        self.horizontalLayout_3.addWidget(self.labelPlotFile)
        self.linePlotFile = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.linePlotFile.setObjectName("linePlotFile")
        self.horizontalLayout_3.addWidget(self.linePlotFile)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.textBrowserOutput = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowserOutput.setObjectName("textBrowserOutput")
        self.verticalLayout_3.addWidget(self.textBrowserOutput)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(660, 70, 211, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBoxRegressionSetting = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxRegressionSetting.setGeometry(QtCore.QRect(10, 20, 191, 22))
        self.comboBoxRegressionSetting.setObjectName("comboBoxRegressionSetting")
        self.comboBoxRegressionSetting.addItem("")
        self.comboBoxRegressionSetting.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(410, 200, 541, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_4.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelMain.setText(_translate("MainWindow", "Meta Prophet Wrapper v1.0"))
        self.ButtonPredict.setText(_translate("MainWindow", "Fit Model and Plot"))
        self.groupBoxInput.setTitle(_translate("MainWindow", "Input"))
        self.labelPredEndDate.setText(_translate("MainWindow", "Plot End Date:"))
        self.labelInputData.setText(_translate("MainWindow", "Input Data File:"))
        self.labelPredSpecDate.setText(_translate("MainWindow", "Value at Date:"))
        self.pushButtonInputFile.setText(_translate("MainWindow", "Select File"))
        self.groupBox.setTitle(_translate("MainWindow", "Output"))
        self.labelPredValue.setText(_translate("MainWindow", "Predicted Value at Date:"))
        self.checkSavePlotToFile.setText(_translate("MainWindow", "Save Plot to PDF"))
        self.labelPlotFile.setText(_translate("MainWindow", "Plot Filename:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Regression Settings:"))
        self.comboBoxRegressionSetting.setItemText(0, _translate("MainWindow", "Linear"))
        self.comboBoxRegressionSetting.setItemText(1, _translate("MainWindow", "Logistic"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

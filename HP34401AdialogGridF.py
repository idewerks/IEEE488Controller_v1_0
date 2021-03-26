# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HP34401AdialogGridF.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HP34401ADialog(object):
    def setupUi(self, HP34401ADialog):
        HP34401ADialog.setObjectName("HP34401ADialog")
        HP34401ADialog.resize(1920, 1080)
        HP34401ADialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        HP34401ADialog.setSizeGripEnabled(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(HP34401ADialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.statustextBrowser = QtWidgets.QTextBrowser(HP34401ADialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statustextBrowser.sizePolicy().hasHeightForWidth())
        self.statustextBrowser.setSizePolicy(sizePolicy)
        self.statustextBrowser.setMaximumSize(QtCore.QSize(600, 90))
        self.statustextBrowser.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.statustextBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.statustextBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statustextBrowser.setLineWidth(1)
        self.statustextBrowser.setObjectName("statustextBrowser")
        self.gridLayout_3.addWidget(self.statustextBrowser, 1, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(HP34401ADialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 70))
        self.lcdNumber.setMaximumSize(QtCore.QSize(800, 90))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setStyleSheet("background-color: rgb(15, 204, 12);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setMidLineWidth(2)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(16)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 1, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(HP34401ADialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(700, 850))
        self.frame_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 131);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(4)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(0, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.AutozeroLabel = QtWidgets.QLabel(self.frame_6)
        self.AutozeroLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.AutozeroLabel.setObjectName("AutozeroLabel")
        self.gridLayout_2.addWidget(self.AutozeroLabel, 3, 0, 1, 1)
        self.RangeCombobox = QtWidgets.QComboBox(self.frame_6)
        self.RangeCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.RangeCombobox.setObjectName("RangeCombobox")
        self.gridLayout_2.addWidget(self.RangeCombobox, 4, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.MathLabel = QtWidgets.QLabel(self.frame_6)
        self.MathLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.MathLabel.setObjectName("MathLabel")
        self.gridLayout_2.addWidget(self.MathLabel, 12, 0, 1, 1)
        self.TrigdelayLabel = QtWidgets.QLabel(self.frame_6)
        self.TrigdelayLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.TrigdelayLabel.setObjectName("TrigdelayLabel")
        self.gridLayout_2.addWidget(self.TrigdelayLabel, 16, 0, 1, 1)
        self.RangeLabel = QtWidgets.QLabel(self.frame_6)
        self.RangeLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.RangeLabel.setObjectName("RangeLabel")
        self.gridLayout_2.addWidget(self.RangeLabel, 4, 0, 1, 1)
        self.scaleLabel_2 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scaleLabel_2.setFont(font)
        self.scaleLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleLabel_2.setObjectName("scaleLabel_2")
        self.gridLayout_2.addWidget(self.scaleLabel_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 14, 1, 1, 1)
        self.ResolutionCombobox = QtWidgets.QComboBox(self.frame_6)
        self.ResolutionCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.ResolutionCombobox.setObjectName("ResolutionCombobox")
        self.gridLayout_2.addWidget(self.ResolutionCombobox, 5, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.ResolutionLabel = QtWidgets.QLabel(self.frame_6)
        self.ResolutionLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.ResolutionLabel.setObjectName("ResolutionLabel")
        self.gridLayout_2.addWidget(self.ResolutionLabel, 5, 0, 1, 1)
        self.FreqapertureCombobox = QtWidgets.QComboBox(self.frame_6)
        self.FreqapertureCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.FreqapertureCombobox.setObjectName("FreqapertureCombobox")
        self.gridLayout_2.addWidget(self.FreqapertureCombobox, 7, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.AcbwLabel = QtWidgets.QLabel(self.frame_6)
        self.AcbwLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.AcbwLabel.setObjectName("AcbwLabel")
        self.gridLayout_2.addWidget(self.AcbwLabel, 11, 0, 1, 1)
        self.PeriodapertureLabel = QtWidgets.QLabel(self.frame_6)
        self.PeriodapertureLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.PeriodapertureLabel.setObjectName("PeriodapertureLabel")
        self.gridLayout_2.addWidget(self.PeriodapertureLabel, 8, 0, 1, 1)
        self.NplcLabel = QtWidgets.QLabel(self.frame_6)
        self.NplcLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.NplcLabel.setObjectName("NplcLabel")
        self.gridLayout_2.addWidget(self.NplcLabel, 6, 0, 1, 1)
        self.FreqapertureLabel = QtWidgets.QLabel(self.frame_6)
        self.FreqapertureLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.FreqapertureLabel.setObjectName("FreqapertureLabel")
        self.gridLayout_2.addWidget(self.FreqapertureLabel, 7, 0, 1, 1)
        self.TriggerDelaySlider = QtWidgets.QSlider(self.frame_6)
        self.TriggerDelaySlider.setMinimumSize(QtCore.QSize(200, 25))
        self.TriggerDelaySlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.TriggerDelaySlider.setStyleSheet("background-color: rgb(3, 3, 3);")
        self.TriggerDelaySlider.setMaximum(3600)
        self.TriggerDelaySlider.setPageStep(1)
        self.TriggerDelaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.TriggerDelaySlider.setInvertedAppearance(False)
        self.TriggerDelaySlider.setInvertedControls(False)
        self.TriggerDelaySlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.TriggerDelaySlider.setTickInterval(360)
        self.TriggerDelaySlider.setObjectName("TriggerDelaySlider")
        self.gridLayout_2.addWidget(self.TriggerDelaySlider, 16, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.ImpedanceCombobox = QtWidgets.QComboBox(self.frame_6)
        self.ImpedanceCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.ImpedanceCombobox.setToolTipDuration(-1)
        self.ImpedanceCombobox.setObjectName("ImpedanceCombobox")
        self.gridLayout_2.addWidget(self.ImpedanceCombobox, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.ACbandwidthCombobox = QtWidgets.QComboBox(self.frame_6)
        self.ACbandwidthCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.ACbandwidthCombobox.setObjectName("ACbandwidthCombobox")
        self.gridLayout_2.addWidget(self.ACbandwidthCombobox, 11, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.SelectedTriggerdelayLabel = QtWidgets.QLabel(self.frame_6)
        self.SelectedTriggerdelayLabel.setScaledContents(False)
        self.SelectedTriggerdelayLabel.setObjectName("SelectedTriggerdelayLabel")
        self.gridLayout_2.addWidget(self.SelectedTriggerdelayLabel, 17, 1, 1, 1)
        self.PeriodapertureCombobox = QtWidgets.QComboBox(self.frame_6)
        self.PeriodapertureCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.PeriodapertureCombobox.setObjectName("PeriodapertureCombobox")
        self.gridLayout_2.addWidget(self.PeriodapertureCombobox, 8, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.ImpedanceLabel = QtWidgets.QLabel(self.frame_6)
        self.ImpedanceLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.ImpedanceLabel.setObjectName("ImpedanceLabel")
        self.gridLayout_2.addWidget(self.ImpedanceLabel, 2, 0, 1, 1)
        self.TrigsrcCombobox = QtWidgets.QComboBox(self.frame_6)
        self.TrigsrcCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.TrigsrcCombobox.setObjectName("TrigsrcCombobox")
        self.gridLayout_2.addWidget(self.TrigsrcCombobox, 13, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.TrigsrcLabel = QtWidgets.QLabel(self.frame_6)
        self.TrigsrcLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.TrigsrcLabel.setObjectName("TrigsrcLabel")
        self.gridLayout_2.addWidget(self.TrigsrcLabel, 13, 0, 1, 1)
        self.MathCombobox = QtWidgets.QComboBox(self.frame_6)
        self.MathCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.MathCombobox.setObjectName("MathCombobox")
        self.gridLayout_2.addWidget(self.MathCombobox, 12, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.NplcCombobox = QtWidgets.QComboBox(self.frame_6)
        self.NplcCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.NplcCombobox.setObjectName("NplcCombobox")
        self.gridLayout_2.addWidget(self.NplcCombobox, 6, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.AutozeroCombobox = QtWidgets.QComboBox(self.frame_6)
        self.AutozeroCombobox.setMinimumSize(QtCore.QSize(100, 25))
        self.AutozeroCombobox.setObjectName("AutozeroCombobox")
        self.gridLayout_2.addWidget(self.AutozeroCombobox, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setMinimumSize(QtCore.QSize(0, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.samplesSlider = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplesSlider.sizePolicy().hasHeightForWidth())
        self.samplesSlider.setSizePolicy(sizePolicy)
        self.samplesSlider.setMinimumSize(QtCore.QSize(350, 40))
        self.samplesSlider.setStyleSheet("background-color: rgb(3, 3, 3);")
        self.samplesSlider.setMaximum(1024)
        self.samplesSlider.setPageStep(1)
        self.samplesSlider.setProperty("value", 16)
        self.samplesSlider.setOrientation(QtCore.Qt.Horizontal)
        self.samplesSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.samplesSlider.setTickInterval(25)
        self.samplesSlider.setObjectName("samplesSlider")
        self.verticalLayout_2.addWidget(self.samplesSlider, 0, QtCore.Qt.AlignHCenter)
        self.sampledisplayLabel = QtWidgets.QLabel(self.frame)
        self.sampledisplayLabel.setObjectName("sampledisplayLabel")
        self.verticalLayout_2.addWidget(self.sampledisplayLabel, 0, QtCore.Qt.AlignHCenter)
        self.samplestartpushButton = QtWidgets.QPushButton(self.frame)
        self.samplestartpushButton.setMinimumSize(QtCore.QSize(300, 30))
        self.samplestartpushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.samplestartpushButton.setObjectName("samplestartpushButton")
        self.verticalLayout_2.addWidget(self.samplestartpushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.samplestoppushButton = QtWidgets.QPushButton(self.frame)
        self.samplestoppushButton.setMinimumSize(QtCore.QSize(300, 30))
        self.samplestoppushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.samplestoppushButton.setStyleSheet("")
        self.samplestoppushButton.setObjectName("samplestoppushButton")
        self.verticalLayout_2.addWidget(self.samplestoppushButton, 0, QtCore.Qt.AlignHCenter)
        self.samplestakenLabel = QtWidgets.QLabel(self.frame)
        self.samplestakenLabel.setMinimumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.samplestakenLabel.setFont(font)
        self.samplestakenLabel.setText("")
        self.samplestakenLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.samplestakenLabel.setObjectName("samplestakenLabel")
        self.verticalLayout_2.addWidget(self.samplestakenLabel, 0, QtCore.Qt.AlignHCenter)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setMinimumSize(QtCore.QSize(300, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar, 0, QtCore.Qt.AlignHCenter)
        self.savescanpushButton = QtWidgets.QPushButton(self.frame)
        self.savescanpushButton.setMinimumSize(QtCore.QSize(400, 30))
        self.savescanpushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.savescanpushButton.setToolTipDuration(-1)
        self.savescanpushButton.setCheckable(True)
        self.savescanpushButton.setChecked(False)
        self.savescanpushButton.setDefault(False)
        self.savescanpushButton.setFlat(False)
        self.savescanpushButton.setObjectName("savescanpushButton")
        self.verticalLayout_2.addWidget(self.savescanpushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(7, 142, 198);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.TWOpushButton = QtWidgets.QPushButton(self.frame_2)
        self.TWOpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.TWOpushButton.setCheckable(True)
        self.TWOpushButton.setObjectName("TWOpushButton")
        self.gridLayout.addWidget(self.TWOpushButton, 1, 2, 1, 1)
        self.ACIpushButton = QtWidgets.QPushButton(self.frame_2)
        self.ACIpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.ACIpushButton.setCheckable(True)
        self.ACIpushButton.setObjectName("ACIpushButton")
        self.gridLayout.addWidget(self.ACIpushButton, 0, 1, 1, 1)
        self.DCVpushButton = QtWidgets.QPushButton(self.frame_2)
        self.DCVpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.DCVpushButton.setCheckable(True)
        self.DCVpushButton.setChecked(True)
        self.DCVpushButton.setObjectName("DCVpushButton")
        self.gridLayout.addWidget(self.DCVpushButton, 1, 0, 1, 1)
        self.ACVpushButton = QtWidgets.QPushButton(self.frame_2)
        self.ACVpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.ACVpushButton.setCheckable(True)
        self.ACVpushButton.setObjectName("ACVpushButton")
        self.gridLayout.addWidget(self.ACVpushButton, 1, 1, 1, 1)
        self.CONpushButton = QtWidgets.QPushButton(self.frame_2)
        self.CONpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.CONpushButton.setCheckable(True)
        self.CONpushButton.setObjectName("CONpushButton")
        self.gridLayout.addWidget(self.CONpushButton, 1, 4, 1, 1)
        self.DCIpushButton = QtWidgets.QPushButton(self.frame_2)
        self.DCIpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.DCIpushButton.setCheckable(True)
        self.DCIpushButton.setObjectName("DCIpushButton")
        self.gridLayout.addWidget(self.DCIpushButton, 0, 0, 1, 1)
        self.DIOpushButton = QtWidgets.QPushButton(self.frame_2)
        self.DIOpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"alternate-background-color: rgb(0, 170, 255);\n"
"color: rgb(85, 255, 255);")
        self.DIOpushButton.setCheckable(True)
        self.DIOpushButton.setObjectName("DIOpushButton")
        self.gridLayout.addWidget(self.DIOpushButton, 0, 4, 1, 1)
        self.FREpushButton = QtWidgets.QPushButton(self.frame_2)
        self.FREpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.FREpushButton.setCheckable(True)
        self.FREpushButton.setObjectName("FREpushButton")
        self.gridLayout.addWidget(self.FREpushButton, 1, 3, 1, 1)
        self.PERpushButton = QtWidgets.QPushButton(self.frame_2)
        self.PERpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.PERpushButton.setCheckable(True)
        self.PERpushButton.setObjectName("PERpushButton")
        self.gridLayout.addWidget(self.PERpushButton, 0, 3, 1, 1)
        self.FWOpushButton = QtWidgets.QPushButton(self.frame_2)
        self.FWOpushButton.setStyleSheet("background-color: rgb(4, 69, 115);\n"
"color: rgb(85, 255, 255);")
        self.FWOpushButton.setCheckable(True)
        self.FWOpushButton.setObjectName("FWOpushButton")
        self.gridLayout.addWidget(self.FWOpushButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.hp34401aTitlelabel = QtWidgets.QLabel(HP34401ADialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hp34401aTitlelabel.setFont(font)
        self.hp34401aTitlelabel.setStyleSheet("color: rgb(85, 170, 255);")
        self.hp34401aTitlelabel.setTextFormat(QtCore.Qt.RichText)
        self.hp34401aTitlelabel.setScaledContents(False)
        self.hp34401aTitlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hp34401aTitlelabel.setObjectName("hp34401aTitlelabel")
        self.gridLayout_3.addWidget(self.hp34401aTitlelabel, 2, 0, 1, 1)
        self.ExitpushButton = QtWidgets.QPushButton(HP34401ADialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitpushButton.sizePolicy().hasHeightForWidth())
        self.ExitpushButton.setSizePolicy(sizePolicy)
        self.ExitpushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.ExitpushButton.setMaximumSize(QtCore.QSize(800, 90))
        self.ExitpushButton.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.ExitpushButton.setObjectName("ExitpushButton")
        self.gridLayout_3.addWidget(self.ExitpushButton, 2, 1, 1, 1)
        self.plotWidget = PlotWidget(HP34401ADialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.plotWidget.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_3.addWidget(self.plotWidget, 0, 1, 1, 1)

        self.retranslateUi(HP34401ADialog)
        QtCore.QMetaObject.connectSlotsByName(HP34401ADialog)

    def retranslateUi(self, HP34401ADialog):
        _translate = QtCore.QCoreApplication.translate
        HP34401ADialog.setWindowTitle(_translate("HP34401ADialog", "HP Agilent 34401A Instrument Module"))
        self.AutozeroLabel.setText(_translate("HP34401ADialog", "AutoZero"))
        self.MathLabel.setText(_translate("HP34401ADialog", "Math"))
        self.TrigdelayLabel.setText(_translate("HP34401ADialog", "Trigger Delay(0-3600Sec)"))
        self.RangeLabel.setText(_translate("HP34401ADialog", "Range (V)"))
        self.scaleLabel_2.setText(_translate("HP34401ADialog", "SETTINGS"))
        self.ResolutionLabel.setText(_translate("HP34401ADialog", "Resolution (V)"))
        self.AcbwLabel.setText(_translate("HP34401ADialog", "AC Bandwidth"))
        self.PeriodapertureLabel.setText(_translate("HP34401ADialog", "Period Aperture"))
        self.NplcLabel.setText(_translate("HP34401ADialog", "NPLC Cycles"))
        self.FreqapertureLabel.setText(_translate("HP34401ADialog", "Freq Aperture"))
        self.ImpedanceCombobox.setToolTip(_translate("HP34401ADialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#00007f;\">Impedance Selector </span></p><p><span style=\" color:#00007f;\">Auto Off Zin=10Mohm all DCV Ranges</span></p><p><span style=\" color:#00007f;\">Auto On Zin=&gt;10Gohm for 100mv, 1v, &amp; 10v DCV Ranges</span></p></body></html>"))
        self.SelectedTriggerdelayLabel.setText(_translate("HP34401ADialog", "0"))
        self.ImpedanceLabel.setText(_translate("HP34401ADialog", "Impedance"))
        self.TrigsrcLabel.setText(_translate("HP34401ADialog", "Trigger Source"))
        self.AutozeroCombobox.setToolTip(_translate("HP34401ADialog", "<html><head/><body><p><span style=\" color:#00007f;\">Auto-Zero: Off=NO AZ, On=AZ/sample, Once= Once at Scan Start</span></p></body></html>"))
        self.sampledisplayLabel.setText(_translate("HP34401ADialog", "TARGET SAMPLES"))
        self.samplestartpushButton.setText(_translate("HP34401ADialog", "SAMPLING START"))
        self.samplestoppushButton.setText(_translate("HP34401ADialog", "SAMPLING STOP"))
        self.savescanpushButton.setText(_translate("HP34401ADialog", "SAVE SCAN as CSV"))
        self.TWOpushButton.setText(_translate("HP34401ADialog", "2-wire Ohms"))
        self.ACIpushButton.setText(_translate("HP34401ADialog", "AC Current"))
        self.DCVpushButton.setText(_translate("HP34401ADialog", "DC Voltage"))
        self.ACVpushButton.setText(_translate("HP34401ADialog", "AC Voltage"))
        self.CONpushButton.setText(_translate("HP34401ADialog", "Continuity"))
        self.DCIpushButton.setText(_translate("HP34401ADialog", "DC Current"))
        self.DIOpushButton.setText(_translate("HP34401ADialog", "Diode"))
        self.FREpushButton.setText(_translate("HP34401ADialog", "Frequency"))
        self.PERpushButton.setText(_translate("HP34401ADialog", "Period"))
        self.FWOpushButton.setText(_translate("HP34401ADialog", "4-wire Ohms"))
        self.hp34401aTitlelabel.setText(_translate("HP34401ADialog", "HP 34401A Instrument"))
        self.ExitpushButton.setText(_translate("HP34401ADialog", "Exit"))
from pyqtgraph import PlotWidget

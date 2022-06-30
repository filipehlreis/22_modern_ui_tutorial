# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_22_modern_tutorialQThFWq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 609)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer, #left_center_SubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton {\n"
"	text-align: left;\n"
"	padding: 5px 10px 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	margin: 1px 0px;\n"
"\n"
"}\n"
"#leftMenuSubContainer QPushButton:hover {\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_6, #frame_8, #popupNotificationSubContainer{\n"
"	background-color: #16191d;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#closeBtn, #minimizeBtn, #restor"
                        "eBtn{\n"
"	text-align: center;\n"
"	padding: 4px 4px 4px 4px;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"\n"
"}\n"
"#minimizeBtn:hover, #restoreBtn:hover {\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#closeBtn:hover {\n"
"	background-color: #8B2635;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 8, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather-WHITE/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))
        self.menuBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy1)
        self.homeBtn.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.homeBtn.setFont(font)
        self.homeBtn.setLayoutDirection(Qt.LeftToRight)
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(u"background-color: #1F232A;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/feather-WHITE/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/feather-WHITE/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.waitingBtn = QPushButton(self.frame_2)
        self.waitingBtn.setObjectName(u"waitingBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/feather-WHITE/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.waitingBtn.setIcon(icon3)
        self.waitingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.waitingBtn)

        self.bomBtn = QPushButton(self.frame_2)
        self.bomBtn.setObjectName(u"bomBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/feather-WHITE/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bomBtn.setIcon(icon4)
        self.bomBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.bomBtn)

        self.pickplaceBtn = QPushButton(self.frame_2)
        self.pickplaceBtn.setObjectName(u"pickplaceBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/feather-WHITE/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pickplaceBtn.setIcon(icon5)
        self.pickplaceBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.pickplaceBtn)

        self.forecastingBtn = QPushButton(self.frame_2)
        self.forecastingBtn.setObjectName(u"forecastingBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/feather-WHITE/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.forecastingBtn.setIcon(icon6)
        self.forecastingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.forecastingBtn)

        self.kitsBtn = QPushButton(self.frame_2)
        self.kitsBtn.setObjectName(u"kitsBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/feather-WHITE/package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.kitsBtn.setIcon(icon7)
        self.kitsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.kitsBtn)

        self.convertBtn = QPushButton(self.frame_2)
        self.convertBtn.setObjectName(u"convertBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/feather-WHITE/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.convertBtn.setIcon(icon8)
        self.convertBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.convertBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/feather-WHITE/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon9)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/feather-WHITE/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon10)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/feather-WHITE/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon11)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.left_center_Container = QWidget(self.centralwidget)
        self.left_center_Container.setObjectName(u"left_center_Container")
        self.verticalLayout_26 = QVBoxLayout(self.left_center_Container)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.left_center_SubContainer = QWidget(self.left_center_Container)
        self.left_center_SubContainer.setObjectName(u"left_center_SubContainer")
        self.left_center_SubContainer.setMinimumSize(QSize(10, 0))
        self.left_center_SubContainer.setMaximumSize(QSize(10, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.left_center_SubContainer)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.left_center_SubContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_11)


        self.verticalLayout_26.addWidget(self.left_center_SubContainer)


        self.horizontalLayout.addWidget(self.left_center_Container)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.centerMenuContainer.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.centerMenuSubContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_6)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/feather-WHITE/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon12)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.widget = QWidget(self.centerMenuSubContainer)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_6.addWidget(self.widget)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setMinimumSize(QSize(0, 0))
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_7 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.settingsPage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_8 = QVBoxLayout(self.informationPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.informationPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.informationPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.helpPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 30))
        self.label_5.setPixmap(QPixmap(u":/images/assets/logo_construction.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_5)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/feather-WHITE/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon13)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_5)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/feather-WHITE/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon14)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_5)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/feather-WHITE/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon15)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/feather-WHITE/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon16)

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/feather-WHITE/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon17)

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/feather-WHITE/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon18)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.mainBodyContent.setMinimumSize(QSize(500, 419))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_16 = QVBoxLayout(self.homePage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.importCsvOmieBtn = QPushButton(self.homePage)
        self.importCsvOmieBtn.setObjectName(u"importCsvOmieBtn")

        self.verticalLayout_16.addWidget(self.importCsvOmieBtn)

        self.exportCsvOmieToHdBtn = QPushButton(self.homePage)
        self.exportCsvOmieToHdBtn.setObjectName(u"exportCsvOmieToHdBtn")

        self.verticalLayout_16.addWidget(self.exportCsvOmieToHdBtn)

        self.label_10 = QLabel(self.homePage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)

        self.mainPages.addWidget(self.homePage)
        self.dataPage = QWidget()
        self.dataPage.setObjectName(u"dataPage")
        self.verticalLayout_17 = QVBoxLayout(self.dataPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_12 = QFrame(self.dataPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(2)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tableWidget = QTableWidget(self.frame_12)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(1, 6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(1, 7, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(2, 5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(2, 6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(2, 7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setItem(3, 4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(3, 5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(3, 6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(3, 7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setItem(4, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(4, 5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setItem(4, 6, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(4, 7, __qtablewidgetitem52)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        font3.setPointSize(10)
        self.tableWidget.setFont(font3)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #30B28C;\n"
"	font: bold 10pt \"Arial\";\n"
"\n"
"    border: solid;\n"
"    height: 30px;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_14.addWidget(self.tableWidget)


        self.verticalLayout_17.addWidget(self.frame_12)

        self.label_11 = QLabel(self.dataPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)

        self.mainPages.addWidget(self.dataPage)
        self.waitingPage = QWidget()
        self.waitingPage.setObjectName(u"waitingPage")
        self.verticalLayout_18 = QVBoxLayout(self.waitingPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.waitingPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.mainPages.addWidget(self.waitingPage)
        self.bomPage = QWidget()
        self.bomPage.setObjectName(u"bomPage")
        self.verticalLayout_21 = QVBoxLayout(self.bomPage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_16 = QLabel(self.bomPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_16)

        self.mainPages.addWidget(self.bomPage)
        self.pickplacePage = QWidget()
        self.pickplacePage.setObjectName(u"pickplacePage")
        self.verticalLayout_25 = QVBoxLayout(self.pickplacePage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_17 = QLabel(self.pickplacePage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_17)

        self.mainPages.addWidget(self.pickplacePage)
        self.forecastingPage = QWidget()
        self.forecastingPage.setObjectName(u"forecastingPage")
        self.verticalLayout_24 = QVBoxLayout(self.forecastingPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_18 = QLabel(self.forecastingPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_18)

        self.mainPages.addWidget(self.forecastingPage)
        self.kitsPage = QWidget()
        self.kitsPage.setObjectName(u"kitsPage")
        self.verticalLayout_23 = QVBoxLayout(self.kitsPage)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_19 = QLabel(self.kitsPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_19)

        self.mainPages.addWidget(self.kitsPage)
        self.convertPage = QWidget()
        self.convertPage.setObjectName(u"convertPage")
        self.verticalLayout_22 = QVBoxLayout(self.convertPage)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_20 = QLabel(self.convertPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_20)

        self.mainPages.addWidget(self.convertPage)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 401))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon12)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_13 = QVBoxLayout(self.profilePage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.profilePage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.profilePage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_14 = QVBoxLayout(self.morePage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.morePage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setFrameShadow(QFrame.Sunken)
        self.label_9.setTextFormat(Qt.PlainText)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.morePage)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_14.setFont(font4)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/feather-WHITE/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon19)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        font5 = QFont()
        font5.setPointSize(10)
        self.sizeGrip.setFont(font5)
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_21 = QLabel(self.sizeGrip)
        self.label_21.setObjectName(u"label_21")
        font6 = QFont()
        font6.setPointSize(7)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_21.setFont(font6)
        self.label_21.setLayoutDirection(Qt.RightToLeft)
        self.label_21.setStyleSheet(u"color: #30B28C;\n"
"text-align: center-center,")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_21)


        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"P\u00e1gina Inicial", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"P\u00e1gina Inicial", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Banco de Dados", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Banco de Dados", None))
#if QT_CONFIG(tooltip)
        self.waitingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Aguardando Padroniza\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.waitingBtn.setText(QCoreApplication.translate("MainWindow", u"Aguardando Padroniza\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.bomBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Listas de Materiais", None))
#endif // QT_CONFIG(tooltip)
        self.bomBtn.setText(QCoreApplication.translate("MainWindow", u"Listas de Materiais", None))
#if QT_CONFIG(tooltip)
        self.pickplaceBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pick & Place", None))
#endif // QT_CONFIG(tooltip)
        self.pickplaceBtn.setText(QCoreApplication.translate("MainWindow", u"Pick && Place", None))
#if QT_CONFIG(tooltip)
        self.forecastingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Previs\u00e3o de Consumo", None))
#endif // QT_CONFIG(tooltip)
        self.forecastingBtn.setText(QCoreApplication.translate("MainWindow", u"Previs\u00e3o de Consumo", None))
#if QT_CONFIG(tooltip)
        self.kitsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"KITs", None))
#endif // QT_CONFIG(tooltip)
        self.kitsBtn.setText(QCoreApplication.translate("MainWindow", u"KITs", None))
#if QT_CONFIG(tooltip)
        self.convertBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Convers\u00f5es de Medidas", None))
#endif // QT_CONFIG(tooltip)
        self.convertBtn.setText(QCoreApplication.translate("MainWindow", u"Convers\u00f5es de Medidas", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ajuda", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Code Description Manager", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.importCsvOmieBtn.setText(QCoreApplication.translate("MainWindow", u"Importar arquivo EXCEL do OMIE", None))
        self.exportCsvOmieToHdBtn.setText(QCoreApplication.translate("MainWindow", u"Gravar CSV tratado no HD", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o Simplificada", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o Completa", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Caixa", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Prateleira", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Corredor", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"5", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Ativo", None));
        ___qtablewidgetitem14 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"660649", None));
        ___qtablewidgetitem15 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"RESISTOR SMD 0603 82R 5%", None));
        ___qtablewidgetitem16 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"RESISTOR SMD 0603 82R 5% (PN: CR0603-JW-820ELF) (PN: RK73B1JTTDD820J) (PN: CRGCQ0603F82R) (PN: RC0603JR-0782RL)", None));
        ___qtablewidgetitem17 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"5000", None));
        ___qtablewidgetitem18 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem19 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem20 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem21 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Ativo", None));
        ___qtablewidgetitem22 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"660630", None));
        ___qtablewidgetitem23 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"CAPACITOR CER\u00c2MICO SMD 0603 560pF 100V 5% C0G", None));
        ___qtablewidgetitem24 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CAPACITOR CER\u00c2MICO SMD 0603 560pF 100V 5% C0G (PN: C1608C0G2A561J080AA) (PN: CC0603JRNPO0BN561) (PN: 0603N561J101CT)", None));
        ___qtablewidgetitem25 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"7000", None));
        ___qtablewidgetitem26 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem27 = self.tableWidget.item(1, 6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem28 = self.tableWidget.item(1, 7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem29 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Ativo", None));
        ___qtablewidgetitem30 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"660646", None));
        ___qtablewidgetitem31 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"MICROCONTROLADOR (PN: STM32G070RBT6)", None));
        ___qtablewidgetitem32 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"MICROCONTROLADOR (PN: STM32G070RBT6)", None));
        ___qtablewidgetitem33 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem34 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem35 = self.tableWidget.item(2, 6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem36 = self.tableWidget.item(2, 7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem37 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Ativo", None));
        ___qtablewidgetitem38 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"660488", None));
        ___qtablewidgetitem39 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"RESISTOR SMD 0603 470K 5%", None));
        ___qtablewidgetitem40 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"RESISTOR SMD 0603 470K 5% (PN: CR0603-JW-474ELF) (PN: AC0603JR-07470KL) (PN: RK73B1JTTD474J) (PN: ERJ-3GEYJ474V)", None));
        ___qtablewidgetitem41 = self.tableWidget.item(3, 4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"10000", None));
        ___qtablewidgetitem42 = self.tableWidget.item(3, 5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem43 = self.tableWidget.item(3, 6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem44 = self.tableWidget.item(3, 7)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem45 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Inativo", None));
        ___qtablewidgetitem46 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"772892", None));
        ___qtablewidgetitem47 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"RESISTOR SMD 0805 510mR 1% 1/4W", None));
        ___qtablewidgetitem48 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"RESISTOR SMD 0805 510mR 1% 1/4W (PN: KDV08DR510ET\u200e) (PN: ERJ-6DQFR51V) (PN: RL0805FR-7W0R51L)", None));
        ___qtablewidgetitem49 = self.tableWidget.item(4, 4)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"800", None));
        ___qtablewidgetitem50 = self.tableWidget.item(4, 5)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem51 = self.tableWidget.item(4, 6)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem52 = self.tableWidget.item(4, 7)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Data Base", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Aguardando Padroniza\u00e7\u00e3o", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Lista de Materiais", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Pick & Place", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Previs\u00e3o de Consumo", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"KITs", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Convers\u00e3o de Unidades", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More ...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Filipe Henrique Leite dos Reis - Engenheiro Eletr\u00f4nico 2022", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"o", None))
    # retranslateUi


# ########################################################################### #
# 22 MODERN UI
# QT GUI BY SPINN TV(YOUTUBE)
# ########################################################################### #

# ########################################################################### #
# IMPORTS
# ########################################################################### #
import sys
import os
# ########################################################################### #
# IMPORT GUI GILE
from ui_interface_22_modern_tutorial import *
# ########################################################################### #


########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


# ########################################################################### #
# MAIN WINDOW CLASS
# ########################################################################### #


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        # APPLY JSON STYLESHEET
        #######################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        #######################################################################

        # ################################################################### #
        # show window
        # ################################################################### #
        self.show()

        # EXPAND CENTER MENU WIDGET SIZE
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
    

        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())


        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())


# ########################################################################### #
# execute app
# ########################################################################### #
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# ########################################################################### #
# END
# ########################################################################### #

# ########################################################################### #
# 22 MODERN UI
# QT GUI BY SPINN TV(YOUTUBE)
# ########################################################################### #

# ########################################################################### #
# IMPORTS
# ########################################################################### #
import sys
import os
from codigo.functions_program import read_omie_sheet, export_excel_sheet_omie
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
        self.ui.settingsBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET
        self.ui.closeCenterMenuBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(
            lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(
            lambda: self.ui.rightMenuContainer.expandMenu())

        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(
            lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(
            lambda: self.ui.popupNotificationContainer.collapseMenu())

        # BUTTONS
        self.ui.importCsvOmieBtn.clicked.connect(
            lambda: read_omie_sheet()
        )

        self.ui.exportCsvOmieToHdBtn.clicked.connect(
            lambda: export_excel_sheet_omie()
        )


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

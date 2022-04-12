########################################################################
## 
########################################################################

########################################################################
## IMPORTS
########################################################################
########################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# IMPORT QTSASS
import qtsass
########################################################################
# IMPORT OS
import os
import shutil

from . colorsystem import CreateColorVariable,Dark,Light
from . SvgToPngIcons import NewIconsGenerator
########################################################################
## IMPORT WORKER
########################################################################
from .. WidgetsWorker import Worker, WorkerResponse

settings = QSettings()



########################################################################
## COMPILE STYLESHEET CLASS
########################################################################
class CompileStyleSheet():
    def __init__(self, parent=None):
        super(CompileStyleSheet, self).__init__(parent)      

        # sass_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.scss'))
        # css_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.css'))

        

    ########################################################################
    ## APPLY COMPILED STYLESHEET
    ########################################################################
    def applyCompiledSass(self):
        qcss_folder = os.path.abspath(os.path.join(os.getcwd(), 'QSS'))
        if not os.path.exists(qcss_folder):
            os.makedirs(qcss_folder)

        main_sass_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/main.scss'))
        styles_sass_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/_styles.scss'))
        css_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/main.css'))

        variablesFile = CreateColorVariable.CreateVariables(self)

        if not os.path.exists(main_sass_path):   
            shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.scss')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))  

        if not os.path.exists(styles_sass_path):   
            shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), '_styles.scss')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))  

        default_scss_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/defaultStyle.scss'))
        if not os.path.exists(default_scss_path):   
            f = open(default_scss_path, 'w')
            print(f"""
            //===================================================//
            // FILE AUTO-GENERATED. PUT YOUR DEFAULT STYLES HERE. 
            // THESE STYLES WILL OVERIDE THE THEME STYLES
            //====================================================//
            
            //===================================================//
            // END //
            //====================================================//
            """, file=f)

            f.close()

        qtsass.compile_filename(main_sass_path, css_path)
        
        with open(css_path,"r") as css:
            self.setStyleSheet(css.read())


        ########################################################################
        ## GENERATE NEW ICONS
        # START WORKER
        iconsWorker = Worker(self.compileSassTheme)
        iconsWorker.signals.result.connect(WorkerResponse.print_output)
        iconsWorker.signals.finished.connect(self.restart)
        iconsWorker.signals.progress.connect(self.sassCompilationProgress)

        color = CreateColorVariable.getCurrentThemeInfo(self)
        normal_color = str(color["icons-color"])
        # print(settings.value("ICONS-COLOR"), normal_color)
        if not settings.value("ICONS-COLOR") == normal_color and color["icons-color"] is not None:        
            # Execute
            self.customWidgetsThreadpool.start(iconsWorker)
        

########################################################################
## ==>END
########################################################################


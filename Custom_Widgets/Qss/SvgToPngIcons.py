import cairosvg
import codecs
import os
import sys
import shutil
from urllib.parse import urlparse
import __main__


from . colorsystem import *

settings = QSettings()

class NewIconsGenerator():
    """docstring for NewIconsGenerator"""
    def __init__(self, arg):
        super(NewIconsGenerator, self).__init__()
        self.arg = arg

    def generateNewIcons(self, progress_callback):  
        # Files folder
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'icons/original_svg')
        list_of_files = []
        iconsFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/Icons'))

        color = CreateColorVariable.getCurrentThemeInfo(self)

        svg_color = "#fff"
        # print(color)
        normal_color = str(color["icons-color"])
        # print(normal_color)
        focused_color = adjust_lightness(normal_color, 1.5)
        disabled_color = adjust_lightness(normal_color, .5)

        if not settings.value("ICONS-COLOR") == normal_color and color["icons-color"] is not None:
            print("Current icons color ", settings.value("ICONS-COLOR"), "New icons color", normal_color)

            print("Generating icons for your theme, please wait. This may take long")

            for root, dirs, files in os.walk(filename):
                for file in files:
                    list_of_files.append(os.path.join(root,file))

            totalIcons = len(list_of_files)
            for name in list_of_files:
                # Create normal icons
                with codecs.open(name, encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    newSVG = content.replace(svg_color, normal_color)
                    newBytes = str.encode(newSVG)

                    name_2 =  os.path.basename(urlparse(name).path).replace(".svg", ".png")
                    
                    if not os.path.exists(iconsFolder):
                        os.makedirs(iconsFolder)

                    filename = os.path.abspath(os.path.join(iconsFolder, name_2))
                    try:
                        # Convert each SVG icon to png
                        cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                        # print(filename)
                        # a = urlparse(url)
                        # print(os.path.basename(a.path))
                        pass
                    except Exception as e:
                        print(e)
                        pass

                # Create focus icons
                with codecs.open(name, encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    newSVG = content.replace(svg_color, focused_color)
                    newBytes = str.encode(newSVG)

                    name_2 =  os.path.basename(urlparse(name).path).replace(".svg", "_focus.png")
                    
                    if not os.path.exists(iconsFolder):
                        os.makedirs(iconsFolder)

                    filename = os.path.abspath(os.path.join(iconsFolder, name_2))
                    try:
                        # Convert each SVG icon to png
                        cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                        # print(filename)
                        # a = urlparse(url)
                        # print(os.path.basename(a.path))
                        pass
                    except Exception as e:
                        print(e)
                        pass

                # Create disabled icons
                with codecs.open(name, encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    newSVG = content.replace(svg_color, disabled_color)
                    newBytes = str.encode(newSVG)

                    name_2 =  os.path.basename(urlparse(name).path).replace(".svg", "_disabled.png")
                    
                    if not os.path.exists(iconsFolder):
                        os.makedirs(iconsFolder)

                    filename = os.path.abspath(os.path.join(iconsFolder, name_2))
                    try:
                        # Convert each SVG icon to png
                        cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                        # print(filename)
                        # a = urlparse(url)
                        # print(os.path.basename(a.path))
                    except Exception as e:
                        print(e)
                        

                    # EMMIT PROGRESS VALUE
                    progress_callback.emit(int((list_of_files.index(name)/totalIcons) * 100))
                    # print(int((list_of_files.index(name)/totalIcons) * 100), "% Done")

            # Check resource file
            resource_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/QSS_Resources.qrc'))
            if not os.path.exists(resource_path):   
                shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'QSS_Resources.qrc')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))  
            py_resource_path = resource_path.replace(".qrc", ".py")
            py_resource_path = py_resource_path.replace("QSS/", "")
            py_resource_path = py_resource_path.replace("QSS_Resources", "QSS_Resources_rc")
            # Convert qrc to py
            try:
                os.system("pyrcc5 '"+resource_path+"' -o '"+py_resource_path+"'")
                settings.setValue("ICONS-COLOR", normal_color)
                # Restart
                # os.execl(sys.executable, os.path.abspath(__main__.__file__), *sys.argv) 
            except Exception as e:
                raise e   


            


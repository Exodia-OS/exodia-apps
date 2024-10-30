#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

import os
import subprocess
from datetime import datetime
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget


def getExodiaVersion():
    # Run bash command to get the version
    try:
        version = subprocess.check_output(
            "if [[ -e '/version' ]]; then echo v$(cut -d'.' -f1 /version).$(cut -d'.' -f2 /version); else echo 'rolling'; fi",
            shell=True
        ).decode('utf-8').strip()
        return version
    except subprocess.CalledProcessError:
        return "rolling"


class ButtonContent:
    def __init__(self, internal_window):
        self.version = None
        self.internal_window = internal_window
        self.predator_font = self.loadPredatorFont()
        self.version = self.getExodiaVersion()
        self.current_year = datetime.now().year  # Get the current year

    def loadPredatorFont(self):
        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load predator font.")
            return None
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            return QFont(font_family, 30, QFont.Bold)

    def clearButtons(self):
        # Remove all button widgets from the internal window
        for i in reversed(range(self.internal_window.layout().count())):
            widget = self.internal_window.layout().itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def displayWelcomeContent(self):
        # Define welcome text HTML content
        welcome_text = """
        <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
            <h2 style="color: #00C8B0; font-size: 40px; margin-bottom: 15px;">Welcome to Exodia OS</h2>
            <p style="font-size: 18px">
                A highly customized Arch-based Linux distribution for all cybersecurity fields.
                <br/>
                It comes with other special editions as well.
                <br/>
                We advise cleaning the computer with GParted before installing.
            </p>
        </div>
        """.format(self.predator_font.family())

        # Display the welcome text in the internal window
        self.internal_window.updateContent(welcome_text)

        # Check if internal_window already has a layout, and if not, set a QVBoxLayout
        if not self.internal_window.layout():
            self.internal_window.setLayout(QVBoxLayout())

        # Create button containers
        button_container_1 = QWidget()
        button_layout_1 = QHBoxLayout(button_container_1)
        button_container_2 = QWidget()
        button_layout_2 = QHBoxLayout(button_container_2)

        # Define button labels for each row
        first_row_labels = ["GParted", "Exodia Assistant", "Exodia Installer"]
        second_row_labels = ["About Exodia", "Wiki", "Docs", "News"]

        # Create first row of buttons with smaller size
        for label in first_row_labels:
            button = QPushButton(label)
            button.setFixedSize(170, 40)  # Set smaller button size
            button.setStyleSheet("background-color: #00B0C8; color: black; font-size: 20px; padding: 5px;")
            button.clicked.connect(lambda _, cmd=label: self.runCommand(cmd))  # Connect button to command
            button_layout_1.addWidget(button)

        # Create second row of buttons with smaller size
        for label in second_row_labels:
            button = QPushButton(label)
            button.setFixedSize(170, 40)  # Set smaller button size
            button.setStyleSheet("background-color: #00B0C8; color: black; font-size: 20px; padding: 5px;")
            button.clicked.connect(lambda _, cmd=label: self.runCommand(cmd))  # Connect button to command
            button_layout_2.addWidget(button)

        # Add the button containers to the internal window's layout
        self.internal_window.layout().addWidget(button_container_1)
        self.internal_window.layout().addWidget(button_container_2)

    def runCommand(self, command):
        if command == "GParted":
            subprocess.Popen(["gparted"])
        elif command == "Exodia Assistant":
            subprocess.Popen(["exodia-assistant"])
        elif command == "Exodia Installer":
            subprocess.Popen(["/etc/calamares/launch.sh"])
        elif command == "About Exodia":
            subprocess.Popen(["about-exodia-os"])
        elif command == "Wiki":
            subprocess.Popen(["xdg-open", "https://exodia-os.github.io/wiki/"])
        elif command == "Docs":
            subprocess.Popen(["xdg-open", "https://exodia-os.github.io/wiki/docs/intro"])
        elif command == "News":
            subprocess.Popen(["xdg-open", "https://exodia-os.github.io/wiki/news"])


    def displayKeybindingContent(self):
        self.clearButtons()  # Clear previous buttons
        keybinding_text = """
        <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Keybinding</h1>
        
                <h2 align="center" >Bspwm</h2>
              
                <div style="align: center; padding: 20px">
                    <img src="/usr/share/exodia/exodia-welcome/imgs/Keybinding/bspwm.png">
                </div>
                
            </div>
        """.format(self.predator_font.family())
        self.internal_window.updateContent(keybinding_text)

    def getExodiaVersion(self):
        # Run bash command to get the version
        try:
            version = subprocess.check_output(
                "if [[ -e '/version' ]]; then echo v$(cut -d'.' -f1 /version).$(cut -d'.' -f2 /version); else echo 'rolling'; fi",
                shell=True
            ).decode('utf-8').strip()
            return version
        except subprocess.CalledProcessError:
            return "rolling"

    def displayDevelopersContent(self):
        self.clearButtons()  # Clear previous buttons
        developers_text = f"""
            
            <div style="font-family: {self.predator_font.family()}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px;">
                                
                <table style="margin: 20px 0;">
                    <tr>
                        
                        <td style="text-align: left;">
                            <img src="/usr/share/exodia/exodia-welcome/imgs/creator/Ozil.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%;">
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #FFFFFF; font-size: 28px; margin: 0;">Mahmoud Mohamed</h2>
                            <br/>
                            <h4 style="color: #00C8B0; margin-top: 0px;">DevOps/MLOps Engineer</h4>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h4 style="color: #00C8B0; font-size: 28px;">Ozil</h4>
                        </td>
                        
                    </tr>
                    
                </table>
                
                <p style="font-size: 20px; color: #00C8B0; margin-bottom: 10px;">Copyrights:</p>
                
                <p style="font-size: 18px;">
                
                        00xWolf | Cyb3rTh1eveZ Team  﫥  Copyrights 2022-{self.current_year}
                
                </p>
                
                <p style="font-size: 20px; color: #00C8B0; margin-bottom: 10px;">About Creator:</p>
                
                <p style="font-size: 18px;">
                
                        I'm a Junior DevOps/MLOps Engineer with a background in Information Technology from the Faculty of Computers and Artificial Intelligence at Cairo University. 
                        I am an experienced Linux enthusiast with expertise in cybersecurity, including PNPT certification, mobile and web app penetration testing, and general security. 
                        I am actively learning machine learning and am a strong advocate for Free and Open Source Software (FOSS), contributing to various projects. 
                        Additionally, I am a hardware enthusiast and an Acer Predator fanboy.
                        
                </p>
                
                <br>
                
                <p style="font-size: 20px; color: #00C8B0; margin-bottom: 10px;">Version: {self.version}</p>
                
            </div>
        """
        self.internal_window.updateContent(developers_text)

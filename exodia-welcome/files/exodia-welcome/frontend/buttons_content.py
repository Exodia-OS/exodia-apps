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
import shutil
from datetime import datetime

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget


def loadPredatorFont():
    # Load the font from the Fonts directory
    font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        print("Failed to load predator font.")
        return None
    else:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        return QFont(font_family, 30, QFont.Bold)

def runCommand(command):
    # Dictionary of commands with their corresponding executables and URLs
    commands = {
        "Run GParted": ["gparted"],
        "Exodia OS Assistant": ["exodia-assistant"],
        "Exodia OS Installer": ["/etc/calamares/launch.sh"],
        "About Exodia": ["about-exodia-os"],
        "Wiki": ["xdg-open", "https://exodia-os.github.io/wiki"],
        "Docs": ["xdg-open", "https://exodia-os.github.io/wiki/docs/intro"],
        "News": ["xdg-open", "https://exodia-os.github.io/wiki/news"],
        "Discord": ["xdg-open", "https://discord.gg/wPDyfR5AV9"],
        "Reddit": ["xdg-open", "https://www.reddit.com/r/ExodiaOS"],
        "Telegram": ["xdg-open", "https://t.me/exodiaos"],
        "GitHub": ["xdg-open", "https://github.com/Exodia-OS"],
        "YouTube": ["xdg-open", "https://www.youtube.com/@mahmoudmohammed00xwolf88/videos"]
    }

    # Get the command details
    cmd_details = commands.get(command)

    if not cmd_details:
        print(f"Command '{command}' not recognized.")
        return

    executable = cmd_details[0]

    # Check if the executable is valid (file exists or is in PATH)
    if shutil.which(executable) or (executable.startswith('/') and os.path.isfile(executable)):
        try:
            subprocess.Popen(cmd_details)
        except Exception as e:
            print(f"Failed to execute '{command}': {e}")
    else:
        print(f"Command '{executable}' not found. Please install it or check the path.")



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
        self.predator_font = loadPredatorFont()
        self.version = getExodiaVersion()
        self.current_year = datetime.now().year  # Get the current year

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
            <h4 style="color: #00C8B0; font-size: 20px; margin-bottom: 15px;">We advise cleaning the computer with GParted before installing.</h4>
            <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/>
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
            first_row_labels = ["Run GParted", "Exodia OS Assistant", "Exodia OS Installer"]
            second_row_labels = ["About Exodia", "Wiki", "Docs", "News"]

            # Create first row of buttons with smaller size
            for label in first_row_labels:
                button = QPushButton(label)
                button.setFixedSize(220, 40)  # Set smaller button size
                button.setStyleSheet(f"font-family: {self.predator_font.family()}; background-color: #00B0C8; color: black; font-size: 20px; padding: 5px;")
                button.clicked.connect(lambda _, cmd=label: runCommand(cmd))  # Connect button to command
                button_layout_1.addWidget(button)

            # Create second row of buttons with smaller size
            for label in second_row_labels:
                button = QPushButton(label)
                button.setFixedSize(150, 40)  # Set smaller button size
                button.setStyleSheet(f"font-family: {self.predator_font.family()}; background-color: #00B0C8; color: black; font-size: 20px; padding: 5px;")
                button.clicked.connect(lambda _, cmd=label: runCommand(cmd))  # Connect button to command
                button_layout_2.addWidget(button)

            # Add the button containers to the internal window's layout
            self.internal_window.layout().addWidget(button_container_1)
            self.internal_window.layout().addWidget(button_container_2)

            # Create social media container
            social_media_container = QWidget()
            social_media_layout = QHBoxLayout(social_media_container)

            # Define social media icons and their commands
            social_media_icons = {
                "Discord": "/usr/share/exodia/exodia-welcome/imgs/social-media/discord.png",
                "Reddit": "/usr/share/exodia/exodia-welcome/imgs/social-media/reddit.png",
                "Telegram": "/usr/share/exodia/exodia-welcome/imgs/social-media/tg.png",
                "GitHub": "/usr/share/exodia/exodia-welcome/imgs/social-media/gh.png",
                "YouTube": "/usr/share/exodia/exodia-welcome/imgs/social-media/youtube.png"
            }

            # Create buttons for social media icons
            for name, icon_path in social_media_icons.items():
                icon_button = QPushButton()
                icon_button.setFixedSize(40, 40)  # Set icon button size
                icon_button.setIcon(QIcon(icon_path))  # Set icon
                icon_button.setIconSize(QSize(40, 40))  # Set icon size
                icon_button.setStyleSheet("background-color: transparent; border: none;")
                icon_button.clicked.connect(lambda _, cmd=name: runCommand(cmd))  # Connect button to command
                social_media_layout.addWidget(icon_button)

            # Add the social media container to the internal window's layout
            self.internal_window.layout().addWidget(social_media_container)

        else:
            print("already has a layout")


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

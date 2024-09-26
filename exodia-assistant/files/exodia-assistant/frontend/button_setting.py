#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

import os
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont, QFontDatabase, QPolygon, QRegion, QPen
from PyQt5.QtWidgets import QMainWindow, QPushButton

class SettingWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.toggle_button = None
        self.is_auto_start = None
        self.custom_font = None
        self.config_path = os.path.expanduser('~/.config/bspwm/exodia.conf')  # Path to the config file
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1140, 640)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setMask(self.createMask())
        self.loadCustomFont()
        self.loadAutoStartStatus()  # Load the current auto-start status
        self.addToggleButton()

    @staticmethod
    def createMask():
        points = [
            QPoint(910, 100),   # Top center, 1 (Reduced width)
            QPoint(940, 130),  # Top right, 2
            QPoint(940, 440), # Middle right, 3 (Reduced height)
            QPoint(230, 440),  # Bottom center, 4
            QPoint(200, 410),   # Bottom left, 5
            QPoint(200, 100),     # Middle left, 6
        ]
        polygon = QPolygon(points)
        return QRegion(polygon)

    def loadCustomFont(self):
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load custom font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 20, QFont.Bold)

    def loadAutoStartStatus(self):
        # Load the auto-start status from the configuration file
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as config_file:
                for line in config_file:
                    if 'exodia-assistant-auto-start' in line:
                        self.is_auto_start = line.split('=')[1].strip().lower() == 'true'
                        break
        else:
            self.is_auto_start = False  # Default to false if the file does not exist

    def addToggleButton(self):
        self.toggle_button = QPushButton('', self)  # Initialize without text
        self.toggle_button.setGeometry(450, 200, 240, 100)
        self.updateToggleButtonStyle()

        # Set non-rectangular shape
        self.toggle_button.setMask(self.createButtonMask())
        self.toggle_button.clicked.connect(self.toggleAutoStart)

    def createButtonMask(self):
        button_points = [
            QPoint(200, 0),        # Top right, 1
            QPoint(240, 50),       # Bottom right (adjusted height), 2
            QPoint(200, 100),      # Bottom right curve, 3
            QPoint(40, 100),      # Bottom left curve, 4
            QPoint(0, 50),         # Bottom left, 5
            QPoint(40, 0),        # Top left, 6
        ]
        polygon = QPolygon(button_points)
        return QRegion(polygon)

    def updateToggleButtonStyle(self):
        if self.is_auto_start:
            self.toggle_button.setText('ON')
            self.toggle_button.setStyleSheet("""
                QPushButton {
                    background-color: #00B0C8;
                    color: white;
                    font-size: 24px;
                    font-weight: bold;
                    border-radius: 30px;  /* Rounded corners */
                }
            """)
        else:
            self.toggle_button.setText('OFF')
            self.toggle_button.setStyleSheet("""
                QPushButton {
                    background-color: #121212;
                    color: white;
                    font-size: 24px;
                    font-weight: bold;
                    border-radius: 30px;  /* Rounded corners */
                }
            """)

    def toggleAutoStart(self):
        # Toggle the auto-start state and update the button style
        self.is_auto_start = not self.is_auto_start
        self.updateToggleButtonStyle()
        self.saveAutoStartStatus()  # Save the updated status to the configuration file

    def saveAutoStartStatus(self):
        # Save the auto-start status to the configuration file
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as config_file:
                lines = config_file.readlines()

            with open(self.config_path, 'w') as config_file:
                for line in lines:
                    if 'exodia-assistant-auto-start' in line:
                        # Update the line with the new status
                        line = f'exodia-assistant-auto-start = {"true" if self.is_auto_start else "false"}\n'
                    config_file.write(line)
        else:
            # If the file doesn't exist, create it and set the value
            with open(self.config_path, 'w') as config_file:
                config_file.write(f'exodia-assistant-auto-start = {"true" if self.is_auto_start else "false"}\n')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the window background
        painter.setBrush(QBrush(QColor("#1F1F1F")))
        painter.drawRect(self.rect())

        # Draw the border with color #00B0C8 and width 5
        border_points = [
            QPoint(910, 100),   # Top center, 1 (Reduced width)
            QPoint(940, 130),  # Top right, 2
            QPoint(940, 440), # Middle right, 3 (Reduced height)
            QPoint(230, 440),  # Bottom center, 4
            QPoint(200, 410),   # Bottom left, 5
            QPoint(200, 100),     # Middle left, 6
        ]
        border_polygon = QPolygon(border_points)

        # Draw the outer border of the main window
        border_pen = QPen(QColor("#00B0C8"))  # Set the border color
        border_pen.setWidth(10)  # Set the border width
        painter.setPen(border_pen)
        painter.drawPolygon(border_polygon)  # Draw the border polygon

        # Draw window text
        if hasattr(self, 'custom_font'):
            painter.setFont(self.custom_font)
            text = "Auto-Start Assistant"
            painter.setPen(QColor("#00B0C8"))
            painter.drawText(self.rect(), Qt.AlignCenter, text)

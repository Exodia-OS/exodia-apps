import os
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont, QFontDatabase, QPen, QPolygon, QRegion
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys

class SettingWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.toggle_button = None
        self.close_button = None  # New button instance
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
        self.addCloseButton()        # Add the new Close button
        self.addToggleButton()
        print("UI Initialized")

    @staticmethod
    def createMask():
        points = [
            QPoint(910, 100),   # Top center, 1
            QPoint(940, 130),  # Top right, 2
            QPoint(940, 440),  # Middle right, 3
            QPoint(230, 440),  # Bottom center, 4
            QPoint(200, 410),  # Bottom left, 5
            QPoint(200, 100),  # Middle left, 6
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
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as config_file:
                for line in config_file:
                    if 'exodia-assistant-auto-start' in line:
                        self.is_auto_start = line.split('=')[1].strip().lower() == 'true'
                        break
        else:
            self.is_auto_start = False  # Default to false if the file does not exist
        print(f"Auto-start status loaded: {self.is_auto_start}")

    def addCloseButton(self):

        self.close_button = QPushButton('X', self)
        self.close_button.setGeometry(850, 110, 80, 80)  # Positioned above the toggle button
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #1F1F1F;
                color: #00B0C8;
                font-size: 30px;
                font-weight: bold;
                border-radius: 30px;
            }
        """)
        self.close_button.setMask(self.createButtonMask())  # Use the same mask for custom shape
        self.close_button.clicked.connect(self.close)

    def addToggleButton(self):
        self.toggle_button = QPushButton('', self)  # Initialize without text
        self.toggle_button.setGeometry(450, 200, 240, 100)
        self.updateToggleButtonStyle()
        self.toggle_button.setMask(self.createButtonMask())
        self.toggle_button.clicked.connect(self.toggleAutoStart)

    def createButtonMask(self):
        button_points = [
            QPoint(200, 0),        # Top right
            QPoint(240, 50),       # Bottom right
            QPoint(200, 100),      # Bottom right curve
            QPoint(40, 100),       # Bottom left curve
            QPoint(0, 50),         # Bottom left
            QPoint(40, 0),         # Top left
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
                    border-radius: 30px;
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
                    border-radius: 30px;
                }
            """)

    def toggleAutoStart(self):
        self.is_auto_start = not self.is_auto_start
        self.updateToggleButtonStyle()
        self.saveAutoStartStatus()

    def saveAutoStartStatus(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as config_file:
                lines = config_file.readlines()

            with open(self.config_path, 'w') as config_file:
                for line in lines:
                    if 'exodia-assistant-auto-start' in line:
                        line = f'exodia-assistant-auto-start = {"true" if self.is_auto_start else "false"}\n'
                    config_file.write(line)
        else:
            with open(self.config_path, 'w') as config_file:
                config_file.write(f'exodia-assistant-auto-start = {"true" if self.is_auto_start else "false"}\n')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QBrush(QColor("#1F1F1F")))
        painter.drawRect(self.rect())

        border_points = [
            QPoint(910, 100),   # Top center
            QPoint(940, 130),  # Top right
            QPoint(940, 440),  # Middle right
            QPoint(230, 440),  # Bottom center
            QPoint(200, 410),  # Bottom left
            QPoint(200, 100),  # Middle left
        ]
        border_polygon = QPolygon(border_points)

        border_pen = QPen(QColor("#00B0C8"))
        border_pen.setWidth(10)
        painter.setPen(border_pen)
        painter.drawPolygon(border_polygon)

        if hasattr(self, 'custom_font'):
            painter.setFont(self.custom_font)
            text = "Auto-Start Assistant"
            painter.setPen(QColor("#00B0C8"))
            painter.drawText(self.rect(), Qt.AlignCenter, text)


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
        self.initUI()

    def initUI(self):
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.setGeometry(300, 100, 1140, 640)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set custom mask for the non-rectangular window shape
        self.setMask(self.createMask())

        # Set the custom font for the window
        self.loadCustomFont()

        # Add the toggle button
        self.addToggleButton()

    @staticmethod
    def createMask():
        # Define the custom shape using points
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
        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load custom font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 20, QFont.Bold)

    def addToggleButton(self):
        # Create the toggle button
        self.toggle_button = QPushButton('OFF', self)
        self.toggle_button.setGeometry(450, 200, 240, 100)
        self.updateToggleButtonStyle()

        # Connect the button to toggle the state
        self.toggle_button.clicked.connect(self.toggleAutoStart)

    def updateToggleButtonStyle(self):
        # Update button appearance based on state
        if self.is_auto_start:
            self.toggle_button.setText('ON')
            self.toggle_button.setStyleSheet("""
                QPushButton {
                    background-color: #00B0C8;
                    color: white;
                    font-size: 24px;
                    font-weight: bold;
                    border-radius: 50px;
                }
            """)
        else:
            self.toggle_button.setText('OFF')
            self.toggle_button.setStyleSheet("""
                QPushButton {
                    background-color: #FF5F56;
                    color: white;
                    font-size: 24px;
                    font-weight: bold;
                    border-radius: 50px;
                }
            """)

    def toggleAutoStart(self):
        # Toggle the auto-start state
        self.is_auto_start = not self.is_auto_start
        self.updateToggleButtonStyle()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the window background
        painter.setBrush(QBrush(QColor("#1F1F1F")))
        painter.drawRect(self.rect())

        # Draw the border with color #00B0C8 and width 5

        # Define the polygon for the outer border
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

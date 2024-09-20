#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

import sys
import os
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QColor, QRegion, QPolygon, QPen, QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class CustomButton(QPushButton):
    def __init__(self, text, points, x, y, width, height, callback, color="#121212", border_color="#00B0C8", border_thickness=5, parent=None):
        super().__init__(text, parent)
        self.callback = callback  # Store the callback function

        self.setFixedSize(200, 100)
        self.polygon = QPolygon(points)
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.setGeometry(QRect(x, y, width, height))
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMask(QRegion(self.polygon))

        self.loadPredatorFont()

    def loadPredatorFont(self):
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load Predator font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.predator_font = QFont(font_family, 12, QFont.Bold)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.parent().currently_pressed_button == self:
            background_color = QColor("#00B0C8")
            text_color = QColor("white")
        else:
            background_color = QColor(self.color)
            text_color = QColor("#acacac")

        painter.setBrush(background_color)
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(self.polygon)

        pen = QPen(QColor(self.border_color))
        pen.setWidth(self.border_thickness)
        painter.setPen(pen)
        painter.drawPolygon(self.polygon)

        pen = QPen(text_color)
        painter.setPen(pen)
        if self.predator_font:
            painter.setFont(self.predator_font)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.callback()  # Trigger the callback when the button is clicked
        self.parent().setCurrentButton(self)


class CustomButtonPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setFixedSize(width, height)
        self.setFixedSize(200, 400)  # Adjust the size of the main window as needed
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.setGeometry(100, 200, 400, 400)
        self.setAttribute(Qt.WA_TranslucentBackground) # Make the background transparent

        # Initialize the currently pressed button
        self.currently_pressed_button = None

        # Set up a layout for the panel with zero spacing
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Define the shape points, positions, and sizes for each button
        buttons_config = [
            # Welcome Button
            {
                'text': 'Welcome',
                'points': [
                    QPoint(300, 20),
                    QPoint(300, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 50, 'width': 200, 'height': 100,
                'callback': parent.displayWelcomeContent  # Set the callback function
            },
            # Keybinding Button
            {
                'text': 'Keybinding',
                'points': [
                    QPoint(300, 20),
                    QPoint(300, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 160, 'width': 200, 'height': 100,
                'callback': parent.displayKeybindingContent
            },
            # Tips Button
            {
                'text': 'Tips',
                'points': [
                    QPoint(300, 20),
                    QPoint(300, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 270, 'width': 200, 'height': 100,
                'callback': parent.displayTipsContent
            },
            # Setting Button
            {
                'text': 'Setting',
                'points': [
                    QPoint(300, 20),
                    QPoint(300, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 380, 'width': 200, 'height': 100,
                'callback': parent.displaySettingContent
            },
            # Developers Button
            {
                'text': 'Developers',
                'points': [
                    QPoint(300, 20),
                    QPoint(300, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 490, 'width': 200, 'height': 100,
                'callback': parent.displayDevelopersContent
            }
        ]

        # Create custom-shaped buttons with the provided shapes and labels
        for config in buttons_config:
            button = CustomButton(
                text=config['text'],
                points=config['points'],
                x=config['x'],
                y=config['y'],
                width=config['width'],
                height=config['height'],
                callback=config['callback']
            )
            # Add the button to the layout
            self.layout().addWidget(button)

    def setCurrentButton(self, button):
        if self.currently_pressed_button:
            self.currently_pressed_button.update()
        self.currently_pressed_button = button
        self.currently_pressed_button.update()

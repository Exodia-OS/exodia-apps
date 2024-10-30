import sys
import os
from PyQt5.QtCore import Qt, QPoint, QRect, QPropertyAnimation, QSize
from PyQt5.QtGui import QPainter, QColor, QRegion, QPolygon, QPen, QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class CustomButton(QPushButton):
    def __init__(self, text, points, x, y, width, height, callback, color="#0E1218", border_color="#00B0C8", border_thickness=5, parent=None):
        super().__init__(text, parent)
        self.currently_pressed_button = None
        self.predator_font = None
        self.callback = callback  # Store the callback function
        self.setFixedSize(200, 100)
        self.original_points = QPolygon(points)  # Store the original polygon points
        self.reduced_points = QPolygon([
            QPoint(300, 20),
            QPoint(300, 80),
            QPoint(50, 80),
            QPoint(50, 45),
            QPoint(80, 20)
        ])  # Define the reduced points
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.setGeometry(QRect(x, y, width, height))
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMask(QRegion(self.original_points))

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
        painter.drawPolygon(self.original_points if self.parent().currently_pressed_button != self else self.reduced_points)

        pen = QPen(QColor(self.border_color))
        pen.setWidth(self.border_thickness)
        painter.setPen(pen)
        painter.drawPolygon(self.original_points if self.parent().currently_pressed_button != self else self.reduced_points)

        pen = QPen(text_color)
        painter.setPen(pen)
        if self.predator_font:
            painter.setFont(self.predator_font)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.callback()  # Trigger the callback when the button is clicked
        self.parent().setCurrentButton(self)

    def setCurrentButton(self, button):
        if self.currently_pressed_button:
            # Restore the previously pressed button's shape
            self.currently_pressed_button.original_points = self.currently_pressed_button.original_points
            self.currently_pressed_button.update()
        self.currently_pressed_button = button
        # Change the current button to reduced points
        self.currently_pressed_button.original_points = self.currently_pressed_button.reduced_points
        self.currently_pressed_button.update()


class CustomButtonPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 250)  # Adjust the size of the main window as needed
        self.setGeometry(30, 200, 400, 200)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the background transparent

        self.currently_pressed_button = None

        # Set up a layout for the panel with zero spacing
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Define the shape points, positions, and sizes for each button
        buttons_config = [
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
            {
                'text': 'Credits',
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
            self.layout().addWidget(button)

    def setCurrentButton(self, button):
        if self.currently_pressed_button:
            self.currently_pressed_button.update()
        self.currently_pressed_button = button
        self.currently_pressed_button.update()



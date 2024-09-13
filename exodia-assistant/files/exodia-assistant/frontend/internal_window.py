from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QBrush, QRegion, QPolygon, QPen  # Corrected import for QPolygon
from PyQt5.QtWidgets import QWidget

class InternalWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.setGeometry(300, 100, 1140, 640)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the background transparent
        self.polygon = self.createCustomMask()  # Store the polygon used for the mask

    def createCustomMask(self):
        # Define points for an 8-sided polygon
        points = [
            QPoint(1110, 0),   # Top center, 1
            QPoint(1140, 30),  # Top right, 2
            QPoint(1140, 640), # Middle right, 3
            QPoint(1140, 640), # Bottom right, 4
            QPoint(30, 640),   # Bottom center, 5
            QPoint(0, 610),    # Bottom left, 6
            QPoint(0, 0),     # Middle left, 7
            QPoint(0, 0)      # Top left, 8
        ]

        polygon = QPolygon(points)
        mask = QRegion(polygon)
        self.setMask(mask)  # Apply the mask to make the window non-rectangular
        return polygon  # Return the polygon for use in the paint event

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the custom shape with a color fill
        painter.setBrush(QBrush(QColor("#121212")))  # Use a custom background color
        painter.drawPolygon(self.polygon)  # Draw the filled polygon

        # Draw the border with the specified color
        pen = QPen(QColor("#00B0C8"), 3)  # Create a pen with the desired color and border width
        painter.setPen(pen)
        painter.drawPolygon(self.polygon)  # Draw the polygon border
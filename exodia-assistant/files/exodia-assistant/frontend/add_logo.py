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
from PyQt5.QtGui import QPainter, QColor, QRegion, QPolygon, QPen, QPixmap
from PyQt5.QtWidgets import QWidget


class AddLogo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(30, 30, 200, 200)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the background transparent
        self.polygon = self.createCustomMask()  # Store the polygon used for the mask
        self.image_path = os.path.expanduser("~/.face")  # Expand the tilde to the full path
        self.pixmap = QPixmap(self.image_path)

        # Check if the pixmap is loaded correctly
        if self.pixmap.isNull():
            print(f"Failed to load image from: {self.image_path}")

    def createCustomMask(self):
        # Define points for an 8-sided polygon
        points = [
            QPoint(130, 0),   # Top center
            QPoint(160, 30),  # Top right
            QPoint(160, 130), # Middle right
            QPoint(130, 160), # Bottom right
            QPoint(30, 160),  # Bottom center
            QPoint(0, 130),   # Bottom left
            QPoint(0, 30),    # Middle left
            QPoint(30, 0)     # Top left
        ]

        polygon = QPolygon(points)
        mask = QRegion(polygon)
        self.setMask(mask)  # Apply the mask to make the window non-rectangular
        return polygon  # Return the polygon for use in the paint event

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the custom shape with the image fill if the pixmap is valid
        if not self.pixmap.isNull():
            # Get the bounding rectangle of the polygon
            bounding_rect = self.polygon.boundingRect()

            # Scale the pixmap to fit the bounding rectangle of the polygon
            scaled_pixmap = self.pixmap.scaled(
                bounding_rect.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )

            # Clip the painter to the custom polygon region
            painter.setClipRegion(QRegion(self.polygon))

            # Calculate offsets to center the pixmap within the bounding rectangle
            offset_x = (bounding_rect.width() - scaled_pixmap.width()) // 2 + bounding_rect.x()
            offset_y = (bounding_rect.height() - scaled_pixmap.height()) // 2 + bounding_rect.y()

            # Draw the scaled pixmap centered within the polygon
            painter.drawPixmap(offset_x, offset_y, scaled_pixmap)

        # Draw the border with the specified color
        pen = QPen(QColor("#00B0C8"), 3)  # Create a pen with the desired color and border width
        painter.setPen(pen)
        painter.drawPolygon(self.polygon)  # Draw the polygon border

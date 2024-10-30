#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

# AddLogo Class #
from PyQt5.QtWidgets import QWidget


class AddLogo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.setGeometry(30, 20, 150, 150)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the background transparent
        self.radius = min(self.width(), self.height()) // 2
        self.image_path = os.path.expanduser("/usr/share/pixmaps/exodia-cyan.png")  # Expand the tilde to the full path
        self.pixmap = QPixmap(self.image_path)

        # Check if the pixmap is loaded correctly
        if self.pixmap.isNull():
            print(f"Failed to load image from: {self.image_path}")

    def createCustomMask(self):
        # Define a circular mask
        path = QPainterPath()
        path.addEllipse(0, 0, self.width(), self.height())
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)  # Apply the mask to make the window circular
        return path  # Return the path for use in the paint event

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the custom shape with the image fill if the pixmap is valid
        if not self.pixmap.isNull():
            # Get the bounding rectangle of the circular path
            bounding_rect = self.rect()

            # Scale the pixmap to fit the bounding rectangle of the circle
            scaled_pixmap = self.pixmap.scaled(
                bounding_rect.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )

            # Clip the painter to the circular region
            painter.setClipRegion(QRegion(self.createCustomMask().toFillPolygon().toPolygon()))

            # Calculate offsets to center the pixmap within the bounding rectangle
            offset_x = (bounding_rect.width() - scaled_pixmap.width()) // 2
            offset_y = (bounding_rect.height() - scaled_pixmap.height()) // 2

            # Draw the scaled pixmap centered within the circle
            painter.drawPixmap(offset_x, offset_y, scaled_pixmap)

########################################################################################################################

# InternalWindow Class #
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea

class InternalWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.setGeometry(230, 100, 910, 590)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the background transparent
        self.polygon = self.createCustomMask()  # Store the polygon used for the mask
        self.content_label = QLabel(self)
        self.content_label.setGeometry(self.rect())
        self.content_label.setStyleSheet("color: white; font-size: 20px; padding: 10px;")

        # Create the scroll area
        scroll_area = QScrollArea(self)
        # self.setGeometry(x, y, width, height)
        scroll_area.setGeometry(5, 5, 875, 505)  # Set scroll area size within the internal window
        # scroll_area.setGeometry(self.rect())  # Set the scroll area to the full size of the window
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)  # Ensure the content resizes with the window

        # Create a widget to hold the content (which will be scrollable)
        scroll_content = QWidget()
        scroll_content.setStyleSheet("background-color: #0E1218;")  # Transparent background for content
        scroll_area.setWidget(scroll_content)

        # Create a layout for the scrollable content
        layout = QVBoxLayout(scroll_content)

        # Content label that will be scrollable
        self.content_label = QLabel(scroll_content)
        self.content_label.setStyleSheet("color: #0E1218; font-size: 20px; padding: 10px;")
        self.content_label.setWordWrap(True)  # Allow the text to wrap

        layout.addWidget(self.content_label)  # Add the label to the layout

        # Remove border and customize scroll bar colors
        scroll_area.setStyleSheet("""
            QScrollArea { border: none; }
            QScrollBar:vertical {
                background: #222;  /* Background color of the vertical scrollbar */
                width: 10px;       /* Width of the scrollbar */
                margin: 0 0 0 0;   /* Margin around the scrollbar */
            }
            QScrollBar::handle:vertical {
                background: #00B0C8;  /* Color of the scrollbar handle */
                border-radius: 5px;    /* Rounded corners for the scrollbar handle */
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;      /* Hide the add and subtract buttons */
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;      /* Hide the add and subtract page areas */
            }
        """)

    def createCustomMask(self):
        # Define points for an 8-sided polygon
        points = [
            QPoint(880, 0),   # Top center, 1
            QPoint(910, 30),  # Top right, 2
            QPoint(910, 540), # Middle right, 3
            QPoint(30, 540),   # Bottom center, 4
            QPoint(0, 510),    # Bottom left, 5
            QPoint(0, 0)     # Middle left, 6
        ]

        polygon = QPolygon(points)
        mask = QRegion(polygon)
        self.setMask(mask)  # Apply the mask to make the window non-rectangular
        return polygon  # Return the polygon for use in the paint event

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the custom shape with a color fill
        painter.setBrush(QBrush(QColor("#0E1218")))  # Use a custom background color
        painter.drawPolygon(self.polygon)  # Draw the filled polygon

        # Draw the border with the specified color
        pen = QPen(QColor("#00B0C8"), 5)  # Create a pen with the desired color and border width
        painter.setPen(pen)
        painter.drawPolygon(self.polygon)  # Draw the polygon border

    def updateContent(self, text):
        # Assuming you have a QLabel or QTextEdit in the window to display content
        self.content_label.setText(text)  # Update the label with the provided text

########################################################################################################################
# InternalWindow Class #

import os
import subprocess
from datetime import datetime
from PyQt5.QtGui import QFontDatabase, QFont

class ButtonContent:
    def __init__(self, internal_window):
        self.internal_window = internal_window
        self.predator_font = self.loadPredatorFont()
        self.version = self.getExodiaVersion()
        self.current_year = datetime.now().year  # Get the current year

    def loadPredatorFont(self):
        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), './Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load predator font.")
            return None
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            return QFont(font_family, 30, QFont.Bold)

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

    def displayWelcomeContent(self):
        welcome_text = f"""
        
            <div style="font-family: {self.predator_font.family()}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
                
                <h2 style="color: #00C8B0; font-size: 40px; margin-bottom: 15px;">Welcome to Exodia OS</h2>
                
                <p style="font-size: 20px; color: #00C8B0; margin-bottom: 10px;">Version: {self.version}</p>
                                
                <p style="font-size: 18px">
                    A highly customized Arch-based Linux distribution For All Cybersecurity Fields.
                    <br/>
                    It comes with Other Special Editions as well.
                    
                    <br/>
                    <br/>
                    
                    <p style="font-size: 20px; color: #00C8B0; margin-bottom: 10px;">Copyrights:</p>
                    
                    <p style="font-size: 18px;">
                        00xWolf | Cyb3rTh1eveZ Team  﫥  Copyrights 2022-{self.current_year}
                    </p>
                </p>
                
                <table style="margin: 20px 0;">
                    <tr>
                        
                        <td style="text-align: left;">
                            <img src="/usr/share/exodia/about-exodia-os/imgs/Ozil.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%;">
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h3 style="color: #FFFFFF; font-size: 28px; margin: 0;">Mahmoud Mohamed</h3>
                            <br/>
                            <h4 style="color: #00C8B0; margin-top: 0px;">DevOps/MLOps Engineer</h4>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h4 style="color: #00C8B0; font-size: 28px;">Ozil</h4>
                        </td>
                        
                    </tr>
                </table>
                
                <br/>
                Proudly developed in Egypt by Cyb3rTh1eveZ Team.
                    
                    
            </div>
            
    """
        self.internal_window.updateContent(welcome_text)

########################################################################################################################
import os
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QBrush, QPolygon, QColor, QRegion, QFont, QFontDatabase, QPixmap, QPainterPath, QLinearGradient, QPen
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QApplication
from Xlib import X, display
from Xlib.Xatom import STRING

# Function to set WM_CLASS for the window
def set_wm_class(win_id, instance_name, class_name):
    # Set the WM_CLASS property for a window.
    disp = display.Display()
    window = disp.create_resource_object('window', win_id)
    wm_class_atom = disp.intern_atom('WM_CLASS')
    value = f'{instance_name}\0{class_name}\0'.encode('utf-8')
    window.change_property(wm_class_atom, STRING, 8, value)
    disp.flush()

# Function to create a mask for the custom window shape
def createMask():
    points = [
        QPoint(1150, 0),     # Top right corner, 1
        QPoint(1200, 50),    # Right top-middle, a bit down, 2
        QPoint(1200, 700),   # Bottom right corner, 3
        QPoint(50, 700),     # Bottom left-middle, 4
        QPoint(0, 650),      # Bottom left corner, 5
        QPoint(0, 0)        # Top left corner, 6
    ]
    polygon = QPolygon(points)
    return QRegion(polygon)

# Main CustomShapeWindow class
class CustomShapeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_panel = None
        self.internal_window = None
        self.add_logo = None
        self.close_button = None
        self.minimize_button = None
        self.predator_font = None
        self.button_font = None
        self.logo_pixmap = None
        self.button_content = None
        self.setting_window = None  # Initialize the setting window variable
        self.initUI()

    def initUI(self):
        # Set window size
        self.setFixedSize(1200, 700)  # Adjust size as needed
        # Set window flags to remove the title bar and make it frameless
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # Make the window transparent
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Load custom fonts
        self.loadPredatorFont()
        # Load buttons fonts
        self.loadButtonFont()
        # Define the custom shape
        self.setMask(createMask())
        # Add buttons
        self.addButtons()
        # Add the internal window shape
        self.internal_window = InternalWindow(self)
        self.internal_window.show()
        # Add the logo
        self.add_logo = AddLogo(self)
        self.add_logo.show()
        # Set WM_CLASS after the window is shown
        self.set_wm_class()
        # Initialize ButtonContent
        self.button_content = ButtonContent(self.internal_window)
        # Display the welcome content when the app opens
        self.displayWelcomeContent()
        # Set window size and other configurations...
        self.addButtons()

    # Set the WM_CLASS property with instance and class names
    def set_wm_class(self):

        # Get the native window ID
        win_id = self.winId().__int__()
        set_wm_class(win_id, "about-exodia-os", "About ExodiaOS")

    def loadPredatorFont(self):

        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), './Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load predator font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.predator_font = QFont(font_family, 30, QFont.Bold)

    def loadButtonFont(self):

        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), './Fonts', 'Squares-Bold-Italic.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load button font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.button_font = QFont(font_family, 25, QFont.Bold)

    def addButtons(self):

        # Create a QWidget to hold the buttons
        button_widget = QWidget(self)
        button_widget.setGeometry(QRect(self.width() - 200, 0, 200, 40))
        button_widget.setAttribute(Qt.WA_TranslucentBackground)

        self.close_button = QPushButton('X', button_widget)
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.close_button.setGeometry(100, 10, 40, 40)
        self.close_button.clicked.connect(self.closeWindow)
        self.close_button.setFont(self.button_font)

        # Set button styles (optional)
        for button in [self.close_button]:
            button.setStyleSheet("color: #00B0C8; border: none; font-size: 25px;")
            button.setFixedSize(40, 40)

    def minimizeWindow(self):
        self.showMinimized()

    def closeWindow(self):
        self.close()

    def displayWelcomeContent(self):
        self.button_content.displayWelcomeContent()  # Call the method from ButtonContent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw background or other custom content
        painter.setBrush(QBrush(QColor("#151A21")))
        painter.drawRect(self.rect())

        # Draw the logo in the top left corner, slightly moved to the right
        if self.logo_pixmap:
            painter.drawPixmap(60, 20, self.logo_pixmap) # Adjust position as needed

        # Set the custom font if loaded
        if hasattr(self, 'predator_font'):
            painter.setFont(self.predator_font)

        # Define the polygon for the outer border
        border_points = [
            QPoint(1150, 0),     # Top right corner, 1
            QPoint(1200, 50),    # Right top-middle, a bit down, 2
            QPoint(1200, 700),   # Bottom right corner, 3
            QPoint(50, 700),     # Bottom left-middle, 4
            QPoint(0, 650),      # Bottom left corner, 5
            QPoint(0, 0)        # Top left corner, 6
            ]
        border_polygon = QPolygon(border_points)

        # Draw the outer border of the main window
        border_pen = QPen(QColor("#0E1218"))  # Set the border color
        border_pen.setWidth(10)  # Set the border width
        painter.setPen(border_pen)
        painter.drawPolygon(border_polygon)  # Draw the border polygon

        # Create a QPainterPath for the inverted trapezoid background
        path = QPainterPath()
        path.moveTo(self.width() / 2 - 320, 5)
        path.lineTo(self.width() / 2 + 320, 5)
        path.lineTo(self.width() / 2 + 220, 70)
        path.lineTo(self.width() / 2 - 220, 70)
        path.closeSubpath()

        # Create a gradient from "#141414" to "#0D0D0D"
        gradient = QLinearGradient(self.width() / 2 - 200, 0, self.width() / 2 - 200, 70)
        gradient.setColorAt(0, QColor("#15191F"))
        gradient.setColorAt(1, QColor("#0D1117"))

        # Set no pen to remove the border
        painter.setPen(Qt.NoPen)

        # Set the gradient brush for the trapezoid background
        painter.setBrush(QBrush(gradient))
        painter.drawPath(path)

        # Center the text horizontally
        text = "About ExodiaOS"
        text_rect = painter.fontMetrics().boundingRect(text)
        text_width = text_rect.width()
        text_height = text_rect.height()
        x_pos = int((self.width() - text_width) / 2)
        y_pos = int(10)

        # Draw the text with gradient colors
        gradient_pen = QPen(QColor("#00B0C8"))
        painter.setPen(gradient_pen)
        painter.drawText(QRect(x_pos, y_pos, text_width, text_height), Qt.AlignCenter, text)


if __name__ == '__main__':
    app = QApplication([])
    window = CustomShapeWindow()  # Create an instance of CustomShapeWindow
    window.show()
    app.exec_()

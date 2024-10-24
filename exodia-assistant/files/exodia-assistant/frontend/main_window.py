#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

import os
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QBrush, QPolygon, QColor, QRegion, QFont, QFontDatabase, QPixmap, QPainterPath, QLinearGradient, QPen
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QApplication
from frontend.internal_window import InternalWindow
from frontend.add_logo import AddLogo
from frontend.custom_button import CustomButton  # Import the button panel
from frontend.custom_button import CustomButtonPanel  # Import the button panel
from Xlib import X, display
from Xlib.Xatom import STRING
from frontend.buttons_content import ButtonContent  # Import the ButtonContent class
from frontend.button_setting import SettingWindow

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
        QPoint(1450, 0),     # Top right corner, 1
        QPoint(1500, 50),    # Right top-middle, a bit down, 2
        QPoint(1500, 800),   # Bottom right corner, 3
        QPoint(50, 800),     # Bottom left-middle, 4
        QPoint(0, 750),      # Bottom left corner, 5
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
        self.settings_button = None
        self.minimize_button = None
        self.predator_font = None
        self.button_font = None
        self.logo_pixmap = None
        self.button_content = None
        self.setting_window = None  # Initialize the setting window variable
        self.initUI()

    def initUI(self):
        # Set window size
        self.setFixedSize(1500, 800)  # Adjust size as needed
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
        # Add the custom button panel
        self.addButtonPanel()  # Call function to add button panel
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
        set_wm_class(win_id, "exodiaos-assistant", "ExodiaOS Assistant")

    # Function to handle settings button click
    def openSettings(self):
        try:
            self.setting_window = SettingWindow(self)
            self.setting_window.show()
        except Exception as e:
            print(f"Error initializing SettingWindow: {e}")


    def loadPredatorFont(self):

        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load predator font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.predator_font = QFont(font_family, 30, QFont.Bold)

    def loadButtonFont(self):

        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold-Italic.otf')
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

        # Create the buttons
        self.settings_button = QPushButton('⚙', button_widget)
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.settings_button.setGeometry(0, 10, 40, 40)
        self.settings_button.clicked.connect(self.openSettings) # Connect button to openSettings method
        self.settings_button.setFont(self.button_font)

        self.minimize_button = QPushButton('—', button_widget)
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.minimize_button.setGeometry(50, 10, 40, 40)
        self.minimize_button.clicked.connect(self.minimizeWindow)
        self.minimize_button.setFont(self.button_font)

        self.close_button = QPushButton('X', button_widget)
        # Set the geometry (position and size) of the internal window
        # self.setGeometry(x, y, width, height)
        self.close_button.setGeometry(100, 10, 40, 40)
        self.close_button.clicked.connect(self.closeWindow)
        self.close_button.setFont(self.button_font)

        # Set button styles (optional)
        for button in [self.settings_button, self.minimize_button, self.close_button]:
            button.setStyleSheet("color: #00B0C8; border: none; font-size: 25px;")
            button.setFixedSize(40, 40)

    def addButtonPanel(self):

        # Create the custom button panel and add it to the window
        self.button_panel = CustomButtonPanel(self)
        # self.button_panel.setGeometry(40, 210, 200, 300)  # Adjust the position and size as needed
        self.button_panel.show()

    def minimizeWindow(self):
        self.showMinimized()

    def closeWindow(self):
        self.close()

    def displayWelcomeContent(self):
        self.button_content.displayWelcomeContent()  # Call the method from ButtonContent

    def displayKeybindingContent(self):
        self.button_content.displayKeybindingContent() # Call the method from ButtonContent

    def displayTipsContent(self):
        self.button_content.displayTipsContent() # Call the method from ButtonContent

    def displaySettingContent(self):
        self.button_content.displaySettingContent() # Call the method from ButtonContent

    def displayDevelopersContent(self):
        self.button_content.displayDevelopersContent() # Call the method from ButtonContent

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
            QPoint(1450, 0),     # Top right corner, 1
            QPoint(1500, 50),    # Right top-middle, a bit down, 2
            QPoint(1500, 800),   # Bottom right corner, 3
            QPoint(50, 800),     # Bottom left-middle, 4
            QPoint(0, 750),      # Bottom left corner, 5
            QPoint(0, 0)        # Top left corner, 6
            ]
        border_polygon = QPolygon(border_points)

        # Draw the outer border of the main window
        border_pen = QPen(QColor("#121212"))  # Set the border color
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

        # Set the 1st border for the trapezoid
        # border_pen = QPen(QColor("#00B0C8"), 3)  # Create a pen with border color and width
        # painter.setPen(border_pen)
        # painter.drawPath(path)  # Draw the trapezoid border

        # Set the 2nd border for the trapezoid
        # border_pen = QPen(QColor("#121212"), 2)  # Create a pen with border color and width
        # painter.setPen(border_pen)
        # painter.drawPath(path)  # Draw the trapezoid border

        # Center the text horizontally
        text = "ExodiaOS Assistant"
        text_rect = painter.fontMetrics().boundingRect(text)
        text_width = text_rect.width()
        text_height = text_rect.height()
        x_pos = int((self.width() - text_width) / 2)
        y_pos = int(10)

        # Draw the text with gradient colors
        gradient_pen = QPen(QColor("#00B0C8"))
        painter.setPen(gradient_pen)
        painter.drawText(QRect(x_pos, y_pos, text_width, text_height), Qt.AlignCenter, text)


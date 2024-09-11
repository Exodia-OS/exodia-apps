#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

class CustomButtonWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.developers_button = None
        self.settings_button = None
        self.tips_button = None
        self.keybinding_button = None
        self.welcome_button = None
        self.initUI()

    def initUI(self):
        # Create a vertical layout to stack buttons
        layout = QVBoxLayout()

        # Create and add buttons to the layout
        self.welcome_button = QPushButton('Welcome')
        self.keybinding_button = QPushButton('Keybinding')
        self.tips_button = QPushButton('Tips')
        self.settings_button = QPushButton('Setting')
        self.developers_button = QPushButton('Developers')

        layout.addWidget(self.welcome_button)
        layout.addWidget(self.keybinding_button)
        layout.addWidget(self.tips_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.developers_button)

        # Set layout to the widget
        self.setLayout(layout)

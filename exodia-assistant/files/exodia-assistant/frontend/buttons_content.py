#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

class ButtonContent:
    def __init__(self, internal_window):
        self.internal_window = internal_window

    def displayWelcomeContent(self):
        welcome_text = """
        Exodia OS is a highly customized Arch-based Linux distribution built for and by cybersecurity experts, 
        and also for daily usage, capable of performing the strongest pentests and the simplest daily tasks. 
        Even if you're not a cybersecurity fanatic, you'll come to love Exodia OS for its aesthetically pleasing interface, 
        tools, and features. Overall, Exodia OS is a great distro choice for programming and development, 
        operations security, OSINT, and of course daily usage.

        Proudly developed in Egypt 🇪🇬 by Cyb3rTh1eveZ Team.
        """
        self.internal_window.updateContent(welcome_text)

    def displayKeybindingContent(self):
        keybinding_text = "Keybinding content goes here."
        self.internal_window.updateContent(keybinding_text)

    def displayTipsContent(self):
        tips_text = "Tips content goes here."
        self.internal_window.updateContent(tips_text)

    def displaySettingContent(self):
        setting_text = "Setting content goes here."
        self.internal_window.updateContent(setting_text)

    def displayDevelopersContent(self):
        developers_text = "Developers content goes here."
        self.internal_window.updateContent(developers_text)

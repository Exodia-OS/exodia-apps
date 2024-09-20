#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

import os
from PyQt5.QtGui import QFontDatabase, QFont

class ButtonContent:
    def __init__(self, internal_window):
        self.internal_window = internal_window
        self.predator_font = self.loadPredatorFont()

    def loadPredatorFont(self):
        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load predator font.")
            return None
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            return QFont(font_family, 30, QFont.Bold)

    def displayWelcomeContent(self):
        welcome_text = """
        
            <div style="text-align: center; padding: 20px;">
                <img src="icons/exodia-cyan.png" border="0" width="120" style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Welcome to Exodia OS</h1>
                
                <p style="font-size: 20px">
                    Exodia OS is a highly customized Arch-based Linux distribution, crafted for cybersecurity experts and daily users alike. 
                    Whether you're performing robust pentests or tackling simple daily tasks, Exodia OS provides a seamless experience.
                    Its aesthetically pleasing interface and powerful tools make it a prime choice for programming, development, 
                    operations security, OSINT, and much more.
                </p>
                
                <p style="font-style: italic; margin: 20px 0;">
                    Proudly developed in Egypt by the Cyb3rTh1eveZ Team. 🇪🇬
                </p>
                
                <div style="text-align: center; margin: 20px 0;">
                    <img src="imgs/desktop.png" alt="Exodia OS Desktop" width="785" height="320" style="border: 2px solid #00C8B0; border-radius: 10px; max-width: 100%; height: auto;">
                </div>
                
                <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">Benefits:</h2>
                
                <ul style="list-style-type: none; padding-left: 0;">
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Dynamic Environments:</strong> Comes with BSPWM and 20+ tailor-made themes.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Preinstalled Tools:</strong> Essential cybersecurity tools are included.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Multiple Editions:</strong> Choose from Home, Acer-Predator, and Wireless editions.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Versatile Window Managers:</strong> Currently supports BSPWM, DWM, and I3WM.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Future Updates:</strong> More DEs, WMs, and WCs are on the way.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Simplified Installation:</strong> Easy installation with the Calamares installer.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px;">
                         <strong>Rolling Release:</strong> Always up to date with the latest features.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px;">
                         <strong>AUR Support:</strong> Full support for AUR repositories (with yay).
                    </li>
                
                </ul>
                
                
                <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">Key Features:</h2>
                
                <ul style="list-style-type: none; padding-left: 0;">
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>PowerShell:</strong> Microsoft PowerShell pre-installed/pre-configured with Oh My Posh.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>TUI Apps:</strong> Support a whole bunch of TUI Apps RUN: `pacman -Sg Exodia-TUI-Apps` to list all available apps.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Files Templates:</strong> Help you to create coding files like: web Dev, python, etc... and more Files Templates.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>EWW:</strong> Supporting ElKowars wacky widgets(EWW), comes with EWW pre-installed/configured.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>zsh:</strong> Exodia comes zsh pre-installed and pre-configured zsh is the default shell.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>PredatorSense:</strong> A kernel module to control RGB & Fan speed in Linux for Acer Predator Laptops via:`Predator-Sense-CLI`, `Predator-Sense-GUI`.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px;">
                         <strong>CyberSecurity Tools:</strong> Support tools for all CyberSecurity fields using BlackArch Repos & Exodia Repos.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px;">
                         <strong>BIOS & UEFI:</strong> Supporting both BIOS & UEFI.
                    </li>
                    
                    <br>
                
                    <li style="padding: 10px;">
                         <strong>Plymouth:</strong> Supporting `Plymouth`, `exodia-plymouth` is the default theme.
                    </li>
                
                </ul>
            
            </div>
    """.format(self.predator_font.family())  # Use the custom font family
        self.internal_window.updateContent(welcome_text)

    def displayKeybindingContent(self):
        keybinding_text = """
        <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Keybinding Overview</h1>
                
            </div>
        """.format(self.predator_font.family())
        self.internal_window.updateContent(keybinding_text)

    def displayTipsContent(self):
        tips_text = """
        <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Tips Overview</h1>
                
            </div>
        """.format(self.predator_font.family())
        self.internal_window.updateContent(tips_text)

    def displaySettingContent(self):
        setting_text = """
            
            <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Settings Overview</h1>
                
                <p style="font-size: 20px">
                    The Settings tab will be available soon, Inshallah! This tab is designed to help you easily change system configurations, including:
                </p>
                
                <br>
                
                <ul style="list-style-type: none; padding-left: 0; margin-top: 10px;">
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Background, Themes, Icons:</strong> Customize your visual experience effortlessly.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Polybar:</strong> Easily configure your Polybar settings.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>RGB Keyboard:</strong> Control RGB settings for Predator Edition laptops.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Picom Config:</strong> Tailor your Picom configuration.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Keybinding:</strong> Set and modify keybindings easily.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>BSPWM Configurations:</strong> Manage BSPWM configurations and appearance settings.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Auto-Start:</strong> Automatically start Exodia Assistant on boot.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Auto-Update:</strong> Keep your BSPWM configuration up to date with Exodia OS repositories.
                    </li>
                    
                    <br>
                    
                    <li style="padding: 10px;">
                         <strong>And More:</strong> Stay tuned for additional features!
                    </li>
                </ul>
                
                <br>
                
                <p style="font-style: italic; margin: 20px 0;">
                    Thank you for using Exodia OS!  󰣐
                </p>
                
            </div>
    """.format(self.predator_font.family())
        self.internal_window.updateContent(setting_text)


    def displayDevelopersContent(self):
        developers_text = """
            
            <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">The Team Made ExodiaOS</h1>
                
                <p style="font-size: 20px">
                    Exodia Project is a community-driven project. In this page we list contributors and members who have contributed significantly to Exodia OS.
                </p>
                
                <table style="margin: 20px 0;">
                    <tr>
                        
                        <td style="text-align: left;">
                            <img src="imgs/team/Ozil.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #FFFFFF; font-size: 28px; margin: 0;">Ozil</h2>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">DevOps Engineer</h2>
                        </td>
                        
                    </tr>
                </table>
                                
                <ul style="list-style-type: none; padding-left: 0;">
                         
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Team Leader</strong> 
                    </li>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Core Dev</strong>
                    </li>
                                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Release Manager</strong>
                    </li>
                                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Package Maintainer</strong>
                    </li>
            
                </ul>
                
                <br>
                
                <table style="margin: 20px 0;">
                    <tr>
                    
                        <td style="text-align: left;">
                            <img src="imgs/team/Budas.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                        </td>
                    
                        <td style="padding-left: 20px;">
                            <h2 style="color: #FFFFFF; font-size: 28px; margin: 0;">Budas</h2>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">Jr. PenTester</h2>
                        </td>
                        
                    </tr>
                </table>
                                
                <ul style="list-style-type: none; padding-left: 0;">
                         
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>source code review</strong> 
                    </li>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Core Dev</strong>
                    </li>
            
                </ul>
                
                <br>
                
                <table style="margin: 20px 0;">
                    <tr>
                    
                        <td style="text-align: left;">
                            <img src="imgs/team/Joe.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                        </td>
                    
                        <td style="padding-left: 20px;">
                            <h2 style="color: #FFFFFF; font-size: 28px; margin: 0;">Joe</h2>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">Web Developer</h2>
                        </td>
                        
                    </tr>
                </table>
                                
                <ul style="list-style-type: none; padding-left: 0;">
                         
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Web Development</strong> 
                    </li>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Docs Maintainer</strong>
                    </li>
            
                </ul>
                
                <br>
                
                <table style="margin: 20px 0;">
                    <tr>
                    
                        <td style="text-align: left;">
                            <img src="imgs/team/DonSom3a.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                        </td>
                    
                        <td style="padding-left: 20px;">
                            <h2 style="color: #FFFFFF; font-size: 28px; margin: 0;">Don som3a</h2>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">DevOps Engineer</h2>
                        </td>
                        
                    </tr>
                </table>
                                
                <ul style="list-style-type: none; padding-left: 0;">
                         
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Web Development</strong> 
                    </li>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Docs Maintainer</strong>
                    </li>
            
                </ul>
                
                <br>
                
                <div style="text-align: center; margin: 20px 0;">
                    <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Community Contributes</h1>
                </div>
                
                <br>
                
                <table style="margin: 20px 0;">
                    <tr>
                    
                        <td style="text-align: left;">
                            <img src="imgs/team/NahianAdnan.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                        </td>
                    
                        <td style="padding-left: 20px;">
                            <h2 style="color: #FFFFFF; font-size: 28px; margin: 0;">Nahian Adnan</h2>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">Discord Admin</h2>
                        </td>
                        
                    </tr>
                </table>

            </div>
        """.format(self.predator_font.family())
        self.internal_window.updateContent(developers_text)

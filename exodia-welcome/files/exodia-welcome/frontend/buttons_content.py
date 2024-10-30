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
        <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
            <h2 style="color: #00C8B0; font-size: 40px; margin-bottom: 15px;">Welcome to Exodia OS</h2>
            <p style="font-size: 18px">
                A highly customized Arch-based Linux distribution for all cybersecurity fields.
                <br/>
                It comes with other special editions as well.
                <br/>
                We advise cleaning the computer with GParted before installing.
            </p>
            <div style="margin-top: 20px;">
                <button style="background-color: #00C8B0; color: white; border: none; padding: 10px 15px; margin: 5px; cursor: pointer;">Run GParted</button>
                <button style="background-color: #00C8B0; color: white; border: none; padding: 10px 15px; margin: 5px; cursor: pointer;">Exodia Assistant</button>
                <button style="background-color: #00C8B0; color: white; border: none; padding: 10px 15px; margin: 5px; cursor: pointer;">Exodia Installer</button>
            </div>
            <div style="margin-top: 15px;">
                <button style="background-color: #00C8B0; color: white; border: none; padding: 10px 15px; margin: 5px; cursor: pointer;">About Exodia</button>
                <button style="background-color: #00C8B0; color: white; border: none; padding: 10px 15px; margin: 5px; cursor: pointer;">Wiki</button>
                <button style="background-color: #00C8B0; color: white; border: none; padding: 10px 15px; margin: 5px; cursor: pointer;">Docs</button>
                <button style="background-color: #00C8B0; color: white; border: none; padding: 10px 15px; margin: 5px; cursor: pointer;">News</button>
            </div>
    
            <!-- Social media icons -->
            <div style="margin: 20px 0;">
            <h4 style="color: #00C8B0;">Follow us on:</h4>
                <a href="https://discord.gg/wPDyfR5AV9" target="_blank">
                    <img src="/usr/share/exodia/exodia-welcome/imgs/social-media/discord.png" alt="Discord" width="40" height="40" style="margin-right: 10px;">
                </a>
                <a href="https://github.com/Exodia-OS" target="_blank">
                    <img src="/usr/share/exodia/exodia-welcome/imgs/social-media/gh.png" alt="GitHub" width="40" height="40" style="margin-right: 10px;">
                </a>
                <a href="https://www.reddit.com/r/ExodiaOS" target="_blank">
                    <img src="/usr/share/exodia/exodia-welcome/imgs/social-media/reddit.png" alt="Reddit" width="40" height="40" style="margin-right: 10px;">
                </a>
                <a href="https://t.me/exodiaos" target="_blank">
                    <img src="/usr/share/exodia/exodia-welcome/imgs/social-media/tg.png" alt="Telegram" width="40" height="40" style="margin-right: 10px;">
                </a>
                <a href="https://www.youtube.com/@mahmoudmohammed00xwolf88/videos" target="_blank">
                    <img src="/usr/share/exodia/exodia-welcome/imgs/social-media/youtube.png" alt="YouTube" width="40" height="40">
                </a>
            </div>
            
        </div>
    """.format(self.predator_font.family())
        self.internal_window.updateContent(welcome_text)


    def displayKeybindingContent(self):
        keybinding_text = """
        <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Keybinding</h1>
        
                <h2 align="center" >Bspwm</h2>
              
                <div style="align: center; padding: 20px">
                    <img src="/usr/share/exodia/exodia-welcome/imgs/Keybinding/bspwm.png">
                </div>
                
            </div>
        """.format(self.predator_font.family())
        self.internal_window.updateContent(keybinding_text)


    def displayDevelopersContent(self):
        developers_text = """
            
            <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px;">
                                
                <table style="margin: 20px 0;">
                    <tr>
                        
                        <td style="text-align: left;">
                            <img src="/usr/share/exodia/exodia-welcome/imgs/creator/Ozil.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%;">
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h2 style="color: #FFFFFF; font-size: 28px; margin: 0;">Mahmoud Mohamed</h2>
                            <br/>
                            <h4 style="color: #00C8B0; margin-top: 0px;">DevOps/MLOps Engineer</h4>
                        </td>
                        
                        <td style="padding-left: 20px;">
                            <h4 style="color: #00C8B0; font-size: 28px;">Ozil</h4>
                        </td>
                        
                    </tr>
                </table>
                                
                <ul style="list-style-type: none; padding-left: 0;">
                         
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>I am a Junior DevOps and MLOps Engineer.</strong> 
                    </li>
                
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Graduated from Faculty of Computers and Artificial Intelligence, Information Technology (IT) Department.</strong>
                    </li>
                                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>I am a Linux enthusiast with substantial experience, and I proudly present my Linux distribution, Exodia OS.</strong>
                    </li>
                                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>My expertise extends to the realm of CyberSecurity, where I have a background in PNPT, mobile app penetration testing, web app testing, and security.</strong>
                    </li>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Additionally, I am delving into the field of machine learning and currently expanding my knowledge in this area.</strong>
                    </li>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>As a supporter of Free and Open Source Software (FOSS), I have made some minor contributions to various projects.</strong>
                    </li>
                    
                    <li style="padding: 10px; border-bottom: 1px solid #00C8B0;">
                         <strong>Hardware Enthusiast & Acer Predator fanboy.</strong>
                    </li>
            
                </ul>
                
                <br>
                
                
            </div>
        """.format(self.predator_font.family())
        self.internal_window.updateContent(developers_text)

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
                <img src="/usr/share/exodia/exodia-assistant/icons/exodia-cyan.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
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
                    <img src="/usr/share/exodia/exodia-assistant/imgs/desktop.png" alt="Exodia OS Desktop" width="785" height="320" style="border: 2px solid #00C8B0; border-radius: 10px; max-width: 100%; height: auto;">
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
                
                <h2 style="color: #00C8B0; font-size: 28px; margin-top: 30px;">Showcases:</h2>
                
                <div style="text-align: left; padding: 20px;">
                    
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Showcase/1.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                    <br/>
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Showcase/2.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                    <br/>
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Showcase/3.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                    <br/>
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Showcase/4.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                    <br/>
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Showcase/5.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                    <br/>
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Showcase/6.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                    <br/>
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Showcase/7.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                    
                </div>
            
            </div>
    """.format(self.predator_font.family())  # Use the custom font family
        self.internal_window.updateContent(welcome_text)

    def displayKeybindingContent(self):
        keybinding_text = """
        <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
                
                <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Keybinding</h1>
                
                <p style="font-size: 20px">
                    Keybinding refers to the practice of assigning keyboard shortcuts to various actions or commands within the window manager environment. These shortcuts allow users to perform tasks such as opening applications, switching between windows, resizing or moving windows, and executing specific commands, all without needing to use the mouse or navigate through menus.
                </p>
                
                <br/>
                
                <p style="font-size: 20px">
                    Keybinding is highly customizable and can be tailored to suit individual preferences and workflows. Users typically define keybindings in configuration files specific to their chosen window manager, such as:
                </p>
                
                <br/>
                
                <h5 style="color: #FFFFFF;">  <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">~/.config/bspwm/keybinding/sxhkdrc</code> For <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">BSPWM</code></h5>
                <h5 style="color: #FFFFFF;">  <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">~/.config/i3/config</code> For <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">I3WM</code></h5>
                <h5 style="color: #FFFFFF;">  <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">/opt/exodia/dwm/config.def.h</code> For <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">DWM</code></h5>
                
                <br/>
                
                <div style="text-align: left; padding: 20px;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Keybinding/Note.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                </div>
                
                <br/>
                
                <div style="background-color: #00B0C8;"></div>
                
                <br/>
                
                <h2 align="center" >Bspwm</h2>
                
                <h5 style="color: #FFFFFF;">Install</h5>
                <h5 style="color: #FFFFFF;"> For Home Edition <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">install exodia-bspwm</code></h5>
                <h5 style="color: #FFFFFF;"> For Predator Edition <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">install exodia-bspwm-predator</code> </h5>
                <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">mod</code> Is <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">super</code> (window key) </h5>
                
                <br/>
                
                <div style="text-align: left; padding: 20px;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Keybinding/bspwm.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                </div>
                
                <br/>
                
                <div style="background-color: #00B0C8;"></div>
                
                <br/>
                
                <h2 align="center" >I3WM</h2>
                
                <h5 style="color: #FFFFFF;">Install</h5>
                <h5 style="color: #FFFFFF;"> For Home Edition <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">install exodia-i3wm</code></h5>
                <h5 style="color: #FFFFFF;"> For Predator Edition <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">install exodia-i3wm-predator</code> </h5>
                <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">mod</code> Is <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">super</code> (window key) </h5>
                
                <br/>
                
                <div style="text-align: left; padding: 20px;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Keybinding/i3wm.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                </div>
                
                <br/>
                
                <div style="background-color: #00B0C8;"></div>
                
                <br/>
                
                <h2 align="center" >DWM</h2>
                
                <h5 style="color: #FFFFFF;">Install</h5>
                <h5 style="color: #FFFFFF;"> For Home Edition <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">install exodia-dwm</code></h5>
                <h5 style="color: #FFFFFF;"> For Predator Edition <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">install exodia-dwm-predator</code> </h5>
                <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">mod</code> Is <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">super</code> (window key) </h5>
                
                <br/>
                
                <div style="text-align: left; padding: 20px;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/Keybinding/dwm.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
                </div>
                
                
            </div>
        """.format(self.predator_font.family())
        self.internal_window.updateContent(keybinding_text)

    def displayTipsContent(self):
        tips_text = """
    <div style="font-family: {}; color: #00B0C8; line-height: 1.6; font-size: 18px; max-width: 800px; margin: auto; padding: 0 20px;">
    
        <!-- PGP signature Error -->
        <table style="margin: 20px 0;">
            <tr>
                <td style="padding-left: 20px;">
                    <h1 style="color: #FFFFFF; font-size: 32px; margin-bottom: 15px;">PGP signature Error</h1>
                </td>
            </tr>
            <tr>
                <td style="padding-left: 20px;">
                    <h5 style="color: #00B0C8; font-size: 32px; margin-bottom: 15px;">April 5, 2024 · One min read</h5>
                </td>
            </tr>
        </table>
        
        <table style="margin: 20px 0;">
            <tr>
                <!-- Image Cell -->
                <td style="text-align: left; vertical-align: top;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="70" height="70" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                </td>
    
                <!-- Text Cells -->
                <td style="padding-left: 20px; vertical-align: top;">
                    <h4 style="color: #00C8B0; font-size: 15px; margin: 0;">Mahmoud Mohammed</h4>
                    <h5 style="color: #FFFFFF; font-size: 15px; margin-top: 10px;">Team Leader, Core Dev, Release Manager, Package Maintainer</h5>
                </td>
            </tr>
        </table>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/FreePalestine.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <br/>
        
        <!-- PGP Error Resolution Instructions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
            
            <h5 style="color: #FFFFFF;">If you get <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">invalid or corrupted package (PGP signature) error</code>, open up the terminal and do:</h5>
        
        </div>
        
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h5 style="color: #FFFFFF;">  <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">sudo pacman -S archlinux-keyring</code> </h5>
            <h5 style="color: #FFFFFF;">  <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">sudo pacman-key --init</code> </h5>
            <h5 style="color: #FFFFFF;">  <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">sudo pacman-key --populate</code> </h5>
        </div>
        
        <br/>
        <h5 style="color: #FFFFFF;">Not resolved yet? Ok, try this: <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">yay -Syy archlinux-keyring</code> </h5>
        
        
        
        
        <br/>
        <div style="background-color: #00B0C8;"></div>
        
        
        
        <!-- Adding Music -->
        <table style="margin: 20px 0;">
            <tr>
                <td style="padding-left: 20px;">
                    <h1 style="color: #FFFFFF; font-size: 32px; margin-bottom: 15px;">Adding Music</h1>
                </td>
            </tr>
            <tr>
                <td style="padding-left: 20px;">
                    <h5 style="color: #00B0C8; font-size: 32px; margin-bottom: 15px;">April 5, 2024 · One min read</h5>
                </td>
            </tr>
        </table>
        
        <table style="margin: 20px 0;">
            <tr>
                <!-- Image Cell -->
                <td style="text-align: left; vertical-align: top;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="70" height="70" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                </td>
    
                <!-- Text Cells -->
                <td style="padding-left: 20px; vertical-align: top;">
                    <h4 style="color: #00C8B0; font-size: 15px; margin: 0;">Mahmoud Mohammed</h4>
                    <h5 style="color: #FFFFFF; font-size: 15px; margin-top: 10px;">Team Leader, Core Dev, Release Manager, Package Maintainer</h5>
                </td>
            </tr>
        </table>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/FreePalestine.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <br/>
        
        <!-- Add Music Instructions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h5 style="color: #FFFFFF;">you should add your music to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">~/Music</code> directory</h5>
            <h5 style="color: #FFFFFF;"> Open up The Terminal and run <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">ncmpcpp</code> to open Song Browser</h5>
            <h5 style="color: #FFFFFF;"> press <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">2</code> to open Song Browser</h5>
            <h5 style="color: #FFFFFF;"> In browser tab, press <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">u</code> to update the Music Database</h5>
            <h5 style="color: #FFFFFF;"> press <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">SPACE</code> to add the songs in your Playlist</h5>
        </div>
        
        
        
        <br/>
        <div style="background-color: #00B0C8;"></div>



        <!-- Set keyboard Layout -->
        <table style="margin: 20px 0;">
            <tr>
                <td style="padding-left: 20px;">
                    <h1 style="color: #FFFFFF; font-size: 32px; margin-bottom: 15px;">Set keyboard Layout</h1>
                </td>
            </tr>
            <tr>
                <td style="padding-left: 20px;">
                    <h5 style="color: #00B0C8; font-size: 32px; margin-bottom: 15px;">April 5, 2024 · One min read</h5>
                </td>
            </tr>
        </table>
        
        <table style="margin: 20px 0;">
            <tr>
                <!-- Image Cell -->
                <td style="text-align: left; vertical-align: top;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="70" height="70" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                </td>
    
                <!-- Text Cells -->
                <td style="padding-left: 20px; vertical-align: top;">
                    <h4 style="color: #00C8B0; font-size: 15px; margin: 0;">Mahmoud Mohammed</h4>
                    <h5 style="color: #FFFFFF; font-size: 15px; margin-top: 10px;">Team Leader, Core Dev, Release Manager, Package Maintainer</h5>
                </td>
            </tr>
        </table>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/FreePalestine.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <br/>
        
        <!-- PGP Error Resolution Instructions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h5 style="color: #FFFFFF;"> edit <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">~/.config/bspwm/exodia.conf</code></h5>
            <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">nvim ~/.config/bspwm/exodia.conf</code></h5>
            <h5 style="color: #FFFFFF;"> set <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">keyboard-layouts</code> to update the Music Database</h5>
            <h5 style="color: #FFFFFF;"> e.g ( <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">us,ara</code> )</h5>
        </div>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/tips/keyboardLayouts/0.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <!-- older versions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h4 style="color: #FFFFFF;">For <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">v2022.12</code>  Release or less</h4>
            <br/>
            <h5 style="color: #FFFFFF;"> edit <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">bspwmrc</code></h5>
            <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">nvim ~/.config/bspwm/bspwmrc</code> </h5>
            <h5 style="color: #FFFFFF;"> add these lines: </h5>
            <h5 style="color: #FFFFFF;">    <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;"># ----- set keyboard Layout ----- #</code> </h5>
            <h5 style="color: #FFFFFF;">    <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">setxkbmap -layout us,ar  # add 'us,ara'</code> </h5>
            <h5 style="color: #FFFFFF;">    <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">setxkbmap -option 'grp:alt_shift_toggle'  # Alt+Shift -> switch layout #</code> </h5>
            <h5 style="color: #FFFFFF;"> replace <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">us,ara</code> to your language</h5>

        </div>
        
        
        
        <br/>
        <div style="background-color: #00B0C8;"></div>



        <!-- Changing SDDM user picture -->
        <table style="margin: 20px 0;">
            <tr>
                <td style="padding-left: 20px;">
                    <h1 style="color: #FFFFFF; font-size: 32px; margin-bottom: 15px;">Changing SDDM user picture</h1>
                </td>
            </tr>
            <tr>
                <td style="padding-left: 20px;">
                    <h5 style="color: #00B0C8; font-size: 32px; margin-bottom: 15px;">April 5, 2024 · One min read</h5>
                </td>
            </tr>
        </table>
        
        <table style="margin: 20px 0;">
            <tr>
                <!-- Image Cell -->
                <td style="text-align: left; vertical-align: top;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="70" height="70" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                </td>
    
                <!-- Text Cells -->
                <td style="padding-left: 20px; vertical-align: top;">
                    <h4 style="color: #00C8B0; font-size: 15px; margin: 0;">Mahmoud Mohammed</h4>
                    <h5 style="color: #FFFFFF; font-size: 15px; margin-top: 10px;">Team Leader, Core Dev, Release Manager, Package Maintainer</h5>
                </td>
            </tr>
        </table>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/FreePalestine.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <br/>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/tips/sddm/0.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <!-- PGP Error Resolution Instructions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h5 style="color: #FFFFFF;"> copy your pic to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">/usr/share/sddm/faces/</code></h5>
            <h5 style="color: #FFFFFF;"> in my case my pic -> IMG.jpg <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">sudo cp IMG.jpg /usr/share/sddm/faces/</code> </h5>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/sddm/1.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> set pic name to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">username.face.icon</code></h5>
            <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">sudo mv IMG.jpg o0xwolf.face.icon</code></h5>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/sddm/2.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/sddm/3.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h4 style="color: #ffffff; font-size: 32px; margin-bottom: 15px; text-align: center;">Finally!</h4>

            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/sddm/4.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
        </div>
        
        
        
        
        <br/>
        <div style="background-color: #00B0C8;"></div>



        <!-- Create Your Own Theme -->
        <table style="margin: 20px 0;">
            <tr>
                <td style="padding-left: 20px;">
                    <h1 style="color: #FFFFFF; font-size: 32px; margin-bottom: 15px;">Create Your Own Theme</h1>
                </td>
            </tr>
            <tr>
                <td style="padding-left: 20px;">
                    <h5 style="color: #00B0C8; font-size: 32px; margin-bottom: 15px;">April 5, 2024 · One min read</h5>
                </td>
            </tr>
        </table>
        
        <table style="margin: 20px 0;">
            <tr>
                <!-- Image Cell -->
                <td style="text-align: left; vertical-align: top;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="70" height="70" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                </td>
    
                <!-- Text Cells -->
                <td style="padding-left: 20px; vertical-align: top;">
                    <h4 style="color: #00C8B0; font-size: 15px; margin: 0;">Mahmoud Mohammed</h4>
                    <h5 style="color: #FFFFFF; font-size: 15px; margin-top: 10px;">Team Leader, Core Dev, Release Manager, Package Maintainer</h5>
                </td>
            </tr>
        </table>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/FreePalestine.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <br/>
        
        
        <!-- PGP Error Resolution Instructions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h5 style="color: #FFFFFF;">you can easily create your themes with the same steps for all WMs (currently <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">DWM</code> comes with one theme)</h5>
            <h5 style="color: #FFFFFF;"> Go to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">~/.config/bspwm/themes/</code> </h5>
            <h5 style="color: #FFFFFF;"> Copy an existing theme and rename it, eg <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">Ethereum</code> </h5>
            <h5 style="color: #FFFFFF;"> Edit <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">theme.conf</code> </h5>

            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/CreateCustomTheme/1.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> Generate Color Scheme for the theme using <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">python-pywal</code></h5>
            <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">wal -i /usr/share/backgrounds/Etherium.jpg</code></h5>
            
            <br/>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/CreateCustomTheme/GeneratedColorScheme.png" border="0" width=900 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> add the Color Scheme to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">colorScheme</code></h5>
            
            <br/>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/CreateCustomTheme/AddColorScheme.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/CreateCustomTheme/Hint.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> Then Edit <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">polybar</code> config</h5>
            
            <br/>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/CreateCustomTheme/warning.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> Then take a screenshot and save it in the theme directory with name <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">preview.png</code></h5>
            
            <br/>
            
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/CreateCustomTheme/2.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h4 style="color: #ffffff; font-size: 32px; margin-bottom: 15px; text-align: center;">Finally!</h4>

            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/CreateCustomTheme/preview.png" border="0" width=1000 style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
        </div>
        
        
        
        <br/>
        <div style="background-color: #00B0C8;"></div>



        <!-- setup custom monitors config -->
        <table style="margin: 20px 0;">
            <tr>
                <td style="padding-left: 20px;">
                    <h1 style="color: #FFFFFF; font-size: 32px; margin-bottom: 15px;">setup custom monitors config</h1>
                </td>
            </tr>
            <tr>
                <td style="padding-left: 20px;">
                    <h5 style="color: #00B0C8; font-size: 32px; margin-bottom: 15px;">April 5, 2024 · One min read</h5>
                </td>
            </tr>
        </table>
        
        <table style="margin: 20px 0;">
            <tr>
                <!-- Image Cell -->
                <td style="text-align: left; vertical-align: top;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="70" height="70" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                </td>
    
                <!-- Text Cells -->
                <td style="padding-left: 20px; vertical-align: top;">
                    <h4 style="color: #00C8B0; font-size: 15px; margin: 0;">Mahmoud Mohammed</h4>
                    <h5 style="color: #FFFFFF; font-size: 15px; margin-top: 10px;">Team Leader, Core Dev, Release Manager, Package Maintainer</h5>
                </td>
            </tr>
        </table>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/FreePalestine.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <br/>
        
        
        <!-- PGP Error Resolution Instructions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
        
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/monitors/Note.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> use <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">arandr</code> to configure monitors</h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/monitors/1.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> save your configure </h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/monitors/2.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> add configure file path to the <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">monitors-layouts</code> in the <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">monitors-layouts</code> </h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/monitors/4.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            
            
            <br/>
        <div style="background-color: #00B0C8;"></div>



        <!-- setup Polybar Modules -->
        <table style="margin: 20px 0;">
            <tr>
                <td style="padding-left: 20px;">
                    <h1 style="color: #FFFFFF; font-size: 32px; margin-bottom: 15px;">setup Polybar Modules</h1>
                </td>
            </tr>
            <tr>
                <td style="padding-left: 20px;">
                    <h5 style="color: #00B0C8; font-size: 32px; margin-bottom: 15px;">April 5, 2024 · 3 min read</h5>
                </td>
            </tr>
        </table>
        
        <table style="margin: 20px 0;">
            <tr>
                <!-- Image Cell -->
                <td style="text-align: left; vertical-align: top;">
                    <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="70" height="70" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
                </td>
    
                <!-- Text Cells -->
                <td style="padding-left: 20px; vertical-align: top;">
                    <h4 style="color: #00C8B0; font-size: 15px; margin: 0;">Mahmoud Mohammed</h4>
                    <h5 style="color: #FFFFFF; font-size: 15px; margin-top: 10px;">Team Leader, Core Dev, Release Manager, Package Maintainer</h5>
                </td>
            </tr>
        </table>
        
        <div style="text-align: left; padding: 20px;">
            <img src="/usr/share/exodia/exodia-assistant/imgs/FreePalestine.png"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
        </div>
        
        <br/>
        
        
        <!-- PGP Error Resolution Instructions -->
        <div style="padding: 20px; border-radius: 10px; margin-top: 20px;">
        
            <h2 align="left"> weather Module</h2>
        
            <h5 style="color: #FFFFFF;"> create an account on <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">OpenWeatherMap</code> to configure monitors</h5>
            <h5 style="color: #FFFFFF;"> go to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">API</code> page</h5>
            <h5 style="color: #FFFFFF;"> generate an API Key</h5>
            
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/weather/0.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> copy the API Key </h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/weather/1.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> edit <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">~/.config/bspwm/exodia.conf</code> </h5>
            <h5 style="color: #FFFFFF;"> set <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">weather-API</code></h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/weather/2.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> go to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">OpenWeatherMap</code> </h5>
            <h5 style="color: #FFFFFF;"> search for your city</h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/weather/3.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> press on the result</h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/weather/4.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> copy city ID</h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/weather/5.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> edit <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">~/.config/bspwm/exodia.conf</code> </h5>
            <h5 style="color: #FFFFFF;"> set <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">weather-city-ID</code> </h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/weather/6.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> save file and restart polybar ( open terminal <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">bspbar</code> )</h5>
        

            <br/> <br/>
            <h2 align="left"> github-notifications Module</h2>
        
            <h5 style="color: #FFFFFF;"> generate a new <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">Personal access tokens</code> </h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/github/1.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> select the classic</h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/github/2.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> in <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">Note</code> set the name as you like, in <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">Expiration</code> set to <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">No expiration</code></h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/github/3.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> select notifications </h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/github/4.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> copy access tokens </h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/github/5.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">nvim ~/.config/bspwm/exodia.conf</code></h5>
            
            <h5 style="color: #FFFFFF;"> set <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">github-username</code> to your <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">username</code></h5>
            <h5 style="color: #FFFFFF;"> set <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">github-access-token</code> to your <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">accessTokens</code></h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/github/6.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
            <h5 style="color: #FFFFFF;"> save file and restart polybar ( open terminal <code style="background-color: #222222; color: #00B0C8; padding: 2px 4px; border-radius: 4px;">bspbar</code> )</h5>
            <br/>
            <div style="text-align: left; padding: 20px;">
                <img src="/usr/share/exodia/exodia-assistant/imgs/tips/github/github.png" border="0"  style="margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
            </div>
            
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
                            <img src="/usr/share/exodia/exodia-assistant/imgs/team/Ozil.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
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
                            <img src="/usr/share/exodia/exodia-assistant/imgs/team/Budas.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
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
                            <img src="/usr/share/exodia/exodia-assistant/imgs/team/Joe.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
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
                            <img src="/usr/share/exodia/exodia-assistant/imgs/team/DonSom3a.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
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
                
                <br/>
                <div style="background-color: #00B0C8;"></div>
                <br/>
                
                <div style="text-align: center; margin: 20px 0;">
                    <h1 style="color: #00C8B0; font-size: 32px; margin-bottom: 15px;">Community Contributes</h1>
                </div>
                
                <br>
                
                <table style="margin: 20px 0;">
                    <tr>
                    
                        <td style="text-align: left;">
                            <img src="/usr/share/exodia/exodia-assistant/imgs/team/NahianAdnan.png" alt="Ozil" width="115" height="115" style="border: 2px solid #00C8B0; border-radius: 50%; max-width: 100%; height: auto;">
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

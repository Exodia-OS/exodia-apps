#!/bin/python3

#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

import tkinter as tk
from tkinter import ttk


class SettingsTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a label with a border, bigger font, and deep purple color
        label = tk.Label(self, text="Setting", font=("Helvetica", 20), bd=5,
                         relief="groove")
        label.pack(fill='both', padx=10, pady=10)

        # Create a scrollable text widget
        text = tk.Text(self, wrap='word', font=('Helvetica', 14))
        text.pack(side='left', fill='both', expand=True)

        # Add a scrollbar to the text widget
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=text.yview)
        scrollbar.pack(side='right', fill='y')
        text.configure(yscrollcommand=scrollbar.set)

        # Add some sample text to the text widget
        text.insert('end', '\n  this tab setting will be available soon Inshallah.\n \n')
        text.insert('end', '  this tab for helping you to change system config easily like:\n')
        text.insert('end', '    - changing background, themes, icons, etc...\n')
        text.insert('end', '    - polybar.\n')
        text.insert('end', '    - RGB keyboard ( for predator edition).\n')
        text.insert('end', '    - picom config.\n')
        text.insert('end', '    - keybinding.\n')
        text.insert('end', '    - bspwm configurations and appearance setting.\n')
        text.insert('end', '    - auto start exoida-assistant.\n')
        text.insert('end', '    - auto-update for bspwm config from Exodia OS Repos.\n')
        text.insert('end', '    - auto-update for All WMs/DEs/WCs config from Exodia OS Repos.\n')
        text.insert('end', '    - and more.\n\n')
        text.insert('end', '  stay tuned!\n\n')
        text.insert('end', '  thanks for using Exodia OS!  󰣐\n')


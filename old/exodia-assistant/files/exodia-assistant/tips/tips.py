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


class TipsTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a label with a border, bigger font, and deep purple color #
        label = tk.Label(self, text="Tips", font=("Helvetica", 20), bd=5, relief="groove")
        label.pack(fill='both', padx=10, pady=10)

        # Create a frame to hold the canvas and scrollbar #
        canvas_frame = tk.Frame(self)
        canvas_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Create a canvas to hold the text widget #
        canvas = tk.Canvas(canvas_frame)
        canvas.pack(side='left', fill='both', expand=True)

        # Create a vertical scrollbar for the canvas #
        scrollbar = ttk.Scrollbar(canvas_frame, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        # Configure the canvas to use the scrollbar #
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the text widget inside the canvas #
        text_frame = tk.Frame(canvas)

        # Add the tips to the text widget #
        tips_text = tk.Text(text_frame, wrap='word', font=('Helvetica', 11))
        tips_text.insert('end', "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
        tips_text.insert('end', "  Fixing (PGP Signature) or (invalid or corrupted package) Issues:\n\n")
        tips_text.insert('end', "    - Do this:\n\n")
        tips_text.insert('end', "          `sudo pacman-key --populate`\n\n")
        tips_text.insert('end', "    - If the issue persists, try running:\n\n")
        tips_text.insert('end', "          `yay -Syy archlinux-keyring`\n\n")
        tips_text.insert('end', "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
        tips_text.insert('end', "  Fixing GRUB Theme:\n\n")
        tips_text.insert('end', "    - Do this:\n\n")
        tips_text.insert('end', "          `sudo cp -r /usr/share/grub/themes/exodia/ /boot/grub/themes/`\n\n")
        tips_text.insert('end', "    - Then run:\n\n")
        tips_text.insert('end', "          `sudo grub-mkconfig -o /boot/grub/grub.cfg`\n\n")
        tips_text.insert('end', "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
        tips_text.insert('end', "  Set Keyboard Layout:\n\n")
        tips_text.insert('end', "    - Edit `~/.config/bspwm/exodia.conf`\n\n")
        tips_text.insert('end', "    - Then change `keyboard-layouts`\n\n")
        tips_text.insert('end', "    - e.g: `keyboard-layouts = us,ar`\n\n")
        tips_text.insert('end', "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        # Pack the text widget inside the frame and add the frame to the canvas #
        tips_text.pack(side='left', fill='both', expand=True)
        canvas.create_window((50, 50), window=text_frame, anchor='nw')

        # Configure the canvas scroll region #
        text_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))


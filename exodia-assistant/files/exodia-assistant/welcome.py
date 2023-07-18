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
import markdown


class WelcomeTab(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure( padx=10, pady=10)

        # Add label for "About" #
        about_label = tk.Label(self, text="About", font=("Helvetica", 20))
        about_label.pack(padx=10, pady=10)

        # Load and display image #
        try:
            # path = "images/"
            path = "/usr/share/exodia/exodia-assistant/images/"
            image = tk.PhotoImage(file=path + "exodia.png")
            image_label = tk.Label(self, image=image)
            # keep a reference to the image to prevent garbage collection #
            image_label.image = image
            image_label.pack(padx=10, pady=10)
        except tk.TclError as e:
            print(f"Error loading image: {e}")

        # Add description in Markdown #
        description = """

        Exodia OS is a highly customized Arch-based Linux distribution built for and by cybersecurity experts
        and also for daily usage, capable of performing the strongest pen tests and the simplest daily tasks. 
        Even if you're not a cybersecurity fanatic, you'll come to love Exodia OS for its aesthetically pleasing interface, 
        tools, and features. Overall, Exodia OS is a great distro choice for programming and development, 
        operations security, OSINT, and of course daily usage.

        Proudly developed in Egypt 🇪🇬 by Cyb3rTh1eveZ Team.

        Benefits

        - Exodia OS comes with BSPWM (a tiling window manager) and more than 18+ tailor-made fancy themes.
        - Cybersecurity tools are preinstalled on Exodia OS, for all tracks of cybersecurity.
        - Currently, 3 editions exist: Home, Predator, and Wireless (working on the dark edition right now).
        - Currently, 2 window managers are available: BSPWM and DWM, and we will add more DEs, WMs and WCs.
        
        """

        # Convert Markdown to HTML and remove <pre><code> and </code></pre> tags #
        html = markdown.markdown(description).strip()[11:-13]

        # Create scrollable text box for description #
        description_frame = tk.Frame(self)
        description_frame.pack(fill='both', expand=True, padx=10, pady=10)

        canvas = tk.Canvas(description_frame)
        canvas.pack(side='left', fill='both', expand=True)

        scrollbar = tk.Scrollbar(description_frame, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        text_frame = tk.Frame(canvas)
        text_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=text_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        description_label = tk.Label(text_frame, text=html, font=("Helvetica", 12), justify='left')
        description_label.pack(padx=10, pady=10)

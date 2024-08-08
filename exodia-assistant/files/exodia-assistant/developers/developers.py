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
import os
from PIL import Image, ImageTk


class DevelopersTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a label with a border, bigger font, and deep purple color
        label = tk.Label(self, text="Developers", font=("Helvetica", 20), bd=5,
                         relief="groove")
        label.pack(fill='both', padx=10, pady=10)

        # Create a frame to hold the developer box
        developer_frame = tk.Frame(self)
        developer_frame.pack(padx=10, pady=10)

        # Load and display the profile picture
        # path = os.getcwd() + "/developers/images/"
        path = "/usr/share/exodia/exodia-assistant/developers/images/"
        profile_image = Image.open(path + "wolf.png")
        profile_image = profile_image.resize((100, 100), Image.LANCZOS)  # Resize the image
        self.profile_image = ImageTk.PhotoImage(profile_image)

        # Create a canvas to hold the developer picture
        canvas = tk.Canvas(developer_frame, width=profile_image.width,
                           height=profile_image.height,
                           highlightthickness=0)
        canvas.pack(side=tk.LEFT, padx=10)

        # Display the profile picture on the canvas
        canvas.create_image(0, 0, image=self.profile_image, anchor='nw')

        # Create a label to hold the developer information
        info_label = tk.Label(developer_frame, text="\nMahmoud Mohamed  (00xWolf)                                            "
                                                    "                                                 \n"
                                                    "\n-    Team Leader  |     Core Dev  |  󰏖  Package, 󰖟 Web, "
                                                    "󰈬 Docs Maintainer.         \n"
                                                    "\n-    Linux Enthusiast   |     GitHub @mmsaeed509   |  󰀂  "
                                                    "wireless/PenTester.         \n",
                              font=("Helvetica", 12))
        info_label.pack(side=tk.LEFT, padx=10)

        # Create a frame to hold the 2nd developer box
        developer_frame2 = tk.Frame(self)
        developer_frame2.pack(padx=10, pady=10)

        # Load and display the profile picture
        profile_image2 = Image.open(path + "Abdallah.png")
        profile_image2 = profile_image2.resize((100, 100), Image.LANCZOS)  # Resize the image
        self.profile_image2 = ImageTk.PhotoImage(profile_image2)

        # Create a canvas to hold the developer picture
        canvas = tk.Canvas(developer_frame2, width=profile_image2.width,
                           height=profile_image2.height,
                           highlightthickness=0)
        canvas.pack(side=tk.LEFT, padx=10)

        # Display the profile picture on the canvas
        canvas.create_image(0, 0, image=self.profile_image2, anchor='nw')

        # Create a label to hold the developer information
        info_label = tk.Label(developer_frame2, text="\nAbdallah Adham  (0xSkorpioN)                                    "
                                                     "                                                      \n"
                                                     "\n-    Src code review  |     Core Dev   |  󰏖   Package, "
                                                     "󰖟 Web, 󰈬 Docs Maintainer.\n"
                                                     "\n- 󰀂   PenTester/Net-Web security  |     Linux Enthusiast  | "
                                                     "    @AbdallahAdham.",
                              font=("Helvetica", 12))
        info_label.pack(side=tk.LEFT, padx=10)

        # Create a frame to hold the 3rd developer box
        developer_frame3 = tk.Frame(self)
        developer_frame3.pack(padx=10, pady=10)

        # Load and display the profile picture
        profile_image3 = Image.open(path + "omar.png")
        profile_image3 = profile_image3.resize((100, 100), Image.LANCZOS)  # Resize the image
        self.profile_image3 = ImageTk.PhotoImage(profile_image3)

        # Create a canvas to hold the developer picture
        canvas = tk.Canvas(developer_frame3, width=profile_image3.width,
                           height=profile_image3.height,
                           highlightthickness=0)
        canvas.pack(side=tk.LEFT, padx=10)

        # Display the profile picture on the canvas
        canvas.create_image(0, 0, image=self.profile_image3, anchor='nw')

        # Create a label to hold the developer information
        info_label = tk.Label(developer_frame3,
                              text="\nOmar Esmail  (0xSom3aa)                                                           "
                                   "                                         \n"
                                   "\n-    Core Dev   |  󰏖   Package, 󰖟 Web, 󰈬 Docs Maintainer.                   "
                                   "                     \n"
                                   "\n-    Linux Enthusiast  |     @OmarEsmail211.                                  "
                                   "                              ",
                              font=("Helvetica", 12))
        info_label.pack(side=tk.LEFT, padx=10)

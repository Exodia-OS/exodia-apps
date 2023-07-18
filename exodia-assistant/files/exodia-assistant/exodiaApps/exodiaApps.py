#!/bin/python3

#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################


import webbrowser
import tkinter as tk
from tkinter import ttk
import os


def open_tui_apps(button_frame=None):
    # Create a new frame for the TUI Apps section
    tui_frame = tk.Frame(button_frame, bg="#8D8D93", borderwidth=0)

    # Create buttons for the TUI Apps section
    list_button = ttk.Button(tui_frame, text="List", style="Custom.TButton",
                             command=lambda: os.system("pacman -Sg Exodia-TUI-Apps; read -p 'Press enter to continue'"))
    install_button = ttk.Button(tui_frame, text="Install", style="Custom.TButton",
                                command=lambda: os.system(
                                    "sudo pacman -S Exodia-TUI-Apps; read -p 'Press enter to continue'"))
    uninstall_button = ttk.Button(tui_frame, text="Uninstall", style="Custom.TButton",
                                  command=lambda: os.system(
                                      "sudo pacman -Rs Exodia-TUI-Apps; read -p 'Press enter to continue'"))

    # Pack the buttons into the TUI Apps frame
    list_button.pack(side="left", padx=20, pady=10)
    install_button.pack(side="left", padx=20, pady=10)
    uninstall_button.pack(side="left", padx=20, pady=10)

    # Pack the TUI Apps frame into the button frame
    tui_frame.pack(padx=20, pady=20)


def open_about_exodia_os():
    # TODO: Implement function to open about-exodia-os
    os.system("about-exodia-os")
    pass


def run_gparted():
    # TODO: Implement function to run GParted
    os.system("/usr/bin/gparted")
    pass


def open_discord():
    webbrowser.open("https://discord.com/invite/wPDyfR5AV9")


def open_telegram():
    webbrowser.open("https://t.me/exodia_os")


def open_github():
    webbrowser.open("https://github.com/Exodia-OS")


def open_youtube():
    webbrowser.open("https://www.youtube.com/@mahmoudmohammed00xwolf88/videos")


class ExodiaAppsTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a label with a border, bigger font, and deep purple color
        label = tk.Label(self, text="󰀻  Exodia OS Apps & Packages 󰏖", 
                         font=("Helvetica", 20), bd=5, relief="groove")

        label.pack(fill='both', padx=10, pady=10)

        # Load images for the buttons
        path = "/usr/share/exodia/exodia-assistant/images/"
        # path = os.getcwd() + "/images/"
        self.tui_icon = tk.PhotoImage(file=os.path.join(path, "exodia-cyan.png")).subsample(5)
        self.exodia_icon = tk.PhotoImage(file=os.path.join(path, "exodia.png")).subsample(5)
        self.gparted_icon = tk.PhotoImage(file=os.path.join(path, "gparted.png")).subsample(1)
        self.discord_icon = tk.PhotoImage(file=os.path.join(path, "discord.png")).subsample(5)
        self.telegram_icon = tk.PhotoImage(file=os.path.join(path, "tg.png")).subsample(2)
        self.github_icon = tk.PhotoImage(file=os.path.join(path, "gh.png")).subsample(5)
        self.youtube_icon = tk.PhotoImage(file=os.path.join(path, "youtube.png")).subsample(8)

        # Create a custom style with a background for the buttons #
        style = ttk.Style()
        style.configure("Custom.TButton", background="#8D8D93")

        # Create a frame for the buttons with a border size of 5
        button_frame = tk.Frame(self, bg="#8D8D93", borderwidth=0)

        # Create buttons with icons
        tui_button = ttk.Button(button_frame, text="TUI Apps", image=self.tui_icon,
                                compound="top", command=lambda: open_tui_apps(button_frame),
                                style="Custom.TButton")
        exodia_button = ttk.Button(button_frame, text="Release", image=self.exodia_icon,
                                   compound="top", command=open_about_exodia_os,
                                   style="Custom.TButton")
        gparted_button = ttk.Button(button_frame, text="GParted", image=self.gparted_icon,
                                    compound="top", command=run_gparted,
                                    style="Custom.TButton")
        discord_button = ttk.Button(button_frame, text="Discord", image=self.discord_icon,
                                    compound="top", command=open_discord,
                                    style="Custom.TButton")
        telegram_button = ttk.Button(button_frame, text="Telegram", image=self.telegram_icon,
                                     compound="top", command=open_telegram,
                                     style="Custom.TButton")
        github_button = ttk.Button(button_frame, text="GitHub", image=self.github_icon,
                                   compound="top", command=open_github,
                                   style="Custom.TButton")
        youtube_button = ttk.Button(button_frame, text="YouTube", image=self.youtube_icon,
                                    compound="top", command=open_youtube,
                                    style="Custom.TButton")

        # Pack buttons into the frame
        # tui_button.pack(side="left", padx=20, pady=10)
        exodia_button.pack(side="left", padx=20, pady=10)
        gparted_button.pack(side="left", padx=20, pady=10)
        discord_button.pack(side="left", padx=20, pady=10)
        telegram_button.pack(side="left", padx=20, pady=10)
        github_button.pack(side="left", padx=20, pady=10)
        youtube_button.pack(side="left", padx=20, pady=10)

        # Pack the button frame into the main frame
        button_frame.pack(padx=20, pady=20)

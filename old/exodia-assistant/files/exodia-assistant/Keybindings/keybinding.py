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
import os
import markdown
from bs4 import BeautifulSoup


class KeybindingTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the notebook to hold the tabs #
        # notebook = tk.ttk.Notebook(self, style='My.TNotebook')
        notebook = tk.ttk.Notebook(self)
        style = ttk.Style()
        style.configure(
            'My.TNotebook', relief="groove")

        ## Create the bspwm tab ##
        bspwm_tab = tk.Frame(notebook)
        bspwm_tab.pack(fill='both', expand=True)
        notebook.add(bspwm_tab, text='bspwm')

        # Create the label with a border, bigger font, and deep purple color #
        label = tk.Label(
            bspwm_tab, text="Exodia OS bspwm Keybindings ⌨️ ",
            font=("Helvetica", 20), bd=5, relief="groove")
        label.pack(fill='both', padx=10, pady=10)

        # Read in the bspwm Markdown file and convert to HTML #
        PATH = "/usr/share/exodia/exodia-assistant/Keybindings/MDs/"
        # PATH = os.getcwd() + "/Keybindings/MDs/"
        with open(PATH + "bspwm.md", "r") as f:
            html = markdown.markdown(f.read())

        # Use BeautifulSoup to extract the text without the <p> tags #
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        # Create a Text widget to display the text #
        html_label = tk.Text(bspwm_tab, wrap='word', padx=10, pady=10)
        html_label.insert('end', text)
        html_label.configure(state='disabled')
        html_label.pack(fill='both', expand=True)

        # Add a scrollbar for the Text widget #
        scrollbar = tk.Scrollbar(bspwm_tab, command=html_label.yview)
        scrollbar.pack(side='right', fill='y')
        html_label.configure(yscrollcommand=scrollbar.set)


        ## --------------- New Tab --------------- ##


        ## Create the dwm tab ##
        dwm_tab = tk.Frame(notebook)
        dwm_tab.pack(fill='both', expand=True)
        notebook.add(dwm_tab, text='dwm')

        # Create the label with a border, bigger font, and deep purple color #
        label = tk.Label(
            dwm_tab, text="Exodia OS dwm Keybindings ⌨️ ",
            font=("Helvetica", 20), bd=5, relief="groove")
        label.pack(fill='both', padx=10, pady=10)

        # Read in the dwm Markdown file and convert to HTML #
        with open(PATH + "dwm.md", "r") as f:
            html = markdown.markdown(f.read())

        # Use BeautifulSoup to extract the text without the <p> tags #
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        # Create a Text widget to display the text #
        html_label = tk.Text(dwm_tab, wrap='word', padx=10, pady=10)
        html_label.insert('end', text)
        html_label.configure(state='disabled')
        html_label.pack(fill='both', expand=True)

        # Add a scrollbar for the Text widget #
        scrollbar = tk.Scrollbar(dwm_tab, command=html_label.yview)
        scrollbar.pack(side='right', fill='y')
        html_label.configure(yscrollcommand=scrollbar.set)

        ## --------------- New Tab --------------- ##

        ## Create the i3 tab ##
        i3wm_tab = tk.Frame(notebook)
        i3wm_tab.pack(fill='both', expand=True)
        notebook.add(i3wm_tab, text='i3WM')

        # Create the label with a border, bigger font, and deep purple color #
        label = tk.Label(
            i3wm_tab, text="Exodia OS i3WM Keybindings ⌨️ ",
            font=("Helvetica", 20), bd=5, relief="groove")
        label.pack(fill='both', padx=10, pady=10)

        # Read in the i3wm Markdown file and convert to HTML #
        with open(PATH + "i3wm.md", "r") as f:
            html = markdown.markdown(f.read())

        # Use BeautifulSoup to extract the text without the <p> tags #
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        # Create a Text widget to display the text #
        html_label = tk.Text(i3wm_tab, wrap='word', padx=10, pady=10)
        html_label.insert('end', text)
        html_label.configure(state='disabled')
        html_label.pack(fill='both', expand=True)

        # Add a scrollbar for the Text widget #
        scrollbar = tk.Scrollbar(i3wm_tab, command=html_label.yview)
        scrollbar.pack(side='right', fill='y')
        html_label.configure(yscrollcommand=scrollbar.set)

        ## --------------- New Tab --------------- ##

        ## Create the `WMs\WCs` tab ##

        # Pack the notebook #
        notebook.pack(fill='both', expand=True)

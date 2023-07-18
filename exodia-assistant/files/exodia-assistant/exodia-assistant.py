#!/bin/python3

#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

# importing Tabs/libs/classes #
import tkinter as tk
from tkinter import ttk
from settings.settings import SettingsTab
from welcome import WelcomeTab
from Keybindings.keybinding import KeybindingTab
from tips.tips import TipsTab
from developers.developers import DevelopersTab
from exodiaApps.exodiaApps import ExodiaAppsTab

# Create a window #
window = tk.Tk()
window.title("Exoida OS Assistant")
window.geometry("1000x800")
window.configure(borderwidth=5)
window.config(highlightbackground='#8D8D93', highlightcolor='#8D8D93', highlightthickness=5)

# Create a label #
label_empty_1 = tk.Label(window)
label_empty_1.pack()

label = tk.Label(
    window, text=" Exoida OS Assistant ",
    font=("Helvetica", 15),
    bd=5, relief="groove")

label.pack()

label_empty_2 = tk.Label(window)
label_empty_2.pack()

# Create a notebook #
notebook = ttk.Notebook(window, style='My.TNotebook')
style = ttk.Style()
style.configure(
    'My.TNotebook', background='#1A1B26',
    tabposition='n', tabmargins=[2, 2, 0, 0],
    tab=('#53545C',), borderwidth=5)

# Change the color of the selected tab #
style.map('TNotebook.Tab', background=[('selected', '#8D8D93')])

notebook.pack(expand=True, fill='both')

# Create tabs #
welcome_tab = WelcomeTab(notebook)
keybinding_tab = KeybindingTab(notebook)
tips_tab = TipsTab(notebook)
setting_tab = SettingsTab(notebook)
developers_tab = DevelopersTab(notebook)
exodia_apps_tab = ExodiaAppsTab(notebook)

# Add tabs to the notebook #
notebook.add(welcome_tab, text="Welcome")
notebook.add(keybinding_tab, text="Keybinding")
notebook.add(tips_tab, text="Tips")
notebook.add(setting_tab, text="Setting")
notebook.add(developers_tab, text="Developers")
notebook.add(exodia_apps_tab, text="Exodia OS Apps")

# Create a close button #
style = ttk.Style()
style.configure(
    'Close.TButton', background='#1A1B26',
    foreground='red', padding=2)

style.map(
    'Close.TButton',
    background=[('active', '#53545C')],
    foreground=[('active', 'red')])

close_button = ttk.Button(
    window, text="✘", command=window.destroy,
    style='Close.TButton', width=5)

close_button.place(relx=1, x=-10, y=10, anchor="ne")

# Bind the Enter and Leave events to change the button style
close_button.bind("<Enter>", lambda e: close_button.state(['active']))
close_button.bind("<Leave>", lambda e: close_button.state(['!active']))

# Run the window #
window.mainloop()

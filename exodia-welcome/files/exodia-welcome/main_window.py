###############################################################################
#
# =================================================================
# =          Authors: Brad Heffernan & Erik Dubois                =
# =================================================================
#
#    Rebuilt For Exodia OS
#
#     Developer : Mahmoud Mohamed (00xWolf)
#     GitHub : @mmsaeed509
#    󰊫 Gmail : @mmsaeed509
#
###############################################################################

import os
import getpass
from os.path import expanduser

DEBUG = False
#DEBUG = True

base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()

if DEBUG:
    user = username
else:
    user = "liveuser"

Settings = home + "/.config/exodia-welcome/settings.conf"

def GUI(self, Gtk, GdkPixbuf):

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    self.cc = Gtk.Label()
    label = Gtk.Label(xalign=0)
    label.set_markup("<big>Welcome to <b>Exodia OS</b></big>")
    label.set_line_wrap(True)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    label2.set_markup(
        "" + 
        "<big>\nA highly customized <b>arch-based</b> distro For All Cybersecurity fields.\n" +
        "It comes with other special editions as well.\n" +
        "We advise to clean the computer with <b>Gparted</b> before installing. </big>\n")
   

    hbox4.set_center_widget(label2)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)

    # ======================================================================
    #                   MAIN BUTTONS
    # ======================================================================

    button1 = Gtk.Button(label="")
    button1_label = button1.get_child()
    button1_label.set_markup("<span size='large'><b>Run GParted</b></span>")
    button1.connect("clicked", self.on_gp_clicked)
    button1.set_size_request(0, 40)

    button_assistant = Gtk.Button(label="")
    button_assistant_lable = button_assistant.get_child()
    button_assistant_lable.set_markup("<span size='large'><b>Exodia OS Assistant</b></span>")
    button_assistant.connect("clicked", self.on_assistant_clicked)
    button_assistant.set_size_request(0, 40)

    self.button8 = Gtk.Button(label="")
    button8_label = self.button8.get_child()
    button8_label.set_markup("<span size='large'><b>Update Arch Linux mirrors</b></span>")
    self.button8.connect("clicked", self.on_mirror_clicked)
    self.button8.set_size_request(0, 40)

    button2 = Gtk.Button(label="")
    button2_label = button2.get_child()
    button2_label.set_markup("<span size='large'><b>Install Exoida OS</b></span>")
    button2.connect("clicked", self.on_ai_clicked)
    button2.set_size_request(0, 40)
    
    grid = Gtk.Grid()
    grid.set_column_spacing(10)
    grid.set_row_spacing(10)
    grid.attach(self.button8,     2, 0, 2, 2)
    grid.attach(button1,          0, 3, 2, 2)
    grid.attach(button_assistant, 2, 3, 2, 2)
    grid.attach(button2,          4, 3, 2, 2)
    grid.set_column_homogeneous(True)
    grid.set_row_homogeneous(True)

    # ======================================================================
    #                   USER INFO
    # ======================================================================

    lblusrname = Gtk.Label(xalign=0)
    lblusrname.set_text("User:")

    lblpassword = Gtk.Label(xalign=0)
    lblpassword.set_text("Pass:")

    lblusr = Gtk.Label(xalign=0)
    lblusr.set_text("liveuser  |")

    lblpass = Gtk.Label(xalign=0)
    lblpass.set_markup("<i>No Password</i>")

    hboxUser = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hboxUser.pack_start(lblusrname, False, False, 0)
    hboxUser.pack_start(lblusr, False, False, 0)

    hboxUser.pack_start(lblpassword, False, False, 0)
    hboxUser.pack_start(lblpass, False, False, 0)

    # ======================================================================
    #                   FOOTER BUTTON LINKS
    # ======================================================================

    # change this one every year
    button3 = Gtk.Button(label="")
    button3_label = button3.get_child()
    button3_label.set_markup("<b>wiki</b>")
    button3.connect("clicked", self.on_link_clicked,
                    "https://exodia-os.github.io/exodia-website/quickstart/install")
    button3.set_size_request(180, 50)

    button4 = Gtk.Button(label="")
    button4_label = button4.get_child()
    button4_label.set_markup("<b>Keybinding</b>")
    button4.connect("clicked", self.on_link_clicked,
                    "https://exodia-os.github.io/exodia-website/Keybinding")
    button4.set_size_request(180, 50)

    button5 = Gtk.Button(label="")
    button5_label = button5.get_child()
    button5_label.set_markup("<b>Home</b> releases info")
    button5.connect("clicked", self.on_link_clicked,
                    "https://github.com/Exodia-OS/exodia-home-ISO/releases")
    button5.set_size_request(180, 50)

    button6 = Gtk.Button(label="")
    button6_label = button6.get_child()
    button6_label.set_markup("<b>Predator</b> releases info")
    button6.connect("clicked", self.on_link_clicked,
                    "https://github.com/Exodia-OS/exodia-predator-ISO/releases")
    button6.set_size_request(180, 50)

    button7 = Gtk.Button(label="")
    button7_label = button7.get_child()
    button7_label.set_markup("<b>Wireless</b> releases info")
    button7.connect("clicked", self.on_link_clicked,
                    "https://github.com/Exodia-OS/exodia-wireless-ISO/releases")
    button7.set_size_request(180, 50)
    

    button8 = Gtk.Button(label="")
    button8_label = button8.get_child()
    button8_label.set_markup("<b>Dark</b> releases info")
    button8.connect("clicked", self.on_link_clicked,
                    "https://github.com/Exodia-OS/exodia-dark-ISO/releases")


    button12 = Gtk.Button(label="Quit")
    button12.set_size_request(200, 50)
    button12.connect("clicked", Gtk.main_quit)

    button70 = Gtk.Button(label="Screen resolution")
    button70.set_size_request(180, 50)
    button70.set_property("has-tooltip", True)
    button70.connect("query-tooltip",
                      self.tooltip_callback,
                      "Launch Arandr")
    button70.connect("clicked", self.on_buttonarandr_clicked)

    hbox2.pack_start(button5, True, True, 0)
    hbox2.pack_start(button6, True, True, 0)
    hbox2.pack_start(button7, True, True, 0)
    hbox2.pack_start(button8, True, True, 0)

    hbox5.pack_start(button3, True, True, 0)
    hbox5.pack_start(button4, True, True, 0)
    hbox5.pack_start(button70, True, True, 0)
    hbox5.pack_start(button12, True, True, 0)

    # ======================================================================
    #                   SOCIAL LINKS
    # ======================================================================

    fbE = Gtk.EventBox()
    tE = Gtk.EventBox()
    reddit = Gtk.EventBox()
    inE = Gtk.EventBox()
    liE = Gtk.EventBox()
    gh = Gtk.EventBox()
    yE = Gtk.EventBox()
    dE = Gtk.EventBox()
    tgE = Gtk.EventBox()
    Egh = Gtk.EventBox()

    pbfb = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/facebook.png'), 28, 28)
    fbimage = Gtk.Image().new_from_pixbuf(pbfb)

    pbt = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/twitter.png'), 28, 28)
    timage = Gtk.Image().new_from_pixbuf(pbt)

    pbme = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/reddit.png'), 23, 23)
    meimage = Gtk.Image().new_from_pixbuf(pbme)

    pbin = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/insta.png'), 28, 28)
    inimage = Gtk.Image().new_from_pixbuf(pbin)

    pbli = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/linkedin.png'), 28, 28)
    liimage = Gtk.Image().new_from_pixbuf(pbli)

    pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/gh.png'), 28, 28)
    pimage = Gtk.Image().new_from_pixbuf(pbp)

    pby = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/youtube.png'), 28, 28)
    yimage = Gtk.Image().new_from_pixbuf(pby)

    pbd = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/discord.png'), 28, 28)
    dimage = Gtk.Image().new_from_pixbuf(pbd)

    pbtg = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/tg.png'), 28, 28)
    tgimage = Gtk.Image().new_from_pixbuf(pbtg)

    pbel = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, '/usr/share/exodia/exodia-welcome/images/gh.png'), 28, 28)
    elimage = Gtk.Image().new_from_pixbuf(pbel)

    fbE.add(fbimage)
    tE.add(timage)
    reddit.add(meimage)
    inE.add(inimage)
    liE.add(liimage)
    gh.add(pimage)
    yE.add(yimage)
    dE.add(dimage)
    tgE.add(tgimage)
    Egh.add(elimage)

    fbE.connect("button_press_event", self.on_social_clicked,
                "https://www.facebook.com/engrody.linux.5")
    tE.connect("button_press_event", self.on_social_clicked,
               "https://twitter.com/Mahmoudzil4")
    reddit.connect("button_press_event", self.on_social_clicked,
                "https://www.reddit.com/user/mmsaeed509")
    inE.connect("button_press_event", self.on_social_clicked,
                "https://www.instagram.com/mmsaeed509/")
    liE.connect("button_press_event", self.on_social_clicked,
                "https://www.linkedin.com/in/mahmoud-mohamed-a934b21a5/")
    gh.connect("button_press_event", self.on_social_clicked,
               "https://github.com/mmsaeed509")
    yE.connect("button_press_event", self.on_social_clicked,
               "https://www.youtube.com/@mahmoudmohammed00xwolf88/videos")
    dE.connect("button_press_event", self.on_social_clicked,
               "https://discord.gg/wPDyfR5AV9")
    tgE.connect("button_press_event", self.on_social_clicked,
                "https://t.me/exodia_os")
    Egh.connect("button_press_event", self.on_social_clicked,
                "https://github.com/Exodia-OS")

    fbE.set_property("has-tooltip", True)
    tE.set_property("has-tooltip", True)
    reddit.set_property("has-tooltip", True)
    inE.set_property("has-tooltip", True)
    liE.set_property("has-tooltip", True)
    gh.set_property("has-tooltip", True)
    yE.set_property("has-tooltip", True)
    dE.set_property("has-tooltip", True)
    tgE.set_property("has-tooltip", True)
    Egh.set_property("has-tooltip", True)

    fbE.connect("query-tooltip", self.tooltip_callback, "Facebook")
    tE.connect("query-tooltip", self.tooltip_callback, "Twitter")
    reddit.connect("query-tooltip", self.tooltip_callback, "reddit")
    inE.connect("query-tooltip", self.tooltip_callback, "Instagram")
    liE.connect("query-tooltip", self.tooltip_callback, "LinkedIn")
    gh.connect("query-tooltip", self.tooltip_callback, "GitHub")
    yE.connect("query-tooltip", self.tooltip_callback, "Youtube")
    dE.connect("query-tooltip", self.tooltip_callback, "Discord")
    tgE.connect("query-tooltip", self.tooltip_callback, "Telegram")
    Egh.connect("query-tooltip", self.tooltip_callback, "Exodia OS GitHub")

    # hbox3.pack_start(fbE, False, False, 0)
    hbox3.pack_start(tE, False, False, 0)
    hbox3.pack_start(reddit, False, False, 0)
    hbox3.pack_start(inE, False, False, 0)
    # hbox3.pack_start(liE, False, False, 0)
    hbox3.pack_start(gh, False, False, 0)

    hbox6.pack_start(Egh, False, False, 0)
    hbox6.pack_start(yE, False, False, 0)
    hbox6.pack_start(dE, False, False, 0)
    hbox6.pack_start(tgE, False, False, 0)
    hbox3.pack_start(hbox6, True, False, 0)

    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================

    self.vbox.pack_start(hbox1, False, False, 7)  # Logo
    self.vbox.pack_start(hbox4, False, False, 7)  # welcome Label
    self.vbox.pack_start(hbox8, False, False, 7)  # warning Label
    self.vbox.pack_start(grid, True, False, 7)  # Run GParted/Calamares
    self.vbox.pack_end(hbox3, False, False, 0)  # Footer
    self.vbox.pack_end(hbox5, False, False, 7)  # Buttons
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons

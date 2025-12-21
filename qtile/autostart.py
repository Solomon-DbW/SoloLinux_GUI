import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen(["gammastep", "-O", "2200"])
    subprocess.Popen(["redshift", "-O", "4000"])
    subprocess.Popen(["feh", "--bg-scale", f"{home}/Pictures/wallpapers/arch_syle.jpeg"])
    subprocess.Popen(["xinput", "set-prop", "13", "libinput Tapping Enabled", "1"])

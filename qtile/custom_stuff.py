from libqtile import bar, layout, qtile, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile.widget import backlight
import subprocess
from libqtile import popup
from libqtile.widget.base import ThreadPoolText

def get_pipewire_volume():
    try:
        output = subprocess.check_output(
            "wpctl get-volume @DEFAULT_AUDIO_SINK@", shell=True
        ).decode("utf-8").strip()

        parts = output.split()
        volume = float(parts[1]) * 100
        muted = "MUTED" in output

        vol_text = f" {int(volume)}%" if volume < 5 else f" {int(volume)}%" if volume < 50 else f" {int(volume)}%"
        if muted:
            vol_text = " Mute"
        return f"  {vol_text}"
    except Exception as e:
        return "Vol: Error"

def volume_up():
    subprocess.call("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+", shell=True)

def volume_down():
    subprocess.call("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-", shell=True)

def toggle_mute():
    subprocess.call("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle", shell=True)

pipewire_volume_widget = widget.GenPollText(
    update_interval=1,
    func=get_pipewire_volume,
    mouse_callbacks={
        "Button1": toggle_mute,   # Left click
        "Button4": volume_up,     # Scroll up
        "Button5": volume_down,   # Scroll down
    },
)



@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen(["gammastep", "-O", "2200"])
    subprocess.Popen(
        ["feh", "--bg-scale", f"{home}/Pictures/wallpapers/arch_syle.jpeg"]
    )
    subprocess.Popen(["xinput", "set-prop", "13", "libinput Tapping Enabled", "1"])



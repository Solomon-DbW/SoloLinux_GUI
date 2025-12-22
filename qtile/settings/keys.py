from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # ========== APPLICATION LAUNCHERS ==========
    Key([mod], "s", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("emacs --init-directory ~/.config/emacs"), desc="Launch Emacs"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave browser"),
    Key([mod], "v", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "r", lazy.spawn("rofi -show drun -theme dmenu"), desc="Launch Rofi"),

    # ========== SYSTEM CONTROLS ==========
    Key([], "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl set 1%- && notify-send 'Brightness down'"),
        desc="Decrease brightness"),
    Key([], "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl set 1%+"),
        desc="Increase brightness"),
    Key([], "XF86AudioLowerVolume", 
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
        desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", 
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+"),
        desc="Raise volume"),
    Key([], "XF86AudioMute", 
        lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
        desc="Mute/unmute"),

    # ========== WINDOW FOCUS ==========
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # ========== MOVE WINDOWS ==========
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # ========== RESIZE WINDOWS ==========
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # ========== LAYOUT MANAGEMENT ==========
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), 
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), 
        desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"),

    # ========== QTILE CONTROLS ==========
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# VT switching for Wayland
def init_vt_keys():
    vt_keys = []
    for vt in range(1, 8):
        vt_keys.append(
            Key(
                ["control", "mod1"],
                f"f{vt}",
                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT{vt}",
            )
        )
    return vt_keys

keys.extend(init_vt_keys())

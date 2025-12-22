from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import backlight
from libqtile.widget.base import ThreadPoolText


from custom_volume import pipewire_volume_widget
from autostart import autostart

# from qtile.unicode_chars import lower_left_triangle
from unicode_chars import (
    left_half_circle,
    right_half_circle,
    lower_left_triangle,
    left_arrow,
    right_arrow,
)


mod = "mod4"
terminal = guess_terminal()

autostart()

colors = {
    "bg": "#1e1e2e",           # Base background
    "fg": "#cdd6f4",           # Text
    "accent1": "#89b4fa",      # Blue
    "accent2": "#f38ba8",      # Red
    "accent3": "#a6e3a1",      # Green
    "accent4": "#f9e2af",      # Yellow
    "accent5": "#cba6f7",      # Mauve
    "surface0": "#313244",     # Slightly lighter than bg
    "surface1": "#45475a",     # Even lighter
    "surface2": "#585b70",     # Border colors
}

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    Key([mod], "s", lazy.spawn(terminal), desc="Launch terminal"),  # Changed from Return to 's'
    Key([mod], "e", lazy.spawn("emacs --init-directory ~/.config/emacs"), desc="Launch Emacs"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave browser"),
    Key([mod], "v", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "r", lazy.spawn("rofi -show drun -theme dmenu"), desc="Launch Rofi"),


    # Brightness down
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 1%- && notify-send 'Brightness up'"),
    ),
    # Brightness up
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 1%+")),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+"),
    ),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Key([mod], "rs", lazy.spawn("redshift -O 4000"), desc="Move focus to left"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Key([mod], "r", lazy.spawn("rofi -show drun -theme dmenu")),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "border_width": 3,
    "margin": 15,
    "border_focus": "CCCCCC",
    "border_normal": "595959",
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                pipewire_volume_widget,
                right_arrow("555555", "000000"),
                widget.CPU(
                    background="555555",
                    format="     {freq_current}GHz CPU Load:{load_percent}%",
                ),

                right_arrow("000000", "555555"),

                widget.CPUGraph(
                    graph_color="#555555",
                    fill_color="#555555",  # Optional: for the area under the line
                    border_color="#555555",  # Optional: border of the widget
                ),

                right_arrow("555555", "000000"),

                widget.CheckUpdates(background="555555"),

                right_arrow("000000", "555555"),

                widget.GroupBox(
                    highlight_method="block", this_current_screen_border="#555555"
                ),

                widget.TextBox(
                    text="  SoloLinux",
                    fontsize=14,
                    foreground=colors["accent1"],
                    padding=10,
                ),

                right_arrow("555555", "000000"),

                widget.CapsNumLockIndicator(),

                # widget.CheckUpdates(distro="Arch"),

                widget.WindowName(
                    background="555555",
                    # format="{name:.30}",  # Limits title to 30 characters
                    format="{name}",
                    max_chars=50,  # Optional: max number of characters before cutting off
                    width=300,  # Set a fixed width
                ),

                widget.CheckUpdates(
                    distro="Arch",
                    display_format="Up: {updates}",
                    no_update_string="Up: 0",
                    background=colors["surface0"],
                    colour_have_updates=colors["accent4"],
                    colour_no_updates=colors["accent3"],
                    padding=8,
                ),

                widget.Prompt(
                 foreground = "0000ff"
                ),


                left_arrow("555555", "000000"),

                widget.Backlight(
                    backlight_name="amdgpu_bl1", # Changed from intel_backlight
                    format="Brightness: {percent:1.0%}",
                    background="000000",
                ),

                left_arrow("000000", "555555"),

                widget.Battery(
                    format='{char} {percent:2.0%}',
                    charge_char='⚡',
                    discharge_char='🔋',
                    full_char='✓',
                    update_interval=60,
                    background="555555"
                ),

                left_arrow("555555", "000000"),

                widget.Clock(format="󰃭  %d/%m/%Y | 󱑍  %a %I:%M %p"),
                left_arrow("000000", "555555"),

                # left_arrow("000000", "555555"),
                # widget.Bluetooth(),
                widget.Systray(
                    padding=8,
                ),

                widget.HDDBusyGraph(
                    background="555555",
                    graph_color="#000000",
                    fill_color="#555555",  # Optional: for the area under the line
                    border_color="#000000",  # Optional: border of the widget
                ),

                widget.QuickExit(background="555555"),
            ],
            24,
            border_width=[2, 2, 2, 2],  # Draw top and bottom borders
            border_color=[
                "696969",
                "696969",
                "696969",
                "696969",
            ],  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

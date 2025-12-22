# ============================================================================
# FILE: ~/.config/qtile/settings/widgets.py
# ============================================================================

from libqtile import widget
from custom_volume import pipewire_volume_widget
from unicode_chars import left_arrow, right_arrow
from settings.theme import colors

def create_widgets():
    """Create and return the list of widgets for the bar"""
    return [
        pipewire_volume_widget,
        right_arrow("555555", "000000"),
        
        widget.CPU(
            background="555555",
            format="     {freq_current}GHz CPU Load:{load_percent}%",
        ),
        right_arrow("000000", "555555"),
        
        widget.CPUGraph(
            graph_color="#555555",
            fill_color="#555555",
            border_color="#555555",
        ),
        right_arrow("555555", "000000"),
        
        widget.CheckUpdates(background="555555"),
        right_arrow("000000", "555555"),
        
        widget.GroupBox(
            highlight_method="block",
            this_current_screen_border="#555555"
        ),
        
        widget.TextBox(
            text="  SoloLinux",
            fontsize=14,
            foreground=colors["accent1"],
            padding=10,
        ),
        right_arrow("555555", "000000"),
        
        widget.CapsNumLockIndicator(),
        
        widget.WindowName(
            background="555555",
            format="{name}",
            max_chars=50,
            width=300,
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
        
        widget.Prompt(foreground="0000ff"),
        
        left_arrow("555555", "000000"),
        
        widget.Backlight(
            backlight_name="amdgpu_bl1",
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
        
        widget.Systray(padding=8),
        
        widget.HDDBusyGraph(
            background="555555",
            graph_color="#000000",
            fill_color="#555555",
            border_color="#000000",
        ),
        
        widget.QuickExit(background="555555"),
    ]




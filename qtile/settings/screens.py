# ============================================================================
# FILE: ~/.config/qtile/settings/screens.py
# ============================================================================

from libqtile import bar
from libqtile.config import Screen
from settings.widgets import create_widgets
from settings.theme import widget_defaults as theme_widget_defaults

widget_defaults = theme_widget_defaults.copy()
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            create_widgets(),
            24,
            border_width=[2, 2, 2, 2],
            border_color=["696969", "696969", "696969", "696969"],
        ),
    ),
]


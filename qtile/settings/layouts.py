from libqtile import layout
from libqtile.config import Match
from settings.theme import layout_theme

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
]

# Floating layout configuration
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_focus=layout_theme["border_focus"],
    border_normal=layout_theme["border_normal"],
    border_width=layout_theme["border_width"],
)




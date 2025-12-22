from libqtile.config import Group, Key
from libqtile.lazy import lazy

mod = "mod4"

# Create 9 workspaces
groups = [Group(i) for i in "123456789"]

# Generate keybindings for groups
def init_group_keys():
    group_keys = []
    for i in groups:
        group_keys.extend([
            # mod + number = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}"),
            # mod + shift + number = move window to group
            Key([mod, "shift"], i.name, 
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}"),
        ])
    return group_keys

import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    """Run autostart applications once when Qtile starts"""
    home = os.path.expanduser("~")
    
    # List of commands to run at startup
    # Format: [command, args...]
    startup_apps = [
        # Color temperature adjustment (choose one)
        ["redshift", "-O", "4000"],
        # ["gammastep", "-O", "2200"],
        
        # Set wallpaper
        ["feh", "--bg-scale", f"{home}/Pictures/wallpapers/arch_syle.jpeg"],
        
        # Enable touchpad tap-to-click (device ID: 13)
        # ["xinput", "set-prop", "13", "libinput Tapping Enabled", "1"],
        
        # Additional common autostart applications (uncomment as needed):
        # ["picom"],  # Compositor for transparency/effects
        # ["nm-applet"],  # Network manager applet
        # ["blueman-applet"],  # Bluetooth manager
        # ["dunst"],  # Notification daemon
        # ["flameshot"],  # Screenshot tool
        # ["clipmenud"],  # Clipboard manager
        # ["unclutter"],  # Hide mouse cursor when idle
        # ["numlockx", "on"],  # Enable numlock
    ]
    
    # Launch each application
    for app in startup_apps:
        try:
            subprocess.Popen(app)
        except FileNotFoundError:
            print(f"Warning: {app[0]} not found, skipping...")
        except Exception as e:
            print(f"Error launching {app[0]}: {e}")


@hook.subscribe.startup
def startup_every_time():
    """Run commands every time Qtile restarts (including after config reload)"""
    # Add commands here that should run on every restart
    # Example: Reset cursor theme
    # subprocess.run(["xsetroot", "-cursor_name", "left_ptr"])
    pass

# import os
# import subprocess
# from libqtile import hook
#
# @hook.subscribe.startup_once
# def autostart():
#     home = os.path.expanduser("~")
#     # subprocess.Popen(["gammastep", "-O", "2200"])
#     subprocess.Popen(["redshift", "-O", "4000"])
#     subprocess.Popen(["feh", "--bg-scale", f"{home}/Pictures/wallpapers/arch_syle.jpeg"])
#     subprocess.Popen(["xinput", "set-prop", "13", "libinput Tapping Enabled", "1"])

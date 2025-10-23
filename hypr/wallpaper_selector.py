#!/usr/bin/env python3
from gi import require_version
require_version("Gtk", "4.0")

import os
import subprocess
from gi.repository import Gtk, GdkPixbuf, Gio

WALLPAPER_DIR = os.path.expanduser("~/.config/hypr/wallpapers")

class WallpaperChooser(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.sololinux.wallpaperchooser")
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = Gtk.ApplicationWindow(application=self)
            self.window.set_title("Select Wallpaper")
            self.window.set_default_size(1000, 700)

            outer_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
            self.window.set_child(outer_box)

            # Ensure swww daemon is running
            subprocess.Popen(["swww-daemon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            scrolled = Gtk.ScrolledWindow()
            outer_box.append(scrolled)

            flowbox = Gtk.FlowBox()
            flowbox.set_valign(Gtk.Align.START)
            flowbox.set_max_children_per_line(5)
            flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
            flowbox.set_row_spacing(10)
            flowbox.set_column_spacing(10)
            scrolled.set_child(flowbox)

            if os.path.isdir(WALLPAPER_DIR):
                for file in sorted(os.listdir(WALLPAPER_DIR)):
                    if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                        path = os.path.join(WALLPAPER_DIR, file)
                        flowbox.insert(self.create_thumbnail(path), -1)
            else:
                flowbox.insert(Gtk.Label(label="No wallpapers found."), -1)

        self.window.present()

    def create_thumbnail(self, filepath):
        """Create a clickable thumbnail for a wallpaper."""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        box.set_margin_top(5)
        box.set_margin_bottom(5)
        box.set_margin_start(5)
        box.set_margin_end(5)

        picture = Gtk.Picture()
        try:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filepath, 200, 200, preserve_aspect_ratio=True)
            picture.set_pixbuf(pixbuf)
        except Exception as e:
            print(f"Failed to load {filepath}: {e}")
            return Gtk.Label(label="Error loading image")

        label = Gtk.Label(label=os.path.basename(filepath))
        label.set_wrap(True)
        label.set_justify(Gtk.Justification.CENTER)

        button = Gtk.Button()
        button.set_child(picture)
        button.connect("clicked", self.on_wallpaper_click, filepath)

        box.append(button)
        box.append(label)

        frame = Gtk.Frame()
        frame.set_child(box)
        return frame

    def on_wallpaper_click(self, button, filepath):
        """Set wallpaper using swww."""
        subprocess.Popen([
            "swww", "img", filepath,
            "--transition-type", "any",
            "--transition-step", "90"
        ])
        print(f"Wallpaper set: {filepath}")

def main():
    app = WallpaperChooser()
    app.run(None)

if __name__ == "__main__":
    main()


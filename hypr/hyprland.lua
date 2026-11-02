-- SoloLinux configuration migrated for Hyprland 0.57.
-- The old hypr_modules/*.conf files are retained as reference only.
hl.env("XCURSOR_SIZE", "24")
hl.env("HYPRCURSOR_SIZE", "24")
hl.monitor({ output = "", mode = "preferred", position = "auto", scale = "auto" })
hl.monitor({ output = "eDP-1", mode = "1920x1080@60.02000", position = "0x0", scale = 1 })
hl.config({
    general = {
        gaps_in = 5, gaps_out = 20, border_size = 3,
        col = { active_border = "rgba(256897ff)", inactive_border = "rgba(595959aa)" },
        resize_on_border = false, allow_tearing = false, layout = "dwindle",
    },
    decoration = { rounding = 0, active_opacity = 1.0, inactive_opacity = 0.8 },
    animations = { enabled = true },
    dwindle = { preserve_split = true },
    master = { new_status = "master" },
    misc = { force_default_wallpaper = 0, disable_hyprland_logo = true, font_family = "Sans Serif" },
    input = {
        kb_layout = "gb", kb_variant = "", kb_model = "", kb_options = "", kb_rules = "",
        follow_mouse = 1, mouse_refocus = false, sensitivity = 0,
        touchpad = { natural_scroll = false },
    },
})
-- Only enable the shader if its package is installed.
local shader = "/usr/share/hyprshade/shaders/blue-light-filter.glsl"
local f = io.open(shader, "r")
if f then
    f:close()
    hl.config({ decoration = { screen_shader = shader } })
end
hl.device({ name = "epic-mouse-v1", sensitivity = -0.5 })
hl.curve("easeOutQuint",   { type = "bezier", points = { {0.23, 1},    {0.32, 1}    } })
hl.curve("easeInOutCubic", { type = "bezier", points = { {0.65, 0.05}, {0.36, 1}    } })
hl.curve("linear",         { type = "bezier", points = { {0, 0},       {1, 1}       } })
hl.curve("almostLinear",   { type = "bezier", points = { {0.5, 0.5},   {0.75, 1}    } })
hl.curve("quick",          { type = "bezier", points = { {0.15, 0},    {0.1, 1}     } })
hl.animation({ leaf = "global", enabled = true, speed = 10, bezier = "default" })
hl.animation({ leaf = "border", enabled = true, speed = 5.39, bezier = "easeOutQuint" })
hl.animation({ leaf = "windows", enabled = true, speed = 4.79, bezier = "easeOutQuint" })
hl.window_rule({ name = "tile-kitty", match = { class = "^(kitty)$" }, float = false })
hl.window_rule({ name = "suppress-maximize-events", match = { class = ".*" }, suppress_event = "maximize" })
-- Startup runs once per compositor session. The wallpaper script starts hyprpaper itself.
hl.on("hyprland.start", function()
    hl.exec_cmd("waybar")
    hl.exec_cmd("nm-applet --indicator")
    hl.exec_cmd("command -v hyprshade >/dev/null 2>&1 && hyprshade on blue-light-filter")
    hl.exec_cmd("bash ~/.config/hypr/scripts/random_wallpaper.sh")
end)

-- Personal keybindings
hl.bind("SUPER + T", hl.dsp.exec_cmd("~/.config/waybar/switch_theme.sh"))
hl.bind("SUPER + c", hl.dsp.exec_cmd("bash ~/.config/hypr/scripts/change_wallpaper.sh"))
hl.bind("SUPER + w", hl.dsp.exec_cmd("waypaper"))
hl.bind("ALT + TAB", hl.dsp.window.cycle_next())
hl.bind("SUPER + s", hl.dsp.exec_cmd("kitty"))
hl.bind("SUPER + q", hl.dsp.window.close())
hl.bind("SUPER + m", hl.dsp.exit())
hl.bind("SUPER + e", hl.dsp.exec_cmd("emacs --init-directory ~/.config/emacs"))
hl.bind("SUPER + b", hl.dsp.exec_cmd("brave"))
hl.bind("SUPER + SHIFT + b", hl.dsp.exec_cmd("blender"))
hl.bind("SUPER + v", hl.dsp.exec_cmd("code"))
hl.bind("SUPER + f", hl.dsp.exec_cmd("nautilus"))
hl.bind("SUPER + k", hl.dsp.exec_cmd("kicad"))
hl.bind("SUPER + d", hl.dsp.exec_cmd("~/Downloads/Digital/Digital.sh"))
hl.bind("SUPER + r", hl.dsp.exec_cmd("~/.config/rofi/launchers/type-2/launcher.sh"))
hl.bind("Print", hl.dsp.exec_cmd("hyprshot -m output"))
hl.bind("SHIFT + Print", hl.dsp.exec_cmd("hyprshot -m region"))
hl.bind("SUPER + Print", hl.dsp.exec_cmd("hyprshot -m window"))
hl.bind("SUPER + p", hl.dsp.window.pseudo())
hl.bind("SUPER + left", hl.dsp.focus({ direction = "left" }))
hl.bind("SUPER + right", hl.dsp.focus({ direction = "right" }))
hl.bind("SUPER + up", hl.dsp.focus({ direction = "up" }))
hl.bind("SUPER + down", hl.dsp.focus({ direction = "down" }))
hl.bind("SUPER + 1", hl.dsp.focus({ workspace = 1 }))
hl.bind("SUPER + 2", hl.dsp.focus({ workspace = 2 }))
hl.bind("SUPER + 3", hl.dsp.focus({ workspace = 3 }))
hl.bind("SUPER + 4", hl.dsp.focus({ workspace = 4 }))
hl.bind("SUPER + 5", hl.dsp.focus({ workspace = 5 }))
hl.bind("SUPER + 6", hl.dsp.focus({ workspace = 6 }))
hl.bind("SUPER + 7", hl.dsp.focus({ workspace = 7 }))
hl.bind("SUPER + 8", hl.dsp.focus({ workspace = 8 }))
hl.bind("SUPER + 9", hl.dsp.focus({ workspace = 9 }))
hl.bind("SUPER + 0", hl.dsp.focus({ workspace = 10 }))
hl.bind("SUPER + SHIFT + 1", hl.dsp.window.move({ workspace = 1 }))
hl.bind("SUPER + SHIFT + 2", hl.dsp.window.move({ workspace = 2 }))
hl.bind("SUPER + SHIFT + 3", hl.dsp.window.move({ workspace = 3 }))
hl.bind("SUPER + SHIFT + 4", hl.dsp.window.move({ workspace = 4 }))
hl.bind("SUPER + SHIFT + 5", hl.dsp.window.move({ workspace = 5 }))
hl.bind("SUPER + SHIFT + 6", hl.dsp.window.move({ workspace = 6 }))
hl.bind("SUPER + SHIFT + 7", hl.dsp.window.move({ workspace = 7 }))
hl.bind("SUPER + SHIFT + 8", hl.dsp.window.move({ workspace = 8 }))
hl.bind("SUPER + SHIFT + 9", hl.dsp.window.move({ workspace = 9 }))
hl.bind("SUPER + SHIFT + 0", hl.dsp.window.move({ workspace = 10 }))
hl.bind("SUPER + SHIFT + space", hl.dsp.workspace.toggle_special("magic"))
hl.bind("SUPER + SHIFT + s", hl.dsp.window.move({ workspace = "special:magic" }))
hl.bind("SUPER + mouse_down", hl.dsp.focus({ workspace = "e+1" }))
hl.bind("SUPER + mouse_up", hl.dsp.focus({ workspace = "e-1" }))
hl.bind("SUPER + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind("SUPER + mouse:273", hl.dsp.window.resize(), { mouse = true })
hl.bind("xf86audioraisevolume", hl.dsp.exec_cmd("bash ~/.config/hypr/scripts/volume_control.sh up"), { locked = true, repeating = true })
hl.bind("xf86audiolowervolume", hl.dsp.exec_cmd("bash ~/.config/hypr/scripts/volume_control.sh down"), { locked = true, repeating = true })
hl.bind("xf86audiomute", hl.dsp.exec_cmd("bash ~/.config/hypr/scripts/volume_control.sh mute"), { locked = true, repeating = true })
hl.bind("xf86audiomicmute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"), { locked = true, repeating = true })
hl.bind("xf86monbrightnessup", hl.dsp.exec_cmd("brightnessctl s 1%+"), { locked = true, repeating = true })
hl.bind("xf86monbrightnessdown", hl.dsp.exec_cmd("brightnessctl s 1%-"), { locked = true, repeating = true })
hl.bind("xf86audionext", hl.dsp.exec_cmd("playerctl next"), { locked = true })
hl.bind("xf86audiopause", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("xf86audioplay", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("xf86audioprev", hl.dsp.exec_cmd("playerctl previous"), { locked = true })

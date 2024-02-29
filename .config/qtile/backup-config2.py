#   
#       █████████     ███████    ███████████ █████ █████ ███████████ █████ █████       ██████████
#      ███░░░░░███  ███░░░░░███ ░█░░░░░░███ ░░███ ░░███ ░█░░░███░░░█░░███ ░░███       ░░███░░░░░█
#     ███     ░░░  ███     ░░███░     ███░   ░░███ ███  ░   ░███  ░  ░███  ░███        ░███  █ ░ 
#    ░███         ░███      ░███     ███      ░░█████       ░███     ░███  ░███        ░██████   
#    ░███         ░███      ░███    ███        ░░███        ░███     ░███  ░███        ░███░░█   
#    ░░███     ███░░███     ███   ████     █    ░███        ░███     ░███  ░███      █ ░███ ░   █
#     ░░█████████  ░░░███████░   ███████████    █████       █████    █████ ███████████ ██████████
#      ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░    ░░░░░       ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░ 
#

  
from libqtile import bar, layout, hook, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
import colors

mod = "mod4"
ctrl = "control"
terminal = "alacritty"
colors, backgroundColor, foregroundColor, workspaceColor, chordColor = colors.nord()


# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Launch rofi
    Key([mod], "r", lazy.spawn(".config/rofi/scripts/launcher_t1")),

    # Launch powermenu
    Key([mod], "p", lazy.spawn(".config/rofi/scripts/powermenu_t4")),
    # Key([mod], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='theme_switcher'),


    Key([], "XF86AudioRaiseVolume", lazy.spawn("/home/sahil/.local/bin/changevolume up"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("/home/sahil/.local/bin/changevolume down"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("/home/sahil/.local/bin/changevolume mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([mod],"e", lazy.spawn("thunar"), desc='file manager'),
	# Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),

    Key([mod], "v", lazy.spawn("code"), desc="Open VS Code"),
    Key([mod], "w", lazy.spawn(f"{terminal} -e sh -c 'nvim ~/.config/qtile/config.py'")),
    Key([mod], "b", lazy.spawn("brave"), desc="Open Browser"),
    Key([ctrl], "space", lazy.spawn("dunstctl close"), desc="Close notifications"),
            
    # Scratchpads
    Key([mod, ctrl], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod, ctrl], "2", lazy.group['scratchpad'].dropdown_toggle('kdeconnect')),
]


########## Pywal Colors #########

py_colors = []
colors_file='/home/sahil/.cache/wal/colors'
with open(colors_file, 'r') as file:
    for i in range(10):
        py_colors.append(file.readline().strip())
lazy.reload()


# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["󰖟", "", "󰨞", "", "󰈙", "ﭮ", "", "󰝚", "", "󰯈"]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )

groups.append(ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "alacritty", opacity=0.8, height=0.5),

        # define another terminal exclusively for qshell at different position
        DropDown("kdeconnect", "kdeconnect-settings", 
            x=0.2, y=0.36, width=0.6, height=0.6, opacity=0.8,
            on_focus_lost_hide=True) 
    ]),
)

######### LAYOUTS #########
layout_theme = {
        "margin":5,
        "border_width": 4,
        "border_focus": colors[2],
        "border_normal": backgroundColor
    }

layouts = [
    layout.Columns(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize = 15,
    padding = 2,
    background = backgroundColor
)
extension_defaults = widget_defaults.copy()

# def search():
#     qtile.cmd_spawn("rofi -show drun")

# def power():
#     qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄

screens = [
    Screen ( 
        top = bar.Bar(
            [   
                widget.GroupBox(
                    font="JetBrainsMono Nerd Font",
                    fontsize = 18,
                    margin_y = 2,
                    margin_x = 4,
                    padding_y = 6,
                    padding_x = 6,
                    borderwidth = 2,
                    disable_drag = True,
                    active = colors[4], #fg
                    inactive = foregroundColor,
                    hide_unused = True,
                    rounded = False,
                    highlight_method = "line",
                    highlight_color = [backgroundColor, backgroundColor],
                    this_current_screen_border = colors[5],
                    this_screen_border = colors[7],
                    other_screen_border = colors[6],
                    other_current_screen_border = colors[6],
                    urgent_alert_method = "line",
                    urgent_border = colors[9],
                    urgent_text = colors[1],
                    foreground = foregroundColor,
                    background = backgroundColor,
                    use_mouse_wheel = False
                ),
                widget.Sep(linewidth = 1, padding = 10, foreground = colors[5],background = backgroundColor),
                widget.TaskList(
                    icon_size = 17,
                    font = "JetBrainsMono Nerd Font",
                    foreground = colors[0],
                    background = colors[2],
                    borderwidth = 0,
                    border = py_colors[2],
                    margin = 0,
                    padding = 5,
                    highlight_method = "block",
                    title_width_method = "uniform",
                    urgent_alert_method = "border",
                    urgent_border = colors[1],
                    rounded = False,
                    txt_floating = "🗗 ",
                    txt_maximized = "🗖 ",
                    txt_minimized = "🗕 ",
                    window_name_location_offset = 100
                ),
                widget.Sep(linewidth = 1, padding = 10, foreground = colors[0],background = colors[0]),
                widget.TextBox(text = " ", fontsize = 14, font = "JetBrainsMono Nerd Font", foreground = colors[6]),
                widget.CPU(
                    font = "JetBrainsMono Nerd Font",
                    update_interval = 1.0,
                    format = '{load_percent}%',
                    foreground = foregroundColor,
                ),
                widget.Sep(linewidth = 0, padding = 15),
                widget.TextBox(text = "", fontsize = 14, font = "JetBrainsMono Nerd Font", foreground = colors[3]),
                widget.Memory(
                    font = "JetBrainsMonoNerdFont",
                    foreground = foregroundColor,
                    format = '{MemUsed: .1f}{mm} /{MemTotal: .0f}{mm}',
                    measure_mem='G',
                ),
                widget.Sep(linewidth = 0, padding = 15),
                widget.TextBox(text = " ", fontsize = 14, font = "JetBrainsMono Nerd Font", foreground = colors[8]),
                widget.Clock(
                    padding=5,
                    format="%A %b %-d", 
                    foreground = foregroundColor,
                ),
                widget.Sep(linewidth = 0, padding = 10),
                widget.TextBox(text = " ", fontsize = 14, font = "JetBrainsMono Nerd Font", foreground = colors[10]),
                widget.Clock(format='%I:%M %p', font = "JetBrainsMono Nerd Font", padding = 5, foreground = foregroundColor),
                widget.Sep(linewidth = 0, padding = 10),
                 
                widget.BatteryIcon(
                    theme_path='~/.config/qtile/Assets/Battery/',
                    scale=1,
                ),
                widget.Sep(linewidth = 0, padding = 4),
                widget.Battery(
                    font="JetBrainsMonoNerdFont",
                    foreground=foregroundColor,
                    format='{percent:2.0%}',
                ),               
                widget.Sep(linewidth = 0, padding = 10),

                widget.Systray(background = backgroundColor, icon_size = 20, padding = 4),
                widget.Sep(linewidth = 1, padding = 10, foreground = colors[5], background = backgroundColor),
                widget.CurrentLayoutIcon(scale = 0.6, foreground = colors[6], background = colors[6], padding=5),
           ],
            size = 29,
            margin = 6,
            background = backgroundColor,
            opacity=0.8,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  
follow_mouse_focus = True
bring_front_click = False
float_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], fullscreen_border_width = 0, border_width = 0)


import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser('~/.config/qtile/autostart_once.sh')])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"



# E O F

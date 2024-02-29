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
#                                                                                   
  


from libqtile import bar, layout, hook, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from themes.obsidian import *

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

mod = "mod4"
ctrl = "control"
terminal = "alacritty"


########## Pywal Colors #########

colors = []
cache='/home/sahil/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)


########## Powerline from extras ########

arrow_powerlineRight = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_right",
            size=11,
        )
    ]
}
arrow_powerlineLeft = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_left",
            size=11,
        )
    ]
}
rounded_powerlineRight = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_right",
            size=11,
        )
    ]
}
rounded_powerlineLeft = {
    "decorations": [
        PowerLineDecoration(
            path="rouded_left",
            size=11,
        )
    ]
}
slash_powerlineRight = {
    "decorations": [
        PowerLineDecoration(
            path="forward_slash",
            size=11,
        )
    ]
}
slash_powerlineLeft = {
    "decorations": [
        PowerLineDecoration(
            path="back_slash",
            size=11,
        )
    ]
}


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
    Key([ctrl], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([ctrl], "2", lazy.group['scratchpad'].dropdown_toggle('kdeconnect')),
]



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

groups = [Group(f"{i+1}", label=f"{i+1}") for i in range(9)]

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
        DropDown("term", "alacritty", opacity=0.8),

        # define another terminal exclusively for qshell at different position
        DropDown("kdeconnect", "kdeconnect-settings", 
            x=0.2, y=0.36, width=0.6, height=0.6, opacity=0.8,
            on_focus_lost_hide=True) 
    ]),
)

# L A Y O U T S

layouts = [
    layout.Columns(border_width=4, margin=5, border_focus=colors[4], border_normal=unfocused, border_on_single=True), 
    layout.Bsp(border_focus=colors[4], border_normal=unfocused, border_width=4, margin=4, border_on_single=True)
]

widget_defaults = dict(
    font = "FiraCode Nerd Font",
    fontsize = 14,
    padding = 3,
    foreground ="#C5CAD3", # foreground
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
                widget.Image(
                    filename="~/.config/qtile/Assets/arch.png",
                    # mouse_callbacks={"Button1": open_rofi},
                    background=colors[2],
                    margin=4,
                ),
                widget.Spacer(
                    length=1,
                    background=colors[2],
                    **arrow_powerlineLeft,
                ),
                widget.GroupBox(
                    borderwidth = 5,
                    active = "fff",
                    inactive = inactive,
                    highlight_method = "line",
                    highlight_color = colors[1],                      
                    this_current_screen_border = colors[2],
                    disable_drag = True,
                    hide_unused=False,
                    margin_x=0,
                    padding=4,
                ),

                # Task List
                widget.TaskList(
                    icon_size = 0,
                    border = colors[1],
                    unfocused_border = colors[2],
                    background = colors[1],
                    margin = 0,
                    padding = 4,
                    highlight_method="block",
                    title_width_method = "uniform",
                    txt_floating = "🗗 ",
                    txt_maximized = "🗖 ",
                    txt_minimized = "🗕 ",
                    rounded = False
                ),
                widget.Spacer(length=5),
                
                widget.CPU(
                    padding=5,
                    format=" {freq_current}GHz {load_percent}%",
                    background=background,
                ),

                widget.Spacer(length=5),
                
                widget.Memory(
                    padding=5,
                    format="󰈀 {MemUsed:.0f}{mm}",
                    background=colors[2],
                ),
                
                widget.Spacer(length=5),

                widget.Pomodoro(
                    notification_on=True,
                    markup=True,
                    font='Fira Code',
                ),
                
                widget.Spacer(length=5),

                # Date
                widget.Clock(
                    padding=5,
                    format=" %A %b %-d", 
                    background=background,
                ),

                widget.Spacer(length=5),
                
                # Time
                widget.Clock(
                    padding=5,
                    markup=True, 
                    format="<span foreground='#FFFFFF'> </span>%I:%M %p",
                    background=colors[2],
                ),
                
                widget.Spacer(length=5),

                # #Audio
                # widget.PulseVolume(
                #     fmt="󰕾 {}",
                #     padding=10,
                #     **slash_powerlineRight,
                # ),
                # widget.Sep(linewidth = 0, padding = 10),
                
                # Battery
                widget.Battery(show_short_text=False, foreground="#FFFFFF", format="{char}", full_char=" ", charge_char=" ", discharge_char = ' ', update_interval=5),
                widget.Battery(show_short_text=False, format="{percent:2.0%}", notify_below = 30, notification_timeout = 0, update_interval=5),
                widget.Battery(show_short_text=False, format="{char}", full_char="", charge_char="󰁞", discharge_char = '󰁆', update_interval=5),

                widget.Spacer(length=5),

                widget.Systray(
                    padding=5,
                    icon_size=21,
                ),

                widget.Spacer(length=5),
                
                # Layout icon
                widget.CurrentLayoutIcon(padding=7, scale = 0.6, background=colors[1]),
            ],
            size = 27,
            margin = [8, 8, 4, 8],
            background = background,
            opacity=0.8,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floats_kept_above = True
floating_layout = layout.Floating(
    border_width = 2,
    border_focus = colors[4],
    border_normal = background,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="confirm"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pavucontrol"),
        Match(wm_class="dialog"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="download"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)



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

#!/bin/bash

# Apply wallpaper using wal
wal -i wallpaper.jpg

setxkbmap -option caps:swapescape

# Start picom
# picom --config ~/.config/picom/picom.conf &
# picom --experimental-backends -b 
picom -bc &

# eval $(gnome-keyring-daemon --start)
# export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK
dbus-update-activation-environment --all
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
gnome-keyring-daemon --start --components=secrets

xset b off
thunar --daemon &
nm-applet &

#!/bin/sh

echo "Starting Base Arch packages installer, installing Paru..."
sudo pacman -Syu
sudo pacman -S --needed base-devel
mkdir ~/Programs/
cd ~/Programs/
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si 
paru -Syu

echo "Installing essential packages..."
paru -S neovim picom brave-bin acpi_call flameshot thunar thunar-volman thunar-archive-plugin thunar-media-tags-plugin gnome-keyring neofetch nitrogen code tumbler xclip rofi rofi-emoji xdg-user-dirs code code-marketplace feh zsh starship 
xdg-user-dirs-update

echo "Essential packages installed, now some extra packages..."
paru -S npm tldr timeshift telegram-desktop discord libreoffice-fresh exa mpv kdeconnect nwg-look gvfs ocs-url timeshift noto-fonts ttf-fira-code ttf-firacode-nerd ttf-jetbrains-mono-nerd ttf-ms-fonts ttf-roboto tmux snapshot filelight btop pavucontrol obsidian

echo "Installing NvChad, Run :MasonInstallAll command after lazy.nvim finishes downloading plugins..."
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim

echo "Setting up zsh..."
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
chsh -s /bin/zsh

echo "Copying configs..."
cd ~/Programs/
git clone https://github.com/sahilsh-dev/dots-arch.git
cd dots-arch/
cp -r config/alacritty ~/.config/
cp -r config/awesome ~/.config/
cp -r config/picom ~/.config/
cp -r local/bin ~/.local/ 


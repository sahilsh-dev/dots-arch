# File Explorer Script

selected_directory=$(find ~/.config ~/Documents/VS_Code_Files ~/Programs -mindepth 1 -maxdepth 2 -type d | fzf)

# Check if a directory was selected
if [ -n "$selected_directory" ]; then
    # Change to the selected directory
    cd "$selected_directory"
fi

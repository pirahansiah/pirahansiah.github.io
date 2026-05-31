computer vision in IoT
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool TRUE
dot_clean -m /Volumes/4tb
sudo mdutil -i off /Volumes/4tb
touch /Volumes/4tb/.metadata_never_index

cd /Volumes/4tb/2026-6/pirahansiah.github.io
git submodule update --remote --merge

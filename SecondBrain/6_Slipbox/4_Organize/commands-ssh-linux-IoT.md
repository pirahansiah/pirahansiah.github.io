# temux

install 
    - brew install tmux   
    - tmux new-session -f1
    - tmux ls
    - tmux attach -t 0   
    - - ctrl+b 
      - < , > , ^ , 
      - Ctrl+b [
      - 
nano ~/.tmux.conf
set -g mouse on
tmux source-file ~/.tmux.conf






# Commands
Ctrl + b + % to split the current pane vertically.
Ctrl + b + " to split the current pane horizontally.
Ctrl + b + x to close the current pane.

tmux attach -t 0



Enable Remote Login via System Settings:
    Open System Settings again.
    Go to General > Sharing.
    Check the box next to Remote Login.

sudo systemsetup -setremotelogin on
sudo systemsetup -getremotelogin

ifconfig | grep inet



md5sum

Check system uptime
uptime

Check disk space usage
df -h

Monitor system processes and resource usage
htop

Check listening ports and services
ss -ntlp

Check memory usage
free -h

View system logs (e.g., the latest system log)
tail -f /var/log/syslog

Check CPU usage
top

List all active network connections
netstat -tuln

Check currently logged-in users
who

Display the kernel version
uname -r

Show detailed information about the system
lsb_release -a

View information about PCI devices
lspci

Show information about USB devices
lsusb

Check available updates (for Debian-based systems)
sudo apt update

Upgrade installed packages (for Debian-based systems)
sudo apt upgrade

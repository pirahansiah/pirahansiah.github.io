# Persisting tmux Sessions Across Restarts and Using VS Code SSH

I use `tmux` and have set up the plugin `tmux-resurrect` to persist tmux sessions across restarts. This tool saves and restores tmux sessions, making it easy to maintain my work environment. I have several sessions running on different devices: one on my Mac, one on Windows, and one on a Jetson Nano. I connect to each device using VS Code SSH with X forwarding and `tmux`, which allows me to start my work quickly. If I disconnect or face any interruptions, I can simply go back and continue where I left off, with my processes still running without any issues.

## Setting Up `tmux-resurrect` to Persist Sessions

1. **Install `tmux` and `tmux-resurrect`**:
   - Follow the instructions from the [tmux-resurrect GitHub repository](https://github.com/tmux-plugins/tmux-resurrect) to install `tmux-resurrect`.

2. **Configure `tmux-resurrect`**:
   - Add the following lines to your `.tmux.conf` file:
     ```sh
     set -g @plugin 'tmux-plugins/tmux-resurrect'
     run-shell ~/.tmux/plugins/tmux-resurrect/resurrect.tmux
     ```
   - Ensure that you source the `.tmux.conf` file to apply the changes:
     ```sh
     tmux source-file ~/.tmux.conf
     ```

3. **Save and Restore Sessions**:
   - To save your tmux session:
     ```sh
     prefix + Ctrl-s
     ```
   - To restore your tmux session:
     ```sh
     prefix + Ctrl-r
     ```

## Using `tmux` with VS Code SSH

1. **Open VS Code and Connect via SSH**:
   - Install the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension.
   - Use the Remote Explorer in VS Code to connect to your remote machine.

2. **Start a `tmux` Session in Your Remote Terminal**:
   - Open a terminal in VS Code and start a new tmux session:
     ```sh
     tmux new -s mysession
     ```

3. **Detach from `tmux` Session**:
   - Detach from the session to leave it running in the background:
     ```sh
     Ctrl-b d
     ```

4. **Reattach to `tmux` Session**:
   - Reattach to the session when you reconnect:
     ```sh
     tmux attach -t mysession
     ```

## Ensuring Programs Continue Running After Disconnect

1. **Use `tmux` to Run Long-Running Processes**:
   - Start your program inside a tmux session. For example:
     ```sh
     tmux new -s mysession
     ./my_long_running_program
     ```
   - Detach from the session:
     ```sh
     Ctrl-b d
     ```

2. **Reconnecting and Resuming Work**:
   - When you reconnect to the SSH session via VS Code, simply reattach to your tmux session:
     ```sh
     tmux attach -t mysession
     ```

By following these steps, you can ensure that your tmux sessions persist across disconnects and that any long-running processes continue to run even if you close VS Code. This setup allows you to seamlessly resume your work from where you left off.

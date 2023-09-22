# VS Code
* Download 
	* Insider
		* https://code.visualstudio.com/insiders/ 
	* Portable 
		* https://code.visualstudio.com/sha/download?build=insider&os=win32-x64-archive
* Extensions
	* Sourcery
	* Remote * SSH
	* Settings Sync
	* Live Server
	* Prettier
	* GitLens
	* TODO Highlights
	* VSCode-icons
	* Regex Previewer
	* Polacode
	* Better Comments
	* Indent-rainbow
	* Markdown All in One
	* Bookmarks
	* Open file
* Command line
	* code . 
		* open code with current directory
	* code -r . 
		* open the current directory in the most recently used code window
	* code -n 
		* create a new window
* Shortcut
	* PDF
		* https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf 
		* https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf
		* https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf 
	* Command Palette
		* open
			* Windows: CTRL+SHIFT+P
			* Mac: CMD+SHIFT+P
		* Quick Open
		    * Windows: CTRL+P
		    * Mac: CMD+P
	   * Multi-Select Cursor
		    * Windows: CTRL+D
		    * Mac: CMD+D
	   * Column (box) selection
		    * Windows: Shift+Alt 
		    * Mac: Shift+Option
	   * Comment Code Block
		    * Windows: SHIFT+ALT+A (Multi-line comment), CTRL+K+C (Single-line comment)
		    * Mac: SHIFT+OPT+A
	   * Global Find
		    * Windows: CTRL+SHIFT+F
		    * Mac: CMD+SHIFT+F
	   * Multiple Cursors
		    * Windows: CTRL+ALT+UP/Down arrow
		    * Mac: CMD+OPT+UP/Down arrow
	   * Side by side Markdown edit and preview
		    *  Windows: Ctrl+K V
  * IoT
	   * Install 1
			* git clone https://github.com/JetsonHacksNano/installVSCode.git
			* cd installVSCode
			* ./installVSCode.sh
			* ./installVSCodeWithPython.sh
			* code-oss
	   * install 2
			* curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-archive-keyring.gpg
			* echo "deb [arch=arm64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/code-insiders/ stable main" | sudo tee /etc/apt/sources.list.d/code-insiders.list
			* sudo apt update
			* sudo apt install code-insiders
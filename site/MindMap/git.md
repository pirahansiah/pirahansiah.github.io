# git

1. Setup and config 
	* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
	* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
	* git remote set-url origin git@github.com:username/repo.git
1. Configuration and Remote Operations:    
    - git remote -v: View remote repositories
    - git remote set-url origin [url]: Set the URL for the origin remote
    - git branch [branch_name]: Create a new branch
    - git branch -a: List all branches
2. Branch Operations:    
    - git checkout -b [branch_name]: Create and switch to a new branch
    - git branch -d [branch_name]: Delete a branch
    - git log --all: Show the commit history of all branches
    - git switch master: Switch to the master branch
3. Synchronization:    
    - git fetch: Fetch changes from the remote repository
    - git merge: Merge changes from a different branch
    - git pull: Fetch and merge changes from the remote repository
4. Commit Operations:    
    - git commit -a -m "message": Add and commit changes in one line
    - git rm --cached [file]: Remove a file from the staging area
    - git rm -r --cached [directory]: Remove a directory from the staging area
    - git add: Add changes to the staging area
5. Viewing and Logging:    
    - git log --pretty=oneline: Show the commit history in a pretty format
    - git log -3: Show the last 3 commits
    - git reflog: Show a reference log of all branch updates
    - git log -g: Show the reflog with abbreviated commit hashes
    - git log --since="1.hour": Show commits since the last hour
    - git log -oneline -3: Show the last 3 commits in a one-line format
6. Stashing:    
    - git stash -u/-a: Stash changes in the working directory (including untracked files/all changes)
    - git stash branch [new_branch]: Create a new branch from a stash
    - git stash: Stash changes in the working directory
    - git stash drop: Remove the most recent stash
    - git stash clear: Remove all stashes
    - git stash list: List all stashes
7. Miscellaneous:    
    - .gitignore: Specifies files and directories to be ignored by Git
    - git commit --amend: Amend the last commit
    - git push: Push changes to the remote repository
    - git cherry pick: Apply a specific commit from another branch
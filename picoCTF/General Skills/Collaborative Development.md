# Challenge Information

My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?  
You can download the challenge files here: **[challenge.zip](#)**  

### Hints:
- `git branch -a` will let you see available branches.  
- How can file 'diffs' be brought to the main branch?  
- Don't forget to `git config`!  
- Merge conflicts can be tricky! Try a text editor like **nano, emacs, or vim**.  

---

# Solution

Ok, so the first hint tells you to run a command—let's do that!  

```
┌──(kali㉿kali)-[~/picoCTF/drop-in]
└─$ git branch -a
  feature/part-1
  feature/part-2
  feature/part-3
  * main
```

Essentially this command tells git to list out all the branches that Git knows about
Googling what are git branches? led me to some interesting guides:

  "Git branches are effectively a pointer to a snapshot of your changes" https://www.atlassian.com/git/tutorials/usingbranches


  "In Git, a branch is a new/separate version of the main repository". - https://www.w3schools.com/git/git_branch.asp?remote=github

Using advice from the hint I git configed myself 
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

Now I can start merging. However, a problem arises

```
┌──(kali㉿kali)-[~/picoCTF/drop-in]
└─$ git merge feature/part-1
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
```

Now merging feature/part-1, I encountered a merge conflict! Git outputted an error,

Using advice from the third hint I can use a text editor, Nano in my case, to edit the file (flag.py)

![image](https://github.com/user-attachments/assets/90648cfe-f074-4a60-96d1-1ad7a3cc67bf)


Here you can notice the <<<<< Head, =======, and >>>>>>. Using a Google search I came across good advice regarding this


![image](https://github.com/user-attachments/assets/3d20c406-b8b3-4169-a8d7-abf3e1ed15c4)

These markers showed me the code from my main branch and the code from the feature/part-1 branch that was in conflict


To resolve the conflict, I realized the challenge likely intended for me to combine the flag parts from different branches 

Now merging part-3 I came across the same issue but using the documentation I researched prior I can resolve this easily!

![image](https://github.com/user-attachments/assets/109566cb-a030-4204-b825-ae603db2f4b8)


Now that all parts of the flag have been assembled I can use the command "python3" to run the .py file!

![image](https://github.com/user-attachments/assets/7f15e712-386a-46d0-a27a-b6a1f5485145)

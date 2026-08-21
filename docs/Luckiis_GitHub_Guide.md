# Luckii's GitHub Survival Guide

Welcome to the matrix! 

You are officially the **Art Director / Frontend Lead** for Geminisys. Your job is to take the ugly, bare-bones HTML files we created and use Gemini to make them look incredible. 

Because we are working on two different computers, we use **GitHub** as a giant "save folder in the cloud" to share our files. Here is the absolute easiest, jargon-free way to get the files, edit them, and send them back to us.

---

### Step 1: Get the "GitHub Desktop" App
Programmers usually use terrifying black-and-green text terminals to talk to GitHub. You don't have to. 
1. Download and install **[GitHub Desktop](https://desktop.github.com/)**.
2. Open it and sign in with your GitHub account.

### Step 2: Download the Game Files (Cloning)
We need to pull the files from the cloud onto your computer so you can edit them.
1. In GitHub Desktop, click **File > Clone Repository**.
2. Look for the `raworre/geminisys` repository in the list (or paste `https://github.com/raworre/geminisys` into the URL tab).
3. Choose a folder on your computer to save it to (like your Desktop or Documents) and click **Clone**.

*Boom. The files are now on your computer.*

---

### Step 3: Do the Art! (The Fun Part)
1. Open the `geminisys` folder on your computer.
2. Go into the `frontend` folder. You will see a file called `index.html`.
3. **To see what it looks like:** Double-click `index.html` and it will open in your web browser. (It looks terrible right now).
4. **To edit it:** Open `index.html` in any text editor (VS Code, Notepad, whatever you like). 
5. Copy all the text in that file, paste it into Gemini, and say: *"Make this look like a cyberpunk terminal!"*
6. When Gemini gives you the new code, paste it back into your text editor and click Save. 
7. Refresh your web browser to see your beautiful new UI!

---

### Step 4: Send the Art Back to Us (Commit & Push)
Once you have the UI looking exactly how you want it, you need to send it back to the cloud so the backend can attach to it.
1. Open **GitHub Desktop**.
2. You will see a list of all the files you changed on the left side.
3. At the bottom left, there is a box that says **Summary**. Type a quick message explaining what you did (e.g., *"Made the terminal neon green"*).
4. Click the blue **Commit to main** button. *(This "saves" your changes to the timeline).*
5. Finally, click the **Push origin** button at the top of the screen. *(This uploads your saved timeline to the cloud).*

That's it! You have successfully pushed code to a software repository. Let us know when the UI is pushed, and we'll wire up the Javascript!

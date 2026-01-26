# 🧙‍♂️ Command Wizard: The Ultimate Windows CLI Guide

Transform from a mouse-clicking apprentice into a keyboard-wielding master. This guide is designed for **students and developers** who want to command their machine with efficiency, precision, and speed.

---

## 🚀 The Wizard's "Big Five" (Quick Reference)
| Action | Command (CMD) | Command (PS) | Why it matters |
| :--- | :--- | :--- | :--- |
| **Move** | `cd <path>` | `cd <path>` | Teleport across your folders. |
| **List** | `dir` | `ls` or `gci` | See what's hidden in the current room. |
| **Clean** | `cls` | `clear` | Wipe the slate clean. |
| **Action** | `Tab` | `Tab` | The "Auto-Complete" magic wand. |
| **Stop** | `Ctrl + C` | `Ctrl + C` | The Emergency Exit for any command. |

---

## 📂 Navigation & Explorer Mastery
*Learn to traverse your computer's labyrinth without a map.*

### 📍 Track Your Location
* **Command Prompt:** `cd`
* **PowerShell:** `pwd` *(Print Working Directory)*

### 🚶 Move Around
* **Backwards:** `cd ..`
* **To Root (C:):** `cd \`
* **Teleport (Push/Pop):** Use `pushd C:\Temp` to save your spot and `popd` to return to it.

### 🔎 List What's There
* **Simple List:** `dir` (CMD) / `ls` (PS)
* **By Date:** `dir /OD` (CMD) / `ls | sort LastWriteTime` (PS)
* **Everything (Recurse):** `dir /S` (CMD) / `ls -Recurse` (PS)

> 💡 **Wizard Tip:** Type `explorer .` in any shell to instantly open your current folder in a Windows window.

---

## 🛠️ File & Folder Alchemy
*Create, destroy, and transform files with a few keystrokes.*

### ❇️ Creating
* **Empty File:** `type nul > file.txt` (CMD) / `ni file.txt` (PS)
* **New Folder:** `mkdir project_alpha` (Both)
* **Deep Folders:** `mkdir sub1\sub2\sub3` (Both)

### 📋 Copying & Moving
* **Copy:** `copy a.txt b.txt` (CMD) / `cp a.txt b.txt` (PS)
* **Move/Rename:** `move old.txt new.txt` (CMD) / `mv old.txt new.txt` (PS)

### 🗑️ The Void (Deleting)
* **Delete File:** `del file.txt` (CMD) / `rm file.txt` (PS)
* **Delete Folder:** `rd /s /q folder` (CMD) / `rm -r folder` (PS)
  *⚠️ Warning: These delete instantly without a recycle bin!*

---

## ⚙️ System & Life Support
*Monitor the health of your machine and control its soul (processes).*

### 🖥️ Vital Signs
* **System Specs:** `systeminfo`
* **OS Version:** `ver` (CMD) / `$PSVersionTable` (PS)
* **Processes:** `tasklist` (CMD) / `ps` (PS)

### ✂️ Terminating Runaways
* **Kill by Name:** `taskkill /IM node.exe /F` (CMD) / `kill -Name node` (PS)
* **Kill by ID:** `taskkill /PID 1234 /F` (CMD) / `kill 1234` (PS)

---

## 🌐 Networking & The Ethereal Plane
*Communicate with the world outside.*

* **Ping:** `ping google.com` (Check if a server is alive)
* **IP Details:** `ipconfig /all` (Your digital address)
* **Connections:** `netstat -ano` (See who's talking to your ports)
* **DNS:** `nslookup openai.com` (CMD) / `Resolve-DnsName openai.com` (PS)

---

## 🔑 Power User Techniques
*Advanced spells for the truly ambitious.*

### 📜 History & Echoes
*   **Previous Spells:** Press `Up Arrow` or `F7` (CMD) / `Ctrl + R` (Search PS History).
*   **Redirecting Power:**
    *   `dir > report.txt` (Overwrite file with output)
    *   `dir >> report.txt` (Append output to file)
*   **Chaining Spells:** `mkdir test && cd test` (Run second only if first succeeds).

### 🏷️ Aliases (Shortcuts)
In PowerShell, you can create your own shorthand:
```powershell
Set-Alias p Get-Process
Set-Alias ll Get-ChildItem
```
*(Add these to your `$PROFILE` to keep them forever.)*

---

## 🎓 The Apprentice's Training Grounds (Practice)

1.  **The "Ghost" Project:** Open a shell, create a folder named `Ghost`, enter it, create 5 empty `.txt` files, and then delete them all—all without touching the mouse.
2.  **The Process Hunter:** Find the PID (Process ID) of your browser and "gracefully" close it using the command line.
3.  **The Environmentalist:** Find out what your `PATH` variable is. Can you see where Python or Java is stored?

---

## 📜 Wizard's Scroll (Shortcuts)

| Key | Magic Effect |
| :--- | :--- |
| **Tab** | Autocomplete path/command |
| **Ctrl + C** | Stop a runaway command |
| **F7** | Show command history menu (CMD) |
| **Alt + Space + E + P** | CLI Properties (Change colors/fonts) |
| **Win + X** | Summon the Terminal Power Menu |

---

### 🌟 Final Words for the Journey
A true Wizard knows that the CLI isn't about memorizing every command—it's about knowing how to find them. Use `/?` (CMD) or `Get-Help` (PS) when you're stuck.

**Go forth and command your computer!** 🚀


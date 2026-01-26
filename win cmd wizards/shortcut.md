# 💻 Windows CMD Cheat Sheet

A quick reference guide for Command Prompt keyboard shortcuts, file management, networking, and system troubleshooting.

> **Note on Clearing the Screen:**
> While `cls` is the standard command to clear the screen, the shortcuts below help manage your current input line or active processes.

---

## ⌨️ Keyboard Shortcuts & Input Management

These shortcuts help you navigate the command line and manage running tasks efficiently.

| Shortcut              | Function                                                                          |
| :-------------------- | :-------------------------------------------------------------------------------- |
| **Esc**         | Clears the current input line.                                                    |
| **Ctrl + C**    | Stops the currently running process and moves the cursor to a new, blank line.    |
| **Ctrl + Home** | Clears all characters in the input**before** the cursor.                    |
| **Ctrl + End**  | Clears all characters in the input**after** the cursor.                     |
| **F7**          | Displays a list of previously executed commands to select from (Command History). |

---

## 📂 File and Directory Management

Essential commands for navigating folders and manipulating files.

* **`dir`**
  * Lists files and subdirectories in the current folder.
* **`cd [path]`**
  * Changes directory.
  * *Tip:* `cd ..` moves up one level; `cd \` goes to the root drive.
* **`mkdir [name]`** (or `md`)
  * Creates a new directory.
* **`rmdir [name]`** (or `rd`)
  * Removes an **empty** directory.
  * *Tip:* Use `rmdir /s` to remove a directory and its contents.
* **`copy [source] [dest]`**
  * Copies files from a source to a destination.
* **`move [source] [dest]`**
  * Moves or renames files.
* **`del [filename]`**
  * Deletes a specific file.
* **`type [filename]`**
  * Displays the contents of a text file directly in the terminal.

---

## 🌐 Networking Tools

Commands to diagnose connection issues and view network settings.

* **`ipconfig`**
  * Shows network configuration (IP address, Subnet Mask, Gateway).
  * *Useful Flags:* `ipconfig /flushdns` (clears DNS cache), `ipconfig /renew` (requests a new IP).
* **`ping [address]`**
  * Tests network connectivity to a specific IP or website (e.g., `ping google.com`).
* **`tracert [destination]`**
  * Traces the path of data packets to see where a connection might be failing.
* **`netstat`**
  * Displays active network connections and listening ports.

---

## ⚙️ System Management & Troubleshooting

Advanced commands for monitoring system health and processes.

| Command                       | Description                                                                                             |
| :---------------------------- | :------------------------------------------------------------------------------------------------------ |
| **`systeminfo`**      | Displays detailed system configuration (OS version, RAM, BIOS, etc.).                                   |
| **`tasklist`**        | Lists all currently running processes and their Services.                                               |
| **`taskkill`**        | Terminates a process.`<br>`Usage: `taskkill /PID [number]` or `/IM [imagename]`.                  |
| **`sfc /scannow`**    | **System File Checker:** Scans and repairs corrupted Windows system files.                        |
| **`chkdsk [drive:]`** | **Check Disk:** Checks the specified drive for errors and attempts repairs.                       |
| **`shutdown`**        | Manages power states.`<br>shutdown /r /t 0` (Restart immediately)`<br>shutdown /s` (Full shutdown). |

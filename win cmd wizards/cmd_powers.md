# Windows Command Line Power Moves

This is your quick-reference README for mastering the **Windows Command Prompt** and **PowerShell** with keyboard-first workflows. Build, browse, fix, and automate without touching the mouse, and keep these prompts handy for daily coding, data work, and system maintenance.

---

## Core Navigation & Filesystem Controls
| Task | Command Prompt | PowerShell | Notes |
| --- | --- | --- | --- |
| Show current folder | `cd` | `Get-Location` | Use `Tab` to autocomplete paths as you type. |
| Open a folder | `cd path\to\folder` | `Set-Location path\to\folder` | Use `Tab` to cycle through matches. |
| Create a file | `type nul > file.txt` | `New-Item file.txt -ItemType File` | `type nul` is fast for empty files. |
| Create a directory | `mkdir docs` | `New-Item docs -ItemType Directory` | Works even if folder already exists. |
| Remove a file | `del file.txt` | `Remove-Item file.txt` | Add `-Force` in PowerShell to skip prompts. |
| Remove a directory | `rmdir /s /q build` | `Remove-Item build -Recurse -Force` | PowerShell removes contents by default. |
| Copy files | `copy a.txt b.txt` | `Copy-Item a.txt b.txt` | Use wildcards like `*.log`. |
| Move/rename files | `move old.txt new.txt` | `Move-Item old.txt new.txt` | `Move-Item` renames across drives too. |
| List contents | `dir` | `Get-ChildItem` | `dir /OD` sorts by date; PowerShell objects stay rich. |

> **Keyboard tip:** Press `Alt + Space`, then `E` → `P` to edit properties, or use `Tab` + `Shift` + `Arrow` to select text. For longer paths, hold `Ctrl` and press `C`/`V` for copy/paste without the mouse.

---

## System & Process Control
- `cls` / `Clear-Host` — clear the buffer instantly.
- `tasklist` / `Get-Process` — list active processes; use `tasklist /FI "IMAGENAME eq node.exe"` or `Get-Process node | Format-Table` to narrow down.
- `taskkill /IM node.exe /F` / `Stop-Process -Name node -Force` — terminate runaway jobs.
- `systeminfo` / `Get-ComputerInfo` — quick hardware and OS overview.
- `ver` / `$PSVersionTable.PSVersion` — confirm shell versions.
- `assoc` / `Get-ItemProperty HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.txt` — inspect file associations via CLI.

Use `Ctrl + Break` (or `Ctrl + C`) to stop a running command safely, and `Ctrl + Z` to queue `Suspend` in PowerShell.

---

## Networking & Remote Workflows
- `ping google.com` / `Test-Connection google.com` — reachability checks.
- `nslookup api.openai.com` / `Resolve-DnsName api.openai.com` — inspect DNS records.
- `tracert github.com` / `Trace-Command -Name Resolve-DnsName -Expression { Test-Connection github.com }` — trace routes.
- `ipconfig /all` / `Get-NetIPAddress` — inspect IP, DNS, and adapter details.
- `netstat -ano` / `Get-NetTCPConnection | Sort-Object State` — find sockets with associated PID.

Pipe outputs to `more` or redirect to files for logs: `ipconfig /all > network.txt` or `Get-NetIPAddress | Out-File network.txt`.

---

## Power User Techniques
- **Clipboard without mouse:** `Ctrl + C` copies selected text automatically; use `Alt + Space`, `E`, `L` to enable Quick Edit.
- **Command history:** `F7` to open history menu; `doskey /history` lists typed commands. PowerShell's `Get-History` and `Invoke-History` let you replay entries.
- **Aliases:** PowerShell includes `ls`, `cat`, `rm`—they map to native cmdlets. Define your own with `Set-Alias gs git status`.
- **Chaining commands:** `mkdir temp && cd temp && type nul > readme.md` or `New-Item temp -ItemType Directory; Set-Location temp; New-Item readme.md -ItemType File`.
- **Tabs & autocompletion:** Press `Ctrl + R` (PowerShell) or `F8` (CMD) to cycle through previous commands that match what you type.
- **Scripting on the fly:** Save multi-line scripts with `PowerShell -NoProfile -Command "@' <script> '@"` or `cmd /c "(echo line1&echo line2)>script.bat"`.

---

## Shell Customization & Environment Variables
| Task | Command Prompt | PowerShell |
| --- | --- | --- |
| View env vars | `set` | `Get-ChildItem Env:` |
| Temporarily set | `set PATH=C:\Python310;%PATH%` | `$env:PATH = "C:\Python310;" + $env:PATH` |
| Search the history | `doskey /history | findstr python` | `Get-History | Where-Object CommandLine -Match python` |
| Prompt tweak (one line) | `prompt $P$G` | `function prompt { "PS " + (Get-Location) + "> " }` |

Persist changes by editing your PowerShell profile (`notepad $PROFILE`) or Windows environment variables in System Properties (opened with `Control Panel\System`).

---

## Learning & Practice Ideas
1. Build a keyboard-only workflow: open CMD, navigate to a project, create a file, edit it with `notepad`, and then use `type` to confirm contents—no mouse.
2. Create a 2-column comparison document of CMD vs PowerShell commands, then execute each to build confidence.
3. Automate a daily checklist by writing a one-liner script that archives logs, renames them by date, and uploads via `az` or `gh` CLI.
4. Practice PowerShell pipeline mastery: combine `Get-ChildItem` with `Where-Object` and `Out-File` to produce reports.

---

## Resources & Shortcut Cheat Sheet
- `Windows Terminal` (Win + X → Windows Terminal) keeps tabs for CMD, PowerShell, and WSL.
- `Ctrl + Shift + T` reopens the last closed tab in Windows Terminal.
- `Win + D` and `Win + ,` help you peek at the desktop without leaving the shell.
- Bookmark `learn.microsoft.com/windows-server/administration/windows-commands` for an exhaustive command list.
- The PowerShell gallery (`https://www.powershellgallery.com`) is a great place to import modules with `Install-Module`.

---

Share this README, practice daily, and keep a keyboard-first mindset: every repetition locks in muscle memory for the shortcuts, scripts, and flow control you need as an AI or dev power user.

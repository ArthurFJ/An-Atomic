# Shell & Bash Programming Course
A structured **Shell and Bash** terminal course for fundamental comamands and automation.

## Contents
1. [Prerequisites](#prerequisites)
2. [Modules](#modules)
3. [Exercises](#exercises)
4. [Final Project](#final-project)

## Prerequisites
- A Unix-like OS (Linux, macOS, or WSL2 on Windows)
- Terminal access (bash, zsh, etc.)

## Modules
### Module 1: Terminal Basics
- **Lecture 1**: Shell vs Terminal, CLI vs GUI, basic navigation (`ls`, `cd`, `pwd`)
- **Exercise**: Navigate a list of files and directories

### Module 2: File Operations
- **Lecture**: `cp`, `mv`, `rm`, `mkdir`, `touch`, and file permissions (`chmod`)
- **Exercise**: Organize a messy directory (`/tmp/clutter`)

### Module 3: Text Manipulation
- **Lecture**: `cat`, `grep`, `sed`, `awk`, `head`, `tail`
- **Exercise**: Extract specific lines from a log file

### Module 4: Redirection & Pipes
- **Lecture**: `>`, `>>`, `|`, `2>`, `tee`
- **Exercise**: Filter and save process data (`ps aux | grep`)

### Module 5: Environment & Variables
- **Lecture**: `$PATH`, `export`, `env`, `alias`
- **Exercise**: Create a custom command shortcut

### Module 6: Process Management
- **Lecture**: `ps`, `top`, `kill`, `jobs`, `bg`, `fg`
- **Exercise**: Monitor and manage running processes

### Module 7: Shell Scripting Basics
- **Lecture**: Shebang (`#!/bin/bash`), variables, `echo`, `read`
- **Exercise**: Write a "Hello, $USER!" script

### Module 8: Conditional Statements
- **Lecture**: `if-then-else`, `test`/`[ ]`, `case`
- **Exercise**: A script that checks disk space

### Module 9: Loops & Automation
- **Lecture**: `for`, `while`, `until`
- **Exercise**: Rename all `.txt` files in a directory

### Module 10: Functions & Script Organization
- **Lecture**: Defining functions, `source`, modular scripts
- **Exercise**: Build a reusable backup function

### Module 11: Advanced Text Processing
- **Lecture**: `cut`, `paste`, `tr`, `sort`, `uniq`
- **Exercise**: Analyze a CSV file with CLI tools

### Module 12: Job Scheduling
- **Lecture**: `cron`, `at`, systemd timers
- **Exercise**: Schedule a daily backup script

### Module 13: Networking Commands
- **Lecture**: `ping`, `curl`, `wget`, `ssh`, `scp`
- **Exercise**: Fetch and parse a webpage

### Module 14: Debugging & Optimization
- **Lecture**: `set -x`, `strace`, `time`, `bash -n`
- **Exercise**: Profile a slow script

### Module 15: Advanced Bash Features
- **Lecture**: Arrays, associative arrays, `getopts`, `trap`
- **Exercise**: Build a CLI tool with options

## Exercises
- Directory: `/exercises/`
- Solutions: `/solutions/` (or branch `solutions`)

## Final Project
- Description: Build a System Monitoring Dashboard.
    - A Bash script that displays:
    - CPU/RAM usage
    - Disk space
    - Network stats
    - Running processes
- Optional: Output to a web interface (e.g., curl Localhost:8080).
- Submission: Submission: GitHub Repo or short video demo including script(s) to be sent in the submission form [To be created]

## License
[ALFJ](/LICENSE)
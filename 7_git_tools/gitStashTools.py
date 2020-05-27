#!/usr/bin/env python
import os, sys
from utils import showStatus, clear, output, manualMode

# Utils
def showStash():
  print('*** Stash List ***')
  os.system('git stash list')

def commonCmdLoop(opMsg, systemCmd):
  clear()
  index = ""
  while index != "b":
    output(opMsg + " or " + extraOptions)
    print("")
    showStash()
    index = input("""

Index: """)
    manualMode(index)
    if index == 't':
      showStatus()
    else:
      os.system(systemCmd + " stash@{" + index + "}")
  clear()

extraOptions = "(b)-back | (m)-manual mode, (t)-git status"

# Check if current directory is a git repo
try:
  with open('./.git/HEAD') as f:
    clear()
    print("Welcome To Stash Tools!")
except IOError:
  print("This is not a git repository")


# Start the command loop
while True:
  # Process arguments
  mode = input("""
Choose a mode:

(s)ave mode: Save a stash
(a)pply mode: Apply a stash
(v)iew mode: View a stash
(d)rop mode: Drop a stash
(m)anual mode: Execute commands without leaving the program

Extras:
(t) git status
(q)uit

:""")

  manualMode(mode)

  if mode == 'q':
    clear()
    sys.exit()
  elif mode == 't':
    clear()
    showStatus()
  elif mode == 's':
    clear()
    stashMode = input("""
Choose a stash option:

(d)efault: Stash all changes as last commit message
(m)essage: Stash all changes with your own stash message
(p)ick: Stash changes in groups with your own stash message
(b)ack: <-
""")

    if stashMode == 'd':
      os.system("git stash")
    elif stashMode == 'm':
      msg = input("Enter a stash message: ")
      os.system("git stash save " + msg)
    elif stashMode == 'p':
      msg = input("Enter a stash message: ")
      os.system("git stash save -p " + msg)

  elif mode == 'a':
    commonCmdLoop(
      "Choose an index to apply",
      "git stash apply"
    )
  elif mode == 'v':
    commonCmdLoop(
      "Choose an index to view the stash diff",
      "git stash show -p"
    )
  elif mode == 'd':
    commonCmdLoop(
      "Choose an index to drop a stash",
      "git stash drop"
    )
  else:
    output("Command not supported.")

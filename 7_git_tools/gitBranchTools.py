#!/usr/bin/env python
import os, sys
from utils import showStatus, clear, output, manualMode

# Variables
extraOptions = "(b)-back | (m)-manual mode, (t)-git status"
stepOptions = "(b)-back a step | (e)-exit branch mode"
types = [
  'build',
  'ci',
  'docs',
  'feat',
  'fix',
  'perf',
  'refactor',
  'style',
  'test'
]

# Utils
def getIndexedBranches(branches):
  options = ""
  for index, branch in enumerate(branches):
    if branch != "":
      options += "[{}]: {}\n".format(index, branch)
  return options

def commonCmdLoop(opMsg, systemCmd):
  clear()
  index = ""
  while index != "b":
    output(opMsg + " or " + extraOptions)
    branches = os.popen('git branch').read()
    splitBranches = branches.split("\n")
    indexedBranches = getIndexedBranches(splitBranches)
    print(indexedBranches)
    index = input("""

Index: """)
    if index == 't':
      showStatus()
    elif index == 'm':
      manualMode(index)
    elif index == 'b':
      clear()
    else:
      os.system(systemCmd + " " + splitBranches[int(index)])

def createNewBranch():
  branch_type = ""
  ticket_id = ""
  ticket_name = ""
  joined_name = ""
  branch_name = ""
  step = 1
  while branch_name == "" and step != 0:
    while step == 1:
      clear()
      output("Pick a branch type by index or " + stepOptions)
      for index in range(len(types)):
        print("[{}]: {}".format(index, types[index]))
      index = input("""

Index: """)
      if index == 'b':
        step = 0
      elif index == 'e':
        step = 0
        branch_name = "exit"
      else:
        branch_type = index
        step = step + 1
    
    while step == 2:
      clear()
      output("Enter your ticket ID or " + stepOptions)
      t_id = input("""

Ticket ID: """)
      if t_id == 'b':
        step = 1
      elif t_id == 'e':
        step = 0
        branch_name = "exit"
      else:
        ticket_id = t_id
        step = step + 1

    while step == 3:
      clear()
      print("Example: add styles to component")
      output("Enter your ticket name or " + stepOptions)
      t_name = input("""

Ticket Name: """)
      if t_name == 'b':
        step = 2
      elif t_name == 'e':
        step = 0
        branch_name = "exit"
      else:
        ticket_name = t_name
        step = step + 1

    if ticket_name != "" and ticket_name != 'b' and ticket_name != 'e':
      split_name = ticket_name.split(" ")
      joined_name = "-".join(split_name)
      branch_name = "{}/{}-{}".format(
        types[int(branch_type)],
        ticket_id,
        joined_name
      )

  if branch_name != "" and branch_name != "exit":
    os.system("git checkout -b " + branch_name)

# Check if current directory is a git repo
try:
  with open('./.git/HEAD') as f:
    clear()
    print("Welcome To Branch Tools!")
except IOError:
  print("This is not a git repository")


# Start the command loop
while True:
  # Process arguments
  mode = input("""
Choose a mode:

(c)ommit mode: Commit branch changes
(ck)eckout mode: Checkout a branch
(n)ew branch mode: Create a new branch
(d)elete mode: Delete a branch
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
  elif mode == 'c':
    print('c')
    # git commit -m <commitMessage>
    # get current branch name and auto fill commit message to start
    # Look into multi-line input values for more complex commit messages
    # perhaps parse value for double quotes to detect an end to commit message
    # and each new line is a new input().
  elif mode == 'ck':
    commonCmdLoop(
      "Choose a branch to checkout",
      "git checkout"
    )
  elif mode == 'n':
    createNewBranch()
  elif mode == 'd':
    commonCmdLoop(
      "Choose a branch to delete",
      "git branch -d"
    )
  else:
    output("Command not supported.")

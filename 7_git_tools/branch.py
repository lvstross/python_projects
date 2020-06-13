import os, sys
from utils import showStatus, clear, output, manualMode

# Variables
extraOptions = "(b)-back | (~)-execute any command, (t)-git status"
stepOptions = "(b)-back a step | (e)-exit branch mode"
types = [
  "build",
  "ci",
  "docs",
  "feat",
  "fix",
  "perf",
  "refactor",
  "style",
  "test"
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
    branches = os.popen("git branch").read()
    splitBranches = branches.split("\n")
    indexedBranches = getIndexedBranches(splitBranches)
    print(indexedBranches)
    index = input("""

Index: """)
    if index == "t":
      showStatus()
    else:
      if index.isdigit():
        os.system(systemCmd + " " + splitBranches[int(index)])
      else:
        output("Index must be an integer!")
    manualMode(index)

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
      if index == "b":
        step = 0
      elif index == "e":
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
      if t_id == "b":
        step = 1
      elif t_id == "e":
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
      if t_name == "b":
        step = 2
      elif t_name == "e":
        step = 0
        branch_name = "exit"
      else:
        ticket_name = t_name
        step = step + 1

    if ticket_name != "" and ticket_name != "b" and ticket_name != "e":
      split_name = ticket_name.split(" ")
      joined_name = "-".join(split_name)
      branch_name = "{}/{}-{}".format(
        types[int(branch_type)],
        ticket_id,
        joined_name
      )

  if branch_name != "" and branch_name != "exit":
    os.system("git checkout -b " + branch_name)


# Start the command loop
def branch_tool():
  tool_on = True
  while tool_on:
    # Process arguments
    mode = input("""
Choose a mode:

(ck)eckout mode: Checkout a branch
(n)ew branch mode: Create a new branch
(d)elete mode: Delete a branch

Extras:
Include ~ in front of your command to execute any command
(t) git status
(e)xit tool
(q)uit

:""")

    if mode == "e":
      clear()
      tool_on = False
    elif mode == "q":
      clear()
      sys.exit()
    elif mode == "t":
      clear()
      showStatus()
    elif mode == "ck":
      commonCmdLoop(
        "Choose a branch to checkout",
        "git checkout"
      )
    elif mode == "n":
      createNewBranch()
    elif mode == "d":
      commonCmdLoop(
        "Choose a branch to delete",
        "git branch -D"
      )
    else:
      manualMode(mode)

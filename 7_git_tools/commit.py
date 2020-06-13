import os, sys
from utils import showStatus, clear, output, manualMode

# Variables
extraOptions = "(b)-back | (~)-execute any command, (t)-git status"

# Utils
def commonCmdLoop(opMsg, systemCmd, contained, excluded):
  clear()
  index = ""
  while index != "b":
    output(opMsg + " or " + extraOptions)
    files = os.popen("git status -s").read()
    splitFiles = files.split("\n")
    options = ""
    for i, file in enumerate(splitFiles):
      if contained in file and excluded not in file:
        options += "[{}]: {}\n".format(i, file)

    print(options)
    index = input("""

Index: """)
    if index == "t":
      showStatus()
    else:
      if index.isdigit():
        choosenFile = splitFiles[int(index)]
        print(systemCmd + " " + choosenFile[len(contained) + 1:])
        os.system(systemCmd + " " + choosenFile[len(contained) + 1:])
      else:
        output("Index must be an integer!")
    manualMode(index)

# Start the command loop
def commit_tool():
  tool_on = True
  while tool_on:
    #Process arguments
    mode = input("""
Choose a mode:

(a)dd mode: Add files to staging
(r)eset mode: Reset files from staging
(c)ommit mode: Commit staged changes

Extra:
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
    elif mode == "a":
      commonCmdLoop(
        "Choose which files to stage",
        "git add",
        "M ",
        "M  "
      )
    elif mode == "r":
      clear()
      index = ""
      while index != "b":
        output("Choose which files to unstage" + " or " + extraOptions)
        files = os.popen("git status -s").read()
        splitFiles = files.split("\n")
        options = ""
        for i, file in enumerate(splitFiles):
          if "M  " in file:
            options += "[{}]: {}\n".format(i, file)

        print(options)
        index = input("""

Index: """)
        if index == "t":
          showStatus()
        else:
          if index.isdigit():
            choosenFile = splitFiles[int(index)]
            print("git reset" + " " + choosenFile[len("M  "):])
            os.system("git reset" + " " + choosenFile[len("M  "):])
          else:
            output("Index must be an integer!")
        manualMode(index)
    elif mode == "c":
      print("using commit mode")
      # git commit -m <commitMessage>
      # get current branch name and auto fill commit message to start
      # Look into multi-line input values for more complex commit messages
      # perhaps parse value for double quotes to detect an end to commit message
      # and each new line is a new input() call in the loop.
    else:
      manualMode(mode)
import os, sys
from utils import showStatus, clear, output, manualMode

# Variables
extraOptions = "(b)-back | (~)-execute any command, (t)-git status"

# Utils
def commonCmdLoop(opMsg, systemCmd, contained, excluded):
  # @Note: 
  # Need to account for other status options (M, A, D, R, C, U)
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
(d)iscard mode: Discard unstaged changes
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
    elif mode == "d":
      commonCmdLoop(
        "Choose which files to stage",
        "git checkout",
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
      clear()
      inputValue = ""
      msg = ""
      while inputValue != "b":
        clear()
        output("Enter your commit message and end it with '##'")
        output("To exit this commit, include 'exit' in the message")
        inputValue = input("""

Message: {}""".format(msg))
        msg += "{}\n".format(inputValue)
        if "##" in msg:
          msg = msg.replace("##", "")
          os.system("git commit -m " + '"{}"'.format(msg))
          inputValue = "b"
        elif "exit" in msg:
          inputValue = "b"
    else:
      manualMode(mode)
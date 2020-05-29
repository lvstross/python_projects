import os

def showStatus():
  os.system("git status")

def showBranch():
  os.system("git branch")

def clear():
  os.system("clear")

def output(o):
  print("Output: {}".format(o))

def manualMode(arg):
  if "~" in arg:
    clear()
    os.system(arg[1:])
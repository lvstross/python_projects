import os

def showStatus():
  os.system("git status")

def clear():
  os.system('clear')

def output(o):
  print("Output: {}".format(o))

def manualMode(arg):
  if arg == 'm':
    clear()
    cmd = ""
    while cmd != "b":
      output("Manual Mode - (b)ack <-")
      cmd = input("~ ")
      os.system(cmd)
    clear()
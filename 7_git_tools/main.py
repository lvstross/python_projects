#!/usr/bin/env python
import sys
from utils import clear, output, manualMode
from stash import stash_tool
from branch import branch_tool

# Check if current directory is a git repo
try:
  with open('./.git/HEAD') as f:
    clear()
except IOError:
  print("This is not a git repository")


# Get initial starting point
while True:
  tool = input("""
Choose a tool:

(b)ranch tools
(s)tash tools
Include ~ in front of your command to execute any command

(q)uit

:""")

  if tool == 'b':
    clear()
    branch_tool()
  elif tool == 's':
    clear()
    stash_tool()
  elif tool == 'q':
    sys.exit()
  else:
    manualMode(tool)
import pyperclip
contents = """Line 1 of content
Line 2 of content
Line 3 of content
    Line 4 of content with spaces"""
pyperclip.copy(contents)
clip = pyperclip.paste()

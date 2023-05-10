import stdout
import os
write = stdout.write
width = os.get_terminal_size().columns

def oneLine():
    write('\u001b[38;5;47m')
    for i in range(width):
        write('-')
    write('\u001b[39m\n')

def blank(chars:int):
    blanks = width-chars
    for i in range(blanks):
        write(' ')

def charLen(text:str):
    a = 0
    ps = False
    for header in text:
        if header == '\u001b':
            ps = True
        if ps == True:
            if header == 'm':
                ps = False
        else:
            a += 1 if unicodedata.east_asian_width(header) not in 'WF' else 2
    return a

def fullWidth(leftText:str,rightText:str):
    write(leftText)
    blanks = width - charLen(leftText) - charLen(rightText)
    write(' '*blanks)
    write(rightText)
    write('\n')
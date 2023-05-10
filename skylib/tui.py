from sys import stdout
import os
import unicodedata
write = stdout.write
width = os.get_terminal_size().columns

def oneLine(color:int=None):
    ''' ダッシュ(-)로 된 줄 한 줄을 긋는 코드
    color : 사용할 색상(256컬러 체계, 38;5;(숫자) 에서 뒤의 숫자만 적으면 됨), 없는 경우 39(터미널 기본색상)로 간주'''
    if color is not None:
        write(f'\u001b[38;5;{color}m')
    else:
        write('\u001b[39m')
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
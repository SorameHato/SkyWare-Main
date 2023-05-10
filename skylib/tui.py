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
    '''현재 터미널의 너비로부터 입력받은 글자의 너비를 뺀 만큼의 공백을 출력
    원래는 왼쪽 문구를 출력하고 blank 함수를 호출하고 그 다음에 오른쪽 문구를 출력하는 식으로 사용했음
    하위 호환을 위해 남긴 것이므로 가급적이면 사용 금지
    chars : 직접 센 왼쪽 문구 + 오른쪽 문구의 글자 수 (전각 문자는 2, 반각 문자는 1로 카운트)'''
    blanks = width-chars
    for i in range(blanks):
        write(' ')

def charLen(text:str):
    '''입력받은 텍스트의 너비를 구하는 함수
    \u001b는 무시하도록 짜여져 있긴 하지만 \n, \t 같은 건 1로 치니까 주의할 것
    아래의 fullWidth와 연관되어서 사용하고 디버그용으로 단독 호출도 가능하게 했음
    실제 배포시엔 단독 호출은 불가능하게 해야겠지..? 근데 아마 배포할 일 같은 건 없을거야 아마
    2023년 5월 11일 기준으론 난 꿈도 희망도 가망도 없는 공시를 볼 예정인 허접 개발자인 걸
    text : 글자수를 알고 싶은 텍스트'''
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
    '''입력받은 텍스트 두 개를 하나는 왼쪽 정렬로, 하나는 오른쪽 정렬로 해서 출력하는 함수
    난 ANSI 이스케이프 코드 중 커서를 움직이는 것 같은 건 모르니까 그냥 공백을 출력하는 것으로 구현했음
    먼저 leftText를 출력하고, 그 다음 터미널의 너비에서 leftText의 너비, rightText의 너비를 뺀 너비만큼 공백을 출력하고
    그 다음에 rightText를 출력하고 \n을 출력하는 함수
    즉 예전에 했던 걸 자동화(?)한거라고 보면 됨
    charLen 함수와 연동되어서 작동함'''
    write(leftText)
    blanks = width - charLen(leftText) - charLen(rightText)
    write(' '*blanks)
    write(rightText)
    write('\n')
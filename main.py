from datetime import datetime as dt
from sys import stdout
import os
from skylib import tui
now = dt.now()
#now = dt(2023,4,29,0,0,5,0)
write = stdout.write

write('\n\u001b[1m\u001b[38;5;45mSky\u001b[38;5;105mWare\u001b[22m\u001b[38;5;123m 업무관리 시스템\u001b[39m | ')
compareDate = dt(2011,4,30,0,0,0,0)
write(f'\u001b[38;5;123mD+{str((now-compareDate).days+1).zfill(4)} \u001b[39m')
if now.strftime('%m%d') == '0430':
    write(f'\u001b[38;5;219m{now.year-2011}\u001b[39m주년 \u001b[38;5;154mD-DAY!!\u001b[39m')
    dday_width = 14
else:
    if now.month <= 4:
        compareDate = dt(now.year,4,30,0,0,0,0)
        nextYear = now.year-2011
    else:
        compareDate = dt(now.year+1,4,30,0,0,0,0)
        nextYear = now.year-2010
    write(f'\u001b[38;5;219m{nextYear}\u001b[39m주년까지 \u001b[38;5;154mD-{str((compareDate-now).days+1).zfill(3)}\u001b[39m')
    dday_width = 16
write(f' | 오늘의 공문번호 날짜부분 : \u001b[38;5;153mS{(dt.now().year-2011)*12+dt.now().month-3}{str(dt.now().day).zfill(2)}\u001b[39m')
blank(119+dday_width)
write('v\u001b[4m20191031\u001b[0m  \u001b[38;5;118m사용자명 : \u001b[38;5;154m경영이끎부 \u001b[38;5;47m대표이사 \u001b[38;5;159m하늘토끼\u001b[0m\n\n')

print('\u001b[38;5;51m\u001b[1m하늘토끼님 마감이 엄청 많이 밀려있어요! \u001b[22m\u001b[38;5;225m 설마 일 안 하고 노실 건 아니죠?')

def magamPrint(magamDate:str,magamSummary:str):
    compareDate = dt.strptime(magamDate,'%Y-%m-%d')
    if compareDate > now:
        lastDate = str((now-compareDate).days).zfill(5)
    else:
        lastDate = '+\u001b[1m'+str((now-compareDate).days).zfill(4)+'\u001b[22m'
    print(f'[\u001b[38;5;153m{magamDate} \u001b[39mD\u001b[38;5;154m{lastDate}\u001b[39m] {magamSummary}')
    
magamPrint('2016-08-01','[소설]        온수전쟁 7화 마감일')
magamPrint('2021-08-01','[하늘민국]    시온 어반 네트워크선 개통')
magamPrint('2021-12-20','[하늘민국]    SR021, SR210 운용시작 / 준트님과 협의해서 아메는 교토, 호시는 고베, 일반열차는 구로테츠누마즈까지 보내기 (220117부터)')
magamPrint('2022-06-10','[하늘민국]    알피코 교통 카미코치선 전선 복구에 따른 치노시온라인 리뉴얼')
magamPrint('2022-10-31','[하늘민국]    V03.01 개편 적용 (230430까지 단계별로)')
magamPrint('2023-04-29','[개인]        논님, 파선생님, 쿠로님 sr9ht 계정으로 부르기')
magamPrint('2023-04-30','[스카이웨어]  12주년 기념 RE:Born 프로젝트 준비')
magamPrint('2023-10-31','[하늘민국]    정기 시간표 개편 / 일본진출입노선 준트님 黒鉄 新品川線 없어도 운용할 수 있게 23区内線 니지가사키~시나가와 구간 연장')
magamPrint('2024-01-31','[하늘민국]    HAETI(구 HAsTog), maFuyu 신버전 개발')
magamPrint('2024-10-31','[하늘민국]    유트, 레트에게 하늘특별시, 시온특별시 지도 보내기')
oneLine()

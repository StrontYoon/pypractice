import datetime
import time

deltaDayStr = ''


def deltaTimeCalc(inpTime):
    '''
    tdaydata = datetime.datetime(2022, 9, 17)
    tdaystr = tdaydata.strftime('%y%m%d')

    print(tdaydata)
    print(tday)
    '''
    tday = datetime.datetime(int(inpTime[:2]) + 2000,int(inpTime[2:4]),int(inpTime[4:]))
    deductDay = datetime.datetime(2022,9,14) #today time to data

    deltaDay = tday - deductDay
    print(deltaDay.days)

    global deltaDayStr
    deltaDayStr = deltaDay.days
    return 0


def lyj(delta):
    case = (delta + 1) % 12 
    rtstr = 'dd'
    if case == 0:
        rtstr = '주간'
    elif case == 1:
        rtstr = '주간'
    elif case == 2:
        rtstr = '주간'
    elif case == 3:
        rtstr = '주간'
    elif case == 4:
        rtstr = '휴식'
    elif case == 5:
        rtstr = '휴식'
    elif case == 6:
        rtstr = '야간'
    elif case == 7:
        rtstr = '야간'
    elif case == 8:
        rtstr = '야간'
    elif case == 9:
        rtstr = '야간'
    elif case == 10:
        rtstr = '휴식'
    elif case == 11:
        rtstr = '휴식'
    else:
        rtstr = '몰라! 콘'
    return rtstr

def ksh(delta):
    case = delta % 4
    if case == 0:
        rtstrr = '주간'
    elif case == 1:
        rtstrr = '야간'
    elif case == 2:
        rtstrr = '비번'
    elif case == 3:
        rtstrr = '휴식'
    else:
        rtstrr = '몰?루'
    return rtstrr

    
# 220914 lyj delta == 0
# 220914 ksh delta == 0 


print('드림팀 노역계산기 v2')
print('오늘 날짜를 yymmdd 형식으로 ㄱㄱ:')
inputTime = '230103' # change to input
print('입력일부터 기준일까지 차이는 ', end = '')
deltaTimeCalc(inputTime) 
print('unlayak의 그날 근무는 ' + ksh(deltaDayStr) + '이고')
print('pacific의 그날 근무는 ' + lyj(deltaDayStr) + '이야! -sty')


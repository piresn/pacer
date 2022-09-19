def time_to_pace(x):
    
    units=x.split(":")

    hours, minutes, seconds = 0, 0, 0

    seconds = units.pop(-1)

    if len(units) > 0:
        minutes = units.pop(-1)

    if len(units) > 0:
        hours = units.pop(-1)
    
    return hours, minutes, seconds


time_to_pace("1:59:01")

def kmh_to_seckm(x):
     return round(3600/x)

def seckm_to_minkm(x, decimals):
    min = f'{int(x//60)}'
    sec = x%60

    if decimals>0:
        sec_align = f'{int(sec)}'.zfill(2) + '.' + f'{round(10**decimals*(sec-int(sec)))}'
    else:
        sec_align = f'{round(sec)}'.zfill(2)
    return f'{min}:{sec_align}'

def kmh_to_pace(x, decimals):
    x = kmh_to_seckm(x)
    x = seckm_to_minkm(x, decimals)
    return x

def calculate_overall_time(distance, speed):

    total_seconds = (distance*3600)/(speed*1000)

    #TODO fix (showa e.g. 4:60 instead of 5:00)

    h=0
    m=0
    s=0
    m=total_seconds//60
    h=int(m//60)
    m=int(m%60)
    if h+m > 0:
        s=f'{round(total_seconds%60)}'.zfill(2)
    elif h+m==0:
        s=f'{round(total_seconds%60, 2)}'.zfill(5)


    return f'{h}:' + f'{m}'.zfill(2) + f':{s}'


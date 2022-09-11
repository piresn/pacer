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

    #TODO fix

    h=0
    m=0
    s=0
    m=total_seconds//60
    s=round(total_seconds%60, 1)
    h=m//60
    m=m%60

    return f'{h}:{m}:{s}'


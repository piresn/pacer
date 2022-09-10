def kmh_to_seckm(x):
     return round(3600/x)

def seckm_to_string(x):
    min = f'{x//60}'
    sec = f'{x%60}'.zfill(2)
    return f'{min}:{sec}'

def kmh_to_pace(x):
    x = kmh_to_seckm(x)
    x = seckm_to_string(x)
    return x

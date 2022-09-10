def kmh_to_seckm(x):
     return round(3600/x)

def seckm_to_string(x, decimals):
    min = f'{int(x//60)}'
    sec = x%60

    if decimals:
        sec_align = f'{int(sec)}'.zfill(2) + '.' + f'{round(10*(sec-int(sec)))}'
    else:
        sec_align = f'{round(sec)}'.zfill(2)
    return f'{min}:{sec_align}'

def kmh_to_pace(x):
    x = kmh_to_seckm(x)
    x = seckm_to_string(x)
    return x

class Pace:
    """
    Creates paces, store as seconds per km and print as min:sec per km.
    """
    def __init__(self):
        self.pace=None

    def pace_from_kmh(self, kmh):
        self.pace=kmh_to_seckm(kmh)

    def pace_from_distance(self, meters, seconds, hours=0, minutes=0):
        time = seconds+60*minutes+3600*hours
        km = meters/1000
        self.pace = time/km

    def print(self):
        return seckm_to_string(self.pace, decimals=False)




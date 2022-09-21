from helpers import *
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
        self.distanceEvent = meters
        self.pace = time/km

    def print(self, decimals=0, unit='minkm'):

        if unit=='minkm':
            return seckm_to_minkm(self.pace, decimals=decimals)
        elif unit=='kmh':
            out = 3600/self.pace
            if decimals > 0:
                return round(out, decimals)
            else:
                return round(out)
        elif unit=='secskm':
            return self.pace

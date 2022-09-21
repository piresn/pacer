from helpers import *
class Pace:
    """
    Creates paces, store as seconds per km and print as min:sec per km.
    """
    def __init__(self, meters, seconds, hours=0, minutes=0):
        self.pace=None
        self.time = seconds+60*minutes+3600*hours        
        self.distanceEvent = meters
        self.pace = self.time/(meters/1000)

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
